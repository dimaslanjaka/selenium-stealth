import os
import re
import time
import traceback
from typing import Any, Dict

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

from selenium_stealth.preferences import Preferences
from selenium_stealth.main import stealth2
from selenium_stealth.utils import read_json_file
from fingerprint_validator import validate_fingerprint

current_dir = os.path.dirname(os.path.abspath(__file__))


# webdriver start

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

# options.add_argument("--headless")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

driver = None

try:
    driver = webdriver.Chrome(options=options, executable_path=r"\chromedriver.exe")
except Exception as e:
    print(f"fail load default driver: {e}")

# load driver version from preferences
preferences = Preferences()
driver_version = preferences.get("driver_version", "124.0.6367.91")

if not driver:
    # selenium 4
    try:
        driver = webdriver.Chrome(
            service=ChromiumService(
                ChromeDriverManager(
                    chrome_type=ChromeType.CHROMIUM, driver_version=driver_version
                ).install()
            )
        )
    except Exception as e:
        version_match = re.search(r"(\d+\.\d+\.\d+\.\d+)", str(e))
        if version_match:
            version_number = version_match.group(1)
            print(
                f"Chrome version {version_number}, update driver version. Please relaunch this script."
            )
            # set new driver version
            preferences.set("driver_version", version_number)
        else:
            print(f"fail load driver selenium 4: {e}")

fingerprint: Dict[str, Any] = read_json_file("data/fingerprint1.json")
webgl_data = fingerprint.get("webgl_properties", {})
audio_properties = fingerprint.get("audio_properties", {})


if driver:
    try:
        stealth2(
            driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_data=webgl_data,
            user_agent=fingerprint.get("ua"),
            # audio_properties=audio_properties
        )

        # url = "https://bot.sannysoft.com/"
        # url = "https://sh.webmanajemen.com/webgl-information/"
        # url = "https://pixelscan.net/"
        # url = "https://webglreport.com/"
        # url = "https://privacycheck.sec.lrz.de/active/fp_wg/fp_webgl.html"
        url = "https://abrahamjuliot.github.io/creepjs/"
        driver.get(url)

        time.sleep(3)

        validate_fingerprint(driver, fingerprint)

        # time.sleep(60)  # wait before quit
        # driver.quit()
    except Exception as e:
        print(f"Browser error {e}")
        traceback.print_exc()
