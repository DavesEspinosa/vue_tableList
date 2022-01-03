<template>
  <v-card>
     <v-btn v-if="selected.length <= 1"
      disabled
      color="secondary"
      elevation="12"
    >Compare Products {{`(${selected.length})`}}
    </v-btn>
    <v-btn v-else
      color="secondary"
      elevation="12"
      v-on:click="compare()"
    >Compare Products {{`(${selected.length})`}}
    </v-btn>
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
  name: 'Table',
  mounted() {
    this.products = optoSigma.concat(thorlabs)
    this.products.forEach(product => {
      this.products[product.sku] = product
    })
  },
  methods: {
    compare () { 
      if (this.selected.length > 1) {
        this.$router.push({
          name: 'Comparison',
          params: {
            comparison: this.selected,
            headers: this.headers
          }
        })
      } else {
        alert('Please select at least two products to compare')
      }
    },
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

