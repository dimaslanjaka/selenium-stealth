class AnsiFormatter:
    """
    A helper class for formatting text with ANSI escape sequences.

    Supported formats:
    - Bold
    - Red
    - Green
    - Yellow
    - Orange (simulated with RGB)

    Methods:
    --------
    bold(text: str) -> str
        Returns the input text formatted in bold.

    red(text: str) -> str
        Returns the input text formatted in red.

    green(text: str) -> str
        Returns the input text formatted in green.

    yellow(text: str) -> str
        Returns the input text formatted in yellow.

    orange(text: str) -> str
        Returns the input text formatted in orange using RGB values.
    """

    # ANSI codes
    RESET = "\033[0m"
    BOLD = "\033[1m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    ORANGE = "\033[38;2;255;165;0m"  # RGB-based color for orange

    @staticmethod
    def bold(text: str) -> str:
        """Return the text formatted in bold."""
        return f"{AnsiFormatter.BOLD}{text}{AnsiFormatter.RESET}"

    @staticmethod
    def red(text: str) -> str:
        """Return the text formatted in red."""
        return f"{AnsiFormatter.RED}{text}{AnsiFormatter.RESET}"

    @staticmethod
    def green(text: str) -> str:
        """Return the text formatted in green."""
        return f"{AnsiFormatter.GREEN}{text}{AnsiFormatter.RESET}"

    @staticmethod
    def yellow(text: str) -> str:
        """Return the text formatted in yellow."""
        return f"{AnsiFormatter.YELLOW}{text}{AnsiFormatter.RESET}"

    @staticmethod
    def orange(text: str) -> str:
        """Return the text formatted in orange (simulated with RGB)."""
        return f"{AnsiFormatter.ORANGE}{text}{AnsiFormatter.RESET}"


# Example usage:
if __name__ == "__main__":
    print(AnsiFormatter.bold("This is bold text"))
    print(AnsiFormatter.red(AnsiFormatter.bold("This is bold red text")))
    print(AnsiFormatter.red("This is red text"))
    print(AnsiFormatter.green("This is green text"))
    print(AnsiFormatter.yellow("This is yellow text"))
    print(AnsiFormatter.orange("This is orange text"))
