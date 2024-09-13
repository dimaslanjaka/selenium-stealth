from pathlib import Path
from typing import Optional
from .wrapper import evaluateOnNewDocument
from selenium.webdriver import Chrome as Driver


def webgl_vendor_override(
    driver: Driver,
    webgl_vendor: Optional[str],
    renderer: Optional[str],
    shadingLanguage: Optional[str],
    version: Optional[str],
    **kwargs
) -> None:
    evaluateOnNewDocument(
        driver,
        Path(__file__).parent.joinpath("js/webgl.vendor.js").read_text(),
        webgl_vendor,
        renderer,
        shadingLanguage,
        version,
    )
