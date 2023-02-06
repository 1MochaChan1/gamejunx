import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import WishlistView from '../views/WishlistView.vue';
import GamesView from '../views/GamesView.vue';
import LibrariesView from '../views/LibrariesView.vue';
import ProfileView from '../views/ProfileView.vue';
import SettingsView from '../views/SettingsView.vue';

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            component: () => HomeView
        },
        {
            path: '/wishlist',
            component: () => WishlistView
        },
        {
            path: '/games',
            component: () => GamesView
        },
        {
            path: '/libraries',
            component: () => LibrariesView
        },
        {
            path: '/profile',
            component: () => ProfileView
        },
        {
            path: '/settings',
            component: () => SettingsView
        },
    ]
})

export default router;