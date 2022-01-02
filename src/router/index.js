import Vue from 'vue'
import Router from 'vue-router'
import Table from '@/components/Table'
import Cards from '@/components/Cards'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Table,
      props: true
    },
    {
      path: '/compare',
      name: 'Comparison',
      component: Cards,
      props: true
    }
  ]
})
