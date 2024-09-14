import base64
import json
import math
import os
from pathlib import Path
import re
import time
import traceback
from typing import Any, Dict, Union

from selenium import webdriver
from selenium.webdriver import Chrome as WebDriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

from selenium_stealth.audio_properties import audio_properties_override
from selenium_stealth.chrome_app import chrome_app
from selenium_stealth.chrome_runtime import chrome_runtime
from selenium_stealth.hairline_fix import hairline_fix
from selenium_stealth.iframe_content_window import iframe_content_window
from selenium_stealth.media_codecs import media_codecs
from selenium_stealth.navigator_languages import navigator_languages
from selenium_stealth.navigator_permissions import (
    navigator_permissions,
    navigator_permissions2,
)
from selenium_stealth.navigator_plugins import navigator_plugins
from selenium_stealth.navigator_vendor import navigator_vendor
from selenium_stealth.navigator_webdriver import navigator_webdriver
from selenium_stealth.preferences import Preferences
from selenium_stealth.main import stealth2
from selenium_stealth.ansi import AnsiFormatter
from selenium_stealth.debug_utils import get_driver_webgl_info
from selenium_stealth.user_agent_override import user_agent_override
from selenium_stealth.utils import read_json_file, with_utils, with_utils2
from selenium_stealth.webgl_vendor import webgl_vendor_override
from selenium_stealth.window_outerdimensions import window_outerdimensions
from selenium_stealth.wrapper import evaluateOnNewDocument

current_dir = os.path.dirname(os.path.abspath(__file__))


# webdriver start

# load driver version from preferences
preferences = Preferences()
driver_version = preferences.get("driver_version", "124.0.6367.91")
fingerprint: Dict[str, Any] = read_json_file("data/fingerprint1.json")
webgl_data = fingerprint.get("webgl_properties", {})
audio_properties = fingerprint.get("audio_properties", {})

userAgent = fingerprint.get("ua")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("start-maximized")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument(f"user-agent={userAgent}")
driver = None

if not driver:
    # selenium 4
    try:
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
    try:
        with_utils2(driver)
        chrome_app(driver)
        # chrome_runtime(driver, False)
        iframe_content_window(driver)
        # media_codecs(driver)
        navigator_languages(driver, fingerprint.get("lang"))
        # navigator_permissions2(driver)
        navigator_plugins(driver)
        # navigator_vendor(driver, "Google Inc.")
        navigator_webdriver(driver)
        window_outerdimensions(driver)
        user_agent_override(
            driver, fingerprint.get("ua"), fingerprint.get("lang"), "Win32", True
        )
        webgl_vendor_override(
            driver,
            webgl_vendor=webgl_data.get("unmaskedVendor").replace("'", r"\'"),
            renderer=webgl_data.get("unmaskedRenderer").replace("'", r"\'"),
        )
        hairline_fix(driver)

        # url = "https://bot.sannysoft.com/"
        # url = "https://sh.webmanajemen.com/webgl-information/"
        url = "https://pixelscan.net/"
        # url = "https://webglreport.com/"
        # url = "https://privacycheck.sec.lrz.de/active/fp_wg/fp_webgl.html"
        # url = "https://abrahamjuliot.github.io/creepjs/"
        driver.get(url)

        time.sleep(120)
    except Exception as e:
        print(e)
    finally:
        if driver:
            driver.close()
