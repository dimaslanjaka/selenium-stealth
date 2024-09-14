import base64
import json
import math
import os
import re
import time
import traceback
from typing import Any, Dict

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium_stealth import stealth, Preferences
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

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
    # selenium 3
    try:
        driver = webdriver.Chrome(
            ChromeDriverManager(
                chrome_type=ChromeType.CHROMIUM, driver_version=driver_version
            ).install()
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
            print(f"fail load driver selenium 3: {e}")

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

fingerprint = read_json_file("data/fingerprint1.json")
webgl_data = fingerprint.get("webgl_properties", {})

if driver:
    try:
        stealth(
            driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor=webgl_data.get("unmaskedVendor"),
            renderer=webgl_data.get("unmaskedRenderer"),
            fix_hairline=True,
            user_agent=fingerprint.get("ua"),
            shading_language=webgl_data.get("shadingLanguage"),
            webgl_version=webgl_data.get("version"),
        )

        print(driver.execute_script("return navigator.userAgent;"))
        # url = "https://bot.sannysoft.com/"
        # url = "https://sh.webmanajemen.com/webgl-information/"
        url = "https://abrahamjuliot.github.io/creepjs/"
        driver.get(url)

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
