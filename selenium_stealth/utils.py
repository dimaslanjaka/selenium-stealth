import json
from pathlib import Path
from typing import Optional

from selenium.webdriver import Chrome as Driver

from .wrapper import evaluateOnNewDocument


def read_json_file(file_path: Optional[str]):
    """
    Reads a JSON file and returns its contents.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict or list: The content of the JSON file as a Python dictionary or list.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file: {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def with_utils(driver: Driver, **kwargs) -> None:
    evaluateOnNewDocument(
        driver, Path(__file__).parent.joinpath("js/utils.js").read_text()
    )
