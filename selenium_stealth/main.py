import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from selenium.webdriver import Chrome as Driver

from .audio_properties import audio_properties_override
from .chrome_app import chrome_app
from .chrome_runtime import chrome_runtime
from .hairline_fix import hairline_fix
from .iframe_content_window import iframe_content_window
from .media_codecs import media_codecs
from .navigator_languages import navigator_languages
from .navigator_permissions import navigator_permissions
from .navigator_plugins import navigator_plugins
from .navigator_vendor import navigator_vendor
from .navigator_webdriver import navigator_webdriver
from .user_agent_override import user_agent_override
from .utils import with_utils
from .webgl_vendor import webgl_vendor_override
from .window_outerdimensions import window_outerdimensions
from .wrapper import evaluateOnNewDocument


def stealth(
    driver: Optional[Driver],
    user_agent: Optional[str] = None,
    languages: List[str] = ["en-US", "en"],
    vendor: str = "Google Inc.",
    platform: Optional[str] = None,
    webgl_vendor: str = "Intel Inc.",
    renderer: str = "Intel Iris OpenGL Engine",
    fix_hairline: bool = False,
    run_on_insecure_origins: bool = False,
    webgl_version: str = "WebGL 1.0",
    shading_language: str = "WebGL GLSL ES 1.0",
    **kwargs,
) -> None:
    """
    If user_agent = None then selenium-stealth only remove the 'headless' from userAgent
        Here is an example of args:
            user_agent: str = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36',
            languages: [str] = ["en-US", "en"],
            vendor: str = "Google Inc.",
            platform: str = "Win32",
            webgl_vendor: str = "Intel Inc.",
            renderer: str = "Intel Iris OpenGL Engine",
            fix_hairline: bool = False,
            run_on_insecure_origins: bool = False,
    """
    if not isinstance(driver, Driver):
        raise ValueError(
            "driver must is selenium.webdriver.Chrome, currently this lib only support Chrome"
        )

    ua_languages = ",".join(languages)

    with_utils(driver, **kwargs)
    chrome_app(driver, **kwargs)
    chrome_runtime(driver, run_on_insecure_origins, **kwargs)
    iframe_content_window(driver, **kwargs)
    media_codecs(driver, **kwargs)
    navigator_languages(driver, languages, **kwargs)
    navigator_permissions(driver, **kwargs)
    navigator_plugins(driver, **kwargs)
    navigator_vendor(driver, vendor, **kwargs)
    navigator_webdriver(driver, **kwargs)
    user_agent_override(driver, user_agent, ua_languages, platform, **kwargs)
    webgl_vendor_override(
        driver, webgl_vendor, renderer, shading_language, webgl_version, **kwargs
    )
    window_outerdimensions(driver, **kwargs)

    if fix_hairline:
        hairline_fix(driver, **kwargs)


import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from selenium.webdriver.chrome.webdriver import WebDriver as Driver


def stealth2(
    driver: Optional[Driver],
    user_agent: Optional[str] = None,
    languages: Optional[List[str]] = None,
    vendor: Optional[str] = None,
    platform: Optional[str] = None,
    fix_hairline: bool = False,
    run_on_insecure_origins: bool = False,
    webgl_data: Dict[str, Any] = {},
    audio_properties: Optional[Dict[str, Any]] = None,
    **kwargs,
) -> None:
    """
    Configures various stealth techniques for a Selenium WebDriver instance to evade detection.

    Args:
        driver (Optional[Driver]): Selenium WebDriver instance. Only Chrome is supported.
        user_agent (Optional[str]): Custom user agent string. If None, 'headless' is removed from the default user agent.
        languages (Optional[List[str]]): List of accepted languages, e.g., ["en-US", "en"].
        vendor (Optional[str]): The vendor for the navigator object, e.g., "Google Inc.".
        platform (Optional[str]): The platform string, e.g., "Win32".
        fix_hairline (bool): Whether to fix thin hairline rendering issues in headless mode.
        run_on_insecure_origins (bool): Whether to run on insecure origins.
        webgl_data (Dict[str, Any]): Data to spoof WebGL rendering information.
        **kwargs: Additional arguments for further customization.

    WebGL data example see https://github.com/dimaslanjaka/selenium-stealth/blob/48dcd6c85e10109b2d5ebcc82ebbea6b78815ea5/data/fingerprint1.json#L88

    Raises:
        ValueError: If the provided driver is not an instance of selenium.webdriver.Chrome.

    Example usage:
        stealth2(driver, user_agent="Mozilla/5.0...", languages=["en-US", "en"], vendor="Google Inc.")
    """

    if not isinstance(driver, Driver):
        raise ValueError(
            "driver must be selenium.webdriver.Chrome. Currently, this library only supports Chrome."
        )

    # Handle languages input as a string or list
    ua_languages = None
    if isinstance(languages, list):
        ua_languages = ",".join(languages)
    elif isinstance(languages, str):
        ua_languages = languages  # e.g., "en-US,en;q=0.5"

    # Apply various stealth methods to evade detection
    with_utils(driver, **kwargs)
    chrome_app(driver, **kwargs)
    chrome_runtime(driver, run_on_insecure_origins, **kwargs)
    iframe_content_window(driver, **kwargs)
    media_codecs(driver, **kwargs)

    # Set language overrides if specified
    if languages:
        navigator_languages(driver, languages, **kwargs)

    navigator_permissions(driver, **kwargs)
    navigator_plugins(driver, **kwargs)

    # Set vendor if provided
    if vendor:
        navigator_vendor(driver, vendor, **kwargs)

    navigator_webdriver(driver, **kwargs)

    # Override the user agent if all necessary parameters are provided
    if user_agent and ua_languages and platform:
        user_agent_override(driver, user_agent, ua_languages, platform, **kwargs)

    # Inject WebGL spoofing script if webgl_data is provided
    if webgl_data:
        js_code = Path(__file__).parent.joinpath("js/webgl.vendor2.js").read_text()
        evaluateOnNewDocument(
            driver,
            js_code,
            json.dumps(webgl_data),
        )

    if isinstance(audio_properties, dict) and audio_properties:
        # Spoof audio properties
        audio_properties_override(driver, audio_properties)

    # Fix window dimensions to avoid detection
    window_outerdimensions(driver, **kwargs)

    # Optionally fix hairline rendering issues in headless mode
    if fix_hairline:
        hairline_fix(driver, **kwargs)
