import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// Dev server proxies API + WS to the FastAPI backend; the built app is served
// by FastAPI itself in production (mirrors semantica.explorer layout).
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      "/api": "http://127.0.0.1:8088",
      "/ws": { target: "ws://127.0.0.1:8088", ws: true },
    },
  },
  build: {
    outDir: "dist",
    emptyOutDir: true,
  },
});
