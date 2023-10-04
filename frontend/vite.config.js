import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import path from 'path'; 
// https://github.com/vuetifyjs/vuetify-loader/tree/next/packages/vite-plugin
import vuetify from 'vite-plugin-vuetify'
import { VitePluginFonts } from 'vite-plugin-fonts'


export default defineConfig({
  plugins: [
		vue(),
		vuetify({ autoImport: true }),
    VitePluginFonts({
      google: {
        families: [
          'Playfair Display',
          'Pacifico'  
        ],
      }
    })
	],
  build: {
    rollupOptions: {
      output: {
        entryFileNames: 'bundle.js',
      },
    },
    outDir: './dist/dist/',
  },
  server: {
    proxy: {
      '/api': 'http://localhost:8000'
    },
    https: false,
    cors: true,
  },
  resolve: {
    alias: {
      __STATIC__: path.resolve(__dirname, 'static'),
    },
  },
  publicDir: process.env.BASE_URL,
});

