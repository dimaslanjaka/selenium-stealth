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


def validate_fingerprint(driver: WebDriver):
    browser_agent = driver.execute_script("return navigator.userAgent;")
    if browser_agent != fingerprint.get("ua"):
        raise ValueError(
            f"useragent data invalid should be {AnsiFormatter.green(fingerprint.get('ua'))} but got {AnsiFormatter.red(browser_agent)}"
        )

    webgl_getter_result = get_driver_webgl_info(driver)
    print(webgl_getter_result)
    if webgl_getter_result.get("SHADING_LANGUAGE_VERSION") != webgl_data.get(
        "shadingLanguage"
    ):
        raise ValueError(
            f"shadingLanguage missmatch, value should be {AnsiFormatter.green(webgl_data.get('shadingLanguage'))} but got {AnsiFormatter.red(webgl_getter_result('SHADING_LANGUAGE_VERSION'))}"
        )
    if webgl_getter_result.get("RENDERER") != webgl_data.get("renderer"):
        raise ValueError(
            f"shadingLanguage missmatch, value should be {AnsiFormatter.green(webgl_data.get('renderer'))} but got {AnsiFormatter.red(webgl_getter_result('RENDERER'))}"
        )
    if webgl_getter_result.get("VENDOR") != webgl_data.get("vendor"):
        raise ValueError(
            f"vendor missmatch, value should be {AnsiFormatter.green(webgl_data.get('vendor'))} but got {AnsiFormatter.red(webgl_getter_result('VENDOR'))}"
        )
    if webgl_getter_result.get("VERSION") != webgl_data.get("version"):
        raise ValueError(
            f"version missmatch, value should be {AnsiFormatter.green(webgl_data.get('version'))} but got {AnsiFormatter.red(webgl_getter_result('VERSION'))}"
        )


if driver:
    try:
        stealth2(
            driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_data=webgl_data,
            user_agent=fingerprint.get("ua"),
            audio_properties=fingerprint.get("audio_properties"),
        )

        # url = "https://bot.sannysoft.com/"
        # url = "https://sh.webmanajemen.com/webgl-information/"
        # url = "https://pixelscan.net/"
        # url = "https://webglreport.com/"
        url = "https://privacycheck.sec.lrz.de/active/fp_wg/fp_webgl.html"
        driver.get(url)

        time.sleep(3)

        validate_fingerprint(driver)

        time.sleep(30)  # wait before screenshoot

        # screenshoot
        metrics = driver.execute_cdp_cmd("Page.getLayoutMetrics", {})
        width = math.ceil(metrics["contentSize"]["width"])
        height = math.ceil(metrics["contentSize"]["height"])
        screenOrientation = dict(angle=0, type="portraitPrimary")
        driver.execute_cdp_cmd(
            "Emulation.setDeviceMetricsOverride",
            {
                "mobile": False,
                "width": width,
                "height": height,
                "deviceScaleFactor": 1,
                "screenOrientation": screenOrientation,
            },
        )
        clip = dict(x=0, y=0, width=width, height=height, scale=1)
        opt: Dict[str, Any] = {"format": "png"}
        if clip:
            opt["clip"] = clip

        result = driver.execute_cdp_cmd("Page.captureScreenshot", opt)
        buffer = base64.b64decode(result.get("data", b""))
        os.makedirs(os.path.join(current_dir, ".mypy_cache"), exist_ok=True)
        with open(
            os.path.join(
                current_dir, ".mypy_cache/selenium_chrome_headful_with_stealth.png"
            ),
            "wb",
        ) as f:
            f.write(buffer)

        driver.quit()
    except Exception as e:
        print(f"Browser error {e}")
        traceback.print_exc()
