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
    """
        This function attempts to resolve the user's input to the type provided
        Takes in 'text' as a string and '_type' as a type and returns said type

        'text' is used to prompt the user
        '_type' is used to continuously check for the required input
    """

    # Get the input from the user
    u_inp = input(text)

    # Exception block to try and resolve the type
    try:
        # Check to handle the special case for boolean type resolving
        if (_type == bool):
            # Lower the string to not have to check for more cases
            u_inp = u_inp.lower()

            # Use a long if statement to check if it's any variant of true
            if ((u_inp == "true") or (u_inp == "yes") or (u_inp == "y")):
                return True
            # Check for all variants of the false boolean
            elif ((u_inp == "false") or (u_inp == "no") or (u_inp == "n")):
                return False
            # Default to a reprompt for invalid input
            else:
                # Do a recursive call-back for reprompting
                print(f"Invalid input for type: {_type}\nTry again.")
                return prompt_console(text=text, _type=_type)
        else:
            # Otherwise, return the type given
            u_inp = _type(u_inp)
            return u_inp
    except ValueError as ve:
        # Handle the ValueError gracefully
        print(f"A ValueError occured with the user's input: {ve}")
    except Exception as e:
        # Handle other exceptions
        print(f"An unknown exception occured: {e}")

    print(type(u_inp))
    print(u_inp)
