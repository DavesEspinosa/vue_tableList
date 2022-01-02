from selectors import response, separatorHead, objectToCompare, create_json

url_thorlabs = "https://www.thorlabs.com/newgrouppage9.cfm?objectgroup_id=112"
url_optoSigma = "https://www.optosigma.com/eu_en/spherical-lens-bk7-plano-convex-uncoated-SLB-P.html"
provider = ["Thorlabs", "OptoSigma"]

def thorlabs(url):
    table_main_info = response(url).find_all('table', class_="SpecTable", width="100%")
    table_price_name = response(url).select('tr[class*="AltRow"]')
    header_content = table_main_info[2].thead.find_all('th')

    main_info = []
    extra_info = []
    result = []

    for test in table_price_name:
        sku = test.find('td', class_="prodNumber partNumLT8").text
        price = test.find('td', class_="CSS4", align="right", style="padding-right: 15px;").text
        name = test.find('td', class_="prodDesc").text.replace("Ø", "D")
        extra_info.append({ 
            "sku": sku, 
            "price": price, 
            "provider": provider[0], 
            'name': name[0: name.index(", D")]
            })

    separatorHead(header_content)

    for table in table_main_info:
        main_info.append(table.find('tbody'))

    del main_info[:2]

    for details in main_info:
        for extract in details.find_all('tr'):
            iteration = []
            for cell in extract.find_all('td'):
                if not cell.find('a'):
                    iteration.append(cell.text.replace('\n', ' ').strip())

            for key in extra_info:
                if key['sku'] == iteration[0]:
                    data = objectToCompare(iteration[0],key['name'], key['provider'], iteration[1] + " mm", iteration[2] + " mm", key['price'])
            result.append({iteration[0]: data })

    create_json(result, "thorlabs.json")

def optoSigma(url):
    table = response(url).find('table', id="super-product-table")
    header_content = table.find('tr', class_="grouped-items-head")
    content = table.find('tbody')

    result = []

    separatorHead(header_content.find_all('th'))

    for item in content.find_all('tr', class_="grouped-item"):
        sku = item.find('span').text.replace('\n', ' ').strip()
        diameter = item.find('td', attrs={"data-label": "Diameter φD"}).text.replace('\n', ' ').strip()
        focal_length = item.find('td', attrs={"data-label": "Focal length"}).text.replace('\n', ' ').strip()
        price = item.find('span', class_="price").text.replace("€", "") + " €"
        name = item.find('a', class_='link').text.replace('\n', ' ').strip()

        data = objectToCompare(sku, name[0: name.index("Diameter")], provider[1], diameter, focal_length, price)
        result.append({sku: data})

    create_json(result, "optoSigma.json")

thorlabs(url_thorlabs)
optoSigma(url_optoSigma)

