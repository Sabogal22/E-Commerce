// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from "@tailwindcss/vite";

// https://astro.build/config
export default defineConfig({
  vite: {
    plugins: [tailwindcss()],
    
    // Agregar esto para ignorar errores de TypeScript
    build: {
      rollupOptions: {
        onwarn(warning, warn) {
          // Ignorar warnings específicos de TypeScript
          if (warning.code === 'TS_NODE_TRANSFORMS') return;
          if (warning.code === 'a11y-no-static-element-interactions') return;
          warn(warning);
        }
      }
    },
    
    // O también puedes desactivar chequeos estrictos
    esbuild: {
      target: 'es2020',
      supported: {
        'top-level-await': true
      }
    }
  },
});
