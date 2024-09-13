from pathlib import Path
from typing import Optional
from .wrapper import evaluateOnNewDocument
from selenium.webdriver import Chrome as Driver


def audio_properties_override(driver: Driver, data, **kwargs) -> None:
    evaluateOnNewDocument(
        driver,
        Path(__file__).parent.joinpath("js/audio.properties.js").read_text(),
        data,
    )
