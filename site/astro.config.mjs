import { defineConfig } from 'astro/config';

export default defineConfig({
  base: '/data_rein/',
  outDir: '../docs',
  build: {
    format: 'file',
  },
});
