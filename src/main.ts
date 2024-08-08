import './assets/main.css'
import 'bootstrap-icons/font/bootstrap-icons.css'
import 'jquery';
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
createApp(App).use(router).mount('#app')
