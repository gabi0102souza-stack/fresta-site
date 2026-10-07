// Native vector artwork and official avatar only; no synthetic restaurant photos.
const fs = require('node:fs');
const path = require('node:path');
const sharp = require(require.resolve('sharp', { paths: process.env.FRESTA_NODE_MODULES ? [process.env.FRESTA_NODE_MODULES] : [__dirname] }));
const root = path.resolve(__dirname, '..');
(async () => {
  await sharp(path.join(root, 'design/official-avatar-source.jpeg')).resize(128, 128).webp({quality: 95}).toFile(path.join(root, 'dist/images/fresta-symbol.webp'));
  await sharp(path.join(root, 'design/official-avatar-source.jpeg')).resize(64, 64).png().toFile(path.join(root, 'dist/favicon.png'));
  await sharp(path.join(root, 'design/og-fresta.svg')).png().toFile(path.join(root, 'dist/og-fresta.png'));
  console.log('Official avatar: 128 × 128 WebP. Favicon: 64 × 64 PNG. Social card: 1200 × 630 PNG.');
})().catch(error => { console.error(error); process.exitCode = 1; });
