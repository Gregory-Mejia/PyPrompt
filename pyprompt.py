"""

    Date: 4/17/2025
    Purpose:
    Create a simple reusable function that allows for safe user console
    prompting for Python.

"""

# -- Import Typing Lib -- #

from typing import TypeVar

# -- Variables -- #

T = TypeVar("type")  # For the parameter type definition and return-type

# -- Functions -- #


def prompt_console(text: str, _type: T, tries: int = -1) -> T:
    """
        This function attempts to resolve the user's input to the type provided
        Takes in 'text' as a string and '_type' as a type and returns said type
        Also takes in optional parameter 'tries' as an int

        'text' is used to prompt the user
        '_type' is used to continuously check for the required input
        'tries' is the total amount of tries the user gets for input
            - If over 0, it will assume that there a limited amount of tries
            - If 0, only one attempt will be made
            - If less than 0, infinite attempts will be made
    """

    # Get the input from the user
    u_inp: str = input(text)
    # Lower the string for use in the following if statements
    l_inp: str = u_inp.lower()

    # Check for exit conditions from the user's input
    if ((l_inp == "exit") or (l_inp == "terminate")):
        print("Exitting user input prompt.")
        return None

    # Exception block to try and resolve the type
    try:
        # Check to handle the special case for boolean type resolving
        if (_type == bool):

            # Use a long if statement to check if it's any variant of true
            if ((l_inp == "true") or (l_inp == "yes") or (l_inp == "y")):
                return True
            # Check for some variants of the false boolean variants
            elif ((l_inp == "false") or (l_inp == "no") or (l_inp == "n")):
                return False
            # Default to a reprompt for invalid input
            else:
                print(f"Invalid input for type: {_type}")
                if (tries > 0):   # Check for the amount of attempts
                    # Increment attempts down and print feedback
                    tries -= 1
                    print(f"You have {tries} attempts left.")
                elif (tries < 0):  # Check for if there are infinite attempts
                    # Output to signify that the user try again
                    print("Please try again.")
                else:  # Assume that 0 is when there are no more attempts left
                    print("No more attempts will be made.")
                    return None  # Return nothing if no input is given

                # Do a recursive call-back for reprompting
                # This will not be called because the stopping points
                # already resolve this issue by returning early.
                return prompt_console(text=text, _type=_type, tries=tries)
        else:
            # Otherwise, return the type given
            # This will cause an exception if it cannot convert
            u_inp: T = _type(u_inp)
            return u_inp
    except ValueError as ve:
        # Handle the ValueError gracefully
        print(f"A ValueError occured with the user's input: {ve}")
    except Exception as e:
        # Handle other exceptions
        print(f"An unknown exception occured: {e}")


def prompt_list(text: str, len: int, _type: T) -> list[T]:
    print(text)
    store_list = []
    if (len > 0):
        index: int
        for index in range(0, len, 1):
            store_list.append(
                prompt_console()
            )


prompt_list("ioaf", 3, bool)
