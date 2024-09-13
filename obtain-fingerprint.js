const { plugin } = require('selenium-with-fingerprints');
const { writefile } = require('sbg-utility');

// Set the service key for the plugin (you can buy it here https://bablosoft.com/directbuy/FingerprintSwitcher/2).
// Leave an empty string to use the free version.
plugin.setServiceKey('');

(async () => {
  // Get a fingerprint from the server:
  const fingerprint = await plugin.fetch({
    maxWidth: 1366, // max width pixel of device
    maxHeight: 768, // max height pixel of device
    tags: ["Microsoft Windows", "Chrome"],
    enablePrecomputedFingerprints: true
  });

  writefile(path.join(__dirname, "data/fingerprints/" + md5(fingerprint) + ".json"), fingerprint);

  // Apply fingerprint:
  plugin.useFingerprint(fingerprint);

  // Launch the browser instance:
  const driver = await plugin.launch();

  // The rest of the code is the same as for a standard `selenium` library:
  await driver.get('https://example.com');

  // Print the browser viewport size:
  console.log(
    'Viewport:',
    await driver.executeScript(() => ({
      deviceScaleFactor: window.devicePixelRatio,
      width: document.documentElement.clientWidth,
      height: document.documentElement.clientHeight,
    }))
  );

  await driver.quit();
})();