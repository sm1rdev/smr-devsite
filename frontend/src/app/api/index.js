import axios from 'axios';


const api = axios.create({
    baseURL: "example/api",
    withCredentials: true
});

export default api
