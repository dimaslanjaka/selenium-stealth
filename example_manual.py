import base64
import math
import os
import re
import time
import traceback
from typing import Any, Dict

from selenium import webdriver
from selenium.webdriver import Chrome as WebDriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

from selenium_stealth.audio_properties import audio_properties_override
from selenium_stealth.preferences import Preferences
from selenium_stealth.main import stealth2
from selenium_stealth.ansi import AnsiFormatter
from selenium_stealth.debug_utils import get_driver_webgl_info
from selenium_stealth.user_agent_override import user_agent_override
from selenium_stealth.utils import read_json_file

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
fingerprint: Dict[str, Any] = read_json_file("data/fingerprint1.json")
webgl_data = fingerprint.get("webgl_properties", {})
audio_properties = fingerprint.get("audio_properties", {})

if not driver:
    # selenium 4
    try:
        userAgent = fingerprint.get("ua")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f"user-agent={userAgent}")
        driver = webdriver.Chrome(
            options=chrome_options,
            service=ChromiumService(
                ChromeDriverManager(
                    chrome_type=ChromeType.CHROMIUM, driver_version=driver_version
                ).install()
            ),
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

if driver:
    user_agent_override(
        driver, fingerprint.get("ua"), fingerprint.get("lang"), "Win32", True
    )
    # url = "https://bot.sannysoft.com/"
    # url = "https://sh.webmanajemen.com/webgl-information/"
    # url = "https://pixelscan.net/"
    # url = "https://webglreport.com/"
    # url = "https://privacycheck.sec.lrz.de/active/fp_wg/fp_webgl.html"
    url = "https://abrahamjuliot.github.io/creepjs/"
    driver.get(url)

    time.sleep(30)
    driver.quit()
