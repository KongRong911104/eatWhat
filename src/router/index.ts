import { createRouter, createWebHistory } from "vue-router";
import Login from "@/components/views/LoginPage.vue";
import Room from "@/components/views/Room.vue";
const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      component: Login,
    },
    {
      name: 'Room',
      path: "/room/:room",
      component: Room,
    },
  ],
});
export default router;
