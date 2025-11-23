// src/main.ts

import { createApp } from 'vue';
import App from './App.vue';
import router from './router/index.js'; 

// 1. IMPORTAR CSS de Bootstrap (para los estilos)
import 'bootstrap/dist/css/bootstrap.css'; // <-- FALTANTE

// 2. IMPORTAR JS de Bootstrap (para interacciones como modales)
import 'bootstrap/dist/js/bootstrap.bundle.min.js'; // <-- FALTANTE

const app = createApp(App);

app.use(router); 

app.mount('#app');