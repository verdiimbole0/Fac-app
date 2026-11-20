// Convertit les figures SVG en PNG (2x) avec les polices de l'ouvrage.
// Usage : node render_png.js <dossier_svg> <dossier_png> [planche.png]
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const [, , svgDir, pngDir, sheet] = process.argv;
const fontDir = path.join(__dirname, 'fonts');
const face = (fam, file, w, st) =>
  `@font-face{font-family:'${fam}';src:url('file://${path.join(fontDir, file)}') format('woff2');font-weight:${w};font-style:${st};}`;
let css = '';
for (const w of [400, 500, 600, 700]) for (const st of ['normal', 'italic'])
  css += face('Inter', `inter-latin-${w}-${st}.woff2`, w, st);
for (const w of [600, 700, 800]) css += face('Outfit', `outfit-latin-${w}-normal.woff2`, w, 'normal');

(async () => {
  fs.mkdirSync(pngDir, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ deviceScaleFactor: 2 });
  const files = fs.readdirSync(svgDir).filter(f => f.endsWith('.svg')).sort();
  for (const f of files) {
    const svg = fs.readFileSync(path.join(svgDir, f), 'utf8');
    const tmp = path.join(pngDir, '_tmp.html');
    fs.writeFileSync(tmp, `<html><head><style>${css} body{margin:0}</style></head><body>${svg}</body></html>`);
    await page.goto('file://' + tmp);
    await page.evaluate(() => document.fonts.ready);
    const el = await page.$('svg');
    await el.screenshot({ path: path.join(pngDir, f.replace('.svg', '.png')) });
  }
  if (sheet) {
    const imgs = files.map(f => `<div><img src="file://${path.join(pngDir, f.replace('.svg', '.png'))}" style="width:100%"><p>${f}</p></div>`).join('');
    const tmp = path.join(pngDir, '_sheet.html');
    fs.writeFileSync(tmp, `<html><body style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;width:1500px;font:10px sans-serif">${imgs}</body></html>`);
    const p2 = await browser.newPage({ deviceScaleFactor: 1, viewport: { width: 1500, height: 800 } });
    await p2.goto('file://' + tmp);
    await p2.screenshot({ path: sheet, fullPage: true });
  }
  for (const t of ['_tmp.html', '_sheet.html']) { try { fs.unlinkSync(path.join(pngDir, t)); } catch (e) {} }
  await browser.close();
  console.log(files.length + ' PNG');
})();
