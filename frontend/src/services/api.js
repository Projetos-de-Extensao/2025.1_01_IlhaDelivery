// filepath: frontend/src/services/api.js
import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api/';

export const getPedidos = () => axios.get(`${API_BASE_URL}pedidos/`);
// Add more functions for other endpoints as needed