import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  // Served under the GitHub Pages /blog/ subpath — keep base and
  // <BrowserRouter basename="/blog"> in sync (see AGENTS.md).
  base: "/blog/",
});
