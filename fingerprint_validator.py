from typing import Any, Dict

from selenium.webdriver import Chrome as WebDriver

from selenium_stealth.ansi import AnsiFormatter
from selenium_stealth.debug_utils import get_driver_webgl_info


def validate_fingerprint(driver: WebDriver, fingerprint: Dict[str, Any]):
    webgl_data = fingerprint.get("webgl_properties", {})

    browser_agent = driver.execute_script("return navigator.userAgent;")
    if browser_agent != fingerprint.get("ua"):
        raise ValueError(
            f"useragent data invalid should be {AnsiFormatter.green(fingerprint.get('ua'))} but got {AnsiFormatter.red(browser_agent)}"
        )

    webgl_getter_result = get_driver_webgl_info(driver)
    print(webgl_getter_result)
    if webgl_data:
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
