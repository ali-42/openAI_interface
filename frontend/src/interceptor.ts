import axios, { AxiosError} from "axios"


const onFulfilled = (res: any) => {
  return res
}

const onRejected = async (error: AxiosError) => {
  if (error.response!.status === 401) {
    axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('refresh_token')}`
    const token = await axios.get('http://127.0.0.1:8000/auth/token/refresh', { withCredentials: true })
      if (token.status === 200) {
        axios.defaults.headers.common['Authorization'] = `Bearer ${token.data[0].access_token}`
        localStorage.setItem("access_token", token.data[0].access_token);
        localStorage.setItem("refresh_token", token.data[1].access_token);
      }
  }
  return error
}

axios.interceptors.response.use(onFulfilled, onRejected);
