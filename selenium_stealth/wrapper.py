import json
from typing import Any

from selenium.webdriver import Chrome as Driver


def evaluationString(fun: str, *args: Any) -> str:
    """Convert function and arguments to str."""
    _args = ", ".join([json.dumps("undefined" if arg is None else arg) for arg in args])
    expr = "(" + fun + ")(" + _args + ")"
    return expr


def evaluateOnNewDocument(driver: Driver, pagefunction: str, *args: Any) -> None:

    js_code = evaluationString(pagefunction, *args)

    driver.execute_cdp_cmd(
        "Page.addScriptToEvaluateOnNewDocument",
        {
            "source": js_code,
        },
    )
