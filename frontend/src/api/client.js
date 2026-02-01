//Creates a preconfigured Axios instance pointing to the FastAPI backend.
//Acts as the single gateway for all frontend → backend API calls.

import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000",
});

export default api;
