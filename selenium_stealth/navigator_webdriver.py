from pathlib import Path
from .wrapper import evaluateOnNewDocument
from selenium.webdriver import Chrome as Driver


def navigator_webdriver(driver: Driver, **kwargs) -> None:
    """Remove JS navigator.webdriver attribute"""
    evaluateOnNewDocument(
        driver, Path(__file__).parent.joinpath("js/navigator.webdriver.js").read_text()
    )
