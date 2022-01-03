<template v-if="selected.length > 0">
<div>
      <v-btn
        class="ma-2"
        color="indigo"
        dark
        v-on:click="goBack()"
      >
        <v-icon
          dark
          left
        >
          mdi-arrow-left
        </v-icon>Back
      </v-btn>
 <v-container class="grey lighten-5">
    <v-row
      no-gutters
      style="flex-wrap: nowrap;"
    >
      <v-col
        cols="2"
        class="flex-grow-0 flex-shrink-0"
      >
 <v-simple-table height="300px">
    <template>
      <tbody>
        <tr
          v-for="title in headers"
          :key="title.text"
        >
          <td>{{ title.text }}</td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>      
  </v-col>
      <v-col
        cols="1"
        style="min-width: 100px; max-width: 100%;"
        class="flex-grow-1 flex-shrink-0"
      >
      <v-sheet 
            class="mx-auto"
            elevation="5"
            max-width="90%"
        >
        <v-slide-group
        v-model="comparison"
        active-class="success"
        mobile-break-point="1000"
        >
        <v-card
            v-for="product in comparison"
            :key="product.sku"
            class="pa-2 card-padding"
            outlined
            tile
            height="300px"
        >
        <v-card-text id="text">
                <div class="text--primary">
                    <p>{{product.product}}</p>
                </div>
                <div class="text--primary">
                    <p>{{product.sku}}</p>
                </div>
                <div class="text--primary">
                    <p>{{product.diameter}}</p>
                </div>
                <div class="text--primary">
                    <p>{{product.focal_length}}</p>
                </div>
                <div class="text--primary">
                    <p>{{product.price}}</p>
                </div>
                <div class="text--primary">
                    <p>{{product.provider}}</p>
                </div>
            </v-card-text>
        </v-card>
        </v-slide-group>
      </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</div>
</template>

<script>

export default {
  name: 'Cards',
  props: ['comparison', 'headers'],
  methods: {
    goBack () { 
        this.$router.back();
    },
  }
}
</script>

<style scoped>
.text--primary {
  font-size: 1.2rem;
  height: 48px;
}
.text--primary > p{
  padding-bottom: 1rem;
  border-bottom: thin solid rgba(0,0,0,.12);
}
.text--primary:last-child p{
  border-bottom: none;
}
.text--primary:first-child p{
  font-weight: bold;
}
#text {
  padding: 0rem 2rem;
}

</style>
