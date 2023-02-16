import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import WishlistView from "../views/WishlistView.vue";
import GamesView from "../views/GamesView.vue";
import LibrariesView from "../views/LibrariesView.vue";
import ProfileView from "../views/ProfileView.vue";
import SettingsView from "../views/SettingsView.vue";
import AuthWrapper from "../components/AuthWrapper.vue";
import SignupView from "../views/SignupView.vue";
import LoginView from "../views/LoginView.vue";

const routes = [
  {
    path: "/",
    name: "wrapper",
    meta: { sidebar: false },
    component: AuthWrapper,
  },
  {
    path: "/home",
    name: "home",
    meta: { sidebar: true },
    component: HomeView,
  },

  {
    path: "/wishlist",
    name: "wishlist",
    meta: { sidebar: true },
    component: WishlistView,
  },
  {
    path: "/games",
    name: "games",
    meta: { sidebar: true },
    component: GamesView,
  },
  {
    path: "/libraries",
    name: "libraries",
    meta: { sidebar: true },
    component: LibrariesView,
  },
  {
    path: "/profile",
    name: "profile",
    meta: { sidebar: true },
    component: ProfileView,
  },
  {
    path: "/settings",
    name: "settings",
    meta: { sidebar: true },
    component: SettingsView,
  },
  {
    path: "/signup",
    meta: { sidebar: false },
    name: "signup",
    component: SignupView,
  },
  {
    path: "/login",
    meta: { sidebar: false },
    name: "login",
    component: LoginView,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

/* eslint-disable no-unused-vars */
router.beforeEach(async (to, from) => {
    let token = localStorage.getItem('token');
    if(token==null && to.name !='login'){
        return {name:'login'}
    }
});
/* eslint-enable no-unused-vars */
export default router;
