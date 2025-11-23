import { createRouter, createWebHistory } from 'vue-router'

import DashboardAcesor from '../Views/DashboardAcesor.vue'



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
    path: '/acesor',
    name: 'Acesor',
    component: DashboardAcesor
    },

  ],
})

export default router
