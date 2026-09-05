import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import path from "node:path";
import { fileURLToPath } from "node:url";

const rootDir = path.dirname(fileURLToPath(import.meta.url));

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      "@": path.resolve(rootDir),
    },
  },
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          react: ["react", "react-dom", "react-router-dom"],
          motion: ["framer-motion"],
          forms: ["react-hook-form", "zod", "@hookform/resolvers"],
          charts: ["recharts"],
          spreadsheet: ["xlsx"],
          ui: ["lucide-react", "clsx", "tailwind-merge", "class-variance-authority"],
        },
      },
    },
  },
});
