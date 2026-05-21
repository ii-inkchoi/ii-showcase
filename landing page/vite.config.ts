import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { resolve } from 'path'

export default defineConfig({
  // Use relative asset paths so the built site works under any sub-path
  // (e.g. GitHub Pages: https://<user>.github.io/<repo>/landing%20page/dist/landing.html)
  base: './',
  plugins: [react()],
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        landing: resolve(__dirname, 'landing.html'),
      },
    },
  },
})
