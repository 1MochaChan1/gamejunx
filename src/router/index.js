import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import GamesView from '../views/GamesView.vue';

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            component: () => HomeView
        },
        {
            path: '/games',
            component: () => GamesView
        },
    ]
})

export default router;