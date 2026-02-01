//Bootstraps the React application and mounts it to the DOM.
//Serves as the entry point where React takes control of the HTML page.

import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
