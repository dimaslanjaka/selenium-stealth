import json
from pathlib import Path
from typing import Any, Optional, Union

from selenium.webdriver import Chrome as Driver

from .wrapper import evaluateOnNewDocument


def with_utils(driver: Driver, **kwargs) -> None:
    evaluateOnNewDocument(
        driver, Path(__file__).parent.joinpath("js/utils.js").read_text()
    )


def read_json_file(file_path: Optional[str]) -> Union[dict, list, None]:
    """
    Reads a JSON file and returns its contents.

    Args:
        file_path (Optional[str]): The path to the JSON file.

    Returns:
        Union[dict, list, None]: The content of the JSON file as a Python dictionary or list, or None if an error occurs.
    """
    if file_path is None:
        print("No file path provided.")
        return None

    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file: {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return None


def write_json_file(file_path: Optional[str], data: Any) -> None:
    """
    Writes data to a JSON file.

    Args:
        file_path (Optional[str]): The path to the JSON file.
        data (Any): The data to write to the JSON file.

    Returns:
        None
    """
    if file_path is None:
        print("No file path provided.")
        return

    try:
        with open(file_path, mode="w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error writing to file: {file_path}, {e}")
    except TypeError as e:
        print(f"Error serializing data to JSON: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
