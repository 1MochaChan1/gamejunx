import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import WishlistView from '../views/WishlistView.vue';
import GamesView from '../views/GamesView.vue';
import LibrariesView from '../views/LibrariesView.vue';
import ProfileView from '../views/ProfileView.vue';
import SettingsView from '../views/SettingsView.vue';
import AuthWrapper from '../components/AuthWrapper.vue';
import SignupView from '../views/SignupView.vue';
import LoginView from '../views/LoginView.vue';

const routes =[
    {
        path: '/',
        name:'wrapper',
        component: AuthWrapper
    },
    {
        path: '/home',
        name:'home',
        component: HomeView
    },
   
    {
        path: '/wishlist',
        name:'wishlist',
        component: WishlistView
    },
    {
        path: '/games',
        name:'games',
        component: GamesView
    },
    {
        path: '/libraries',
        name:'libraries',
        component: LibrariesView
    },
    {
        path: '/profile',
        name:'profile',
        component: ProfileView
    },
    {
        path: '/settings',
        name:'settings',
        component: SettingsView
    },
    {
        path: '/signup',
        name:'signup',
        component: SignupView
    },
    {
        path: '/login',
        name:'login',
        component:  LoginView
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;