import './style.css';
import { createApp } from 'vue'

import { fab } from '@fortawesome/free-brands-svg-icons';
import { far } from '@fortawesome/free-regular-svg-icons';
import { fas } from '@fortawesome/free-solid-svg-icons';

import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

import router from './router/index.js'
import App from './App.vue'
import axios from 'axios';

library.add(fas, far, fab);
const app = createApp(App)

app.use(router)
app.component('fa-icon', FontAwesomeIcon)

axios.defaults.headers.common['Authorization'] = 'Bearer '+ localStorage.getItem('token');
axios.defaults.headers.common['Content-Type'] = 'application/json';
app.config.globalProperties.baseUrl = 'http://127.0.0.1:5000/';
app.mount('#app')