// Em algum lugar no seu setup do React, ex: main.jsx ou App.jsx, ou um arquivo dedicado api.js
import axios from 'axios';

const DEMO_AUTH_TOKEN = '0bd520d8381fa8a7d52f7303b35d6ab96ea8fd5a';
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api'; // Usando variável de ambiente

// Configuração global do Axios
axios.defaults.baseURL = API_BASE_URL;
if (DEMO_AUTH_TOKEN) {
  axios.defaults.headers.common['Authorization'] = `Token ${DEMO_AUTH_TOKEN}`;
} else {
  console.warn("Token de autenticação de demonstração não definido. As chamadas à API podem falhar.");
}

export default axios; // Exporte a instância configurada do axios para usar em outros lugares