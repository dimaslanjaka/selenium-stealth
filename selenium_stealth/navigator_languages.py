from pathlib import Path
from typing import List, Union
from .wrapper import evaluateOnNewDocument
from selenium.webdriver import Chrome as Driver


def navigator_languages(
    driver: Driver, languages: Union[str, List[str]], **kwargs
) -> None:
    languages_list = []
    if isinstance(languages, str):
        # sample full string en-US,en;q=0.9
        strip_semicolon = languages.split(";")[0]  # en-US,en
        split_comma = strip_semicolon.split(",")
        languages_list = split_comma
    else:
        languages_list = languages
    evaluateOnNewDocument(
        driver,
        Path(__file__).parent.joinpath("js/navigator.languages.js").read_text(),
        languages_list,
    )
