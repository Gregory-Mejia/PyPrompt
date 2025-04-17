"""

    Date: 4/17/2025
    Purpose:
    Create a library that allows for safe user console prompting.

"""

# -- Import Typing Lib -- #

from typing import TypeVar

# -- Variables -- #

T = TypeVar("type")  # For the parameter type definition and return-type

# -- Functions -- #


def prompt_console(text: str, _type: T) -> T:
    pass
