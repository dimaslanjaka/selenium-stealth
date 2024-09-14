import json
from pathlib import Path
from typing import Any, Dict

from selenium.webdriver import Chrome as WebDriver


def get_driver_webgl_info(driver: WebDriver) -> Dict[str, Any]:
    webgl_getter = Path(__file__).parent.joinpath("js/webgl.debug.js").read_text()
    return json.loads(driver.execute_script(webgl_getter))
