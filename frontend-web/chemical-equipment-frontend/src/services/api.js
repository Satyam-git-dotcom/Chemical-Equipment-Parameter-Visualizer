import axios from "axios";

const api = axios.create({
  baseURL: "https://chemical-equipment-backend.onrender.com/api/",
  auth: {
    username: "satyamDjango",
    password: "Django@123",
  },
});

export default api;