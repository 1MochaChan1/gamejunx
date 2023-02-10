import './style.css';
import { createApp } from 'vue'

import { fab } from '@fortawesome/free-brands-svg-icons';
import { far } from '@fortawesome/free-regular-svg-icons';
import { fas } from '@fortawesome/free-solid-svg-icons';

import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

import router from './router/index.js'
import App from './App.vue'
library.add(fas, far, fab);

createApp(App)
.component('fa-icon', FontAwesomeIcon)
.use(router)
.mount('#app')
