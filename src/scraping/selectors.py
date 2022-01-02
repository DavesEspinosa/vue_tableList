import requests
from bs4 import BeautifulSoup
import json

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

def response(url): return BeautifulSoup(requests.get(url, headers=headers).text, 'html.parser')

def separatorHead(head):
    headings = []
    for title in head:
        headings.append(title.text.replace('\n', ' ').strip())

def objectToCompare(sku, product, provider, diameter, focal_length, price):
    return {
        "sku": sku,
        "product": product,
        "provider": provider,
        "diameter": diameter,
        "focal_length": focal_length,
        "price": price
    }
def create_json(result, file):
    with open("src/{0}".format(file), "w", encoding='utf-8') as document:
        json.dump(result, document, indent=4, ensure_ascii=False)
