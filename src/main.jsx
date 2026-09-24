// App entry point — mounts the root component into #root.
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import "./app.css";
import App from "./app.jsx";
createRoot(document.getElementById("root")).render(
  <StrictMode>
    <App />
  </StrictMode>
);
