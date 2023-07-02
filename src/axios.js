import axios from 'axios';
const instance = axios.create({
    baseURL: 'https://api.harvardartmuseums.org/exhibition?apikey=0ab310c3-a1e2-4d38-9941-748c59b6f91a&status=current'
});
export default instance;