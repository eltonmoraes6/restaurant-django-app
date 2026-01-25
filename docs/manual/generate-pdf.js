const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  const filePath = `file://${path.resolve('manual.html')}`;

  await page.goto(filePath, { waitUntil: 'networkidle0' });

  await page.pdf({
    path: 'manual.pdf',
    width: '1080px',
    height: '1920px',
    printBackground: true,
  });

  await browser.close();
})();
