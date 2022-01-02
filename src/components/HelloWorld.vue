<template>
  <v-card>
    <v-btn
      color="secondary"
      elevation="12"
      v-on:click="compare"
    >Compare Products</v-btn>
    <v-card-title>
      Spherical Lenses
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search on any field..."
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table
        dark
        v-model="selected"
        :headers="headers"
        :items="products"
        item-key="sku"
        show-select
        :search="search"
        :items-per-page="10"
      >
      </v-data-table>
  </v-card>
</template>


<script>

import optoSigma from '../optoSigma.json'
import thorlabs from '../thorlabs.json'

export default {
  name: 'HelloWorld',
  methods: {
    compare: function () { 
      if(this.selected.length > 0) {
        const compareProducts = []
        for (const product of this.selected) {
            compareProducts.push({...product})
        }
        console.log(`compareProducts`, compareProducts)
      }
    }
  },
  mounted() {
    const allProducts = [...optoSigma, ...thorlabs]
    this.products = allProducts.map(data => {
      for (const key in data) {
        return data[key]
      }
    })
  },
  data () {
    return {
      search: '',
      selected: [],
      headers: [
          {
            text: 'Products',
            align: 'start',
            value: 'product',
          },
          { text: 'Item', value: 'sku' },
          { text: 'Diameter (mm)', value: 'diameter' },
          { text: 'Focal Length (mm)', value: 'focal_length' },
          { text: 'Price (€)', value: 'price' },
          { text: 'Supplier', value: 'provider' },
        ],
      products: [],

    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
