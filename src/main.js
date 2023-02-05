import './style.css';
import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index.js'

import '@fortawesome/fontawesome-svg-core';
import '@fortawesome/free-brands-svg-icons';
import '@fortawesome/free-regular-svg-icons';
import '@fortawesome/free-solid-svg-icons';


createApp(App).use(router).mount('#app')
