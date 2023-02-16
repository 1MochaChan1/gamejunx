import axios from 'axios'


/* eslint-disable no-unused-vars */
export const authfields= ['login', 'signup'];
export class AppImages {
    static login="./src/assets/images/login.jpg"
}

axios.defaults.baseURL = 'http://127.0.0.1:5000'
axios.defaults.headers.common['Authorization'] = 'Bearer '+ localStorage.getItem('token');



/* eslint-enable no-unused-vars */