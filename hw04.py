from typing import List, Tuple

def parse_input(user_input: str) -> Tuple[str, List[str]]:
    """Parses the user input and returns the command and arguments.

    Args:
        user_input (str): The user input to be parsed.

    Returns:
        tuple[str, list]: A tuple containing the command (str) and arguments (list).

    """
    if not user_input.split():
        return "Please enter a command:", []
    cmd, *args = user_input.split()

    return cmd, args


def input_error(func):
    """
    A decorator that handles common input errors and returns appropriate error messages.

    Args:
        func: The function to be decorated.

    Returns:
        The decorated function.

    Raises:
        KeyError: If a contact is not found.
        ValueError: If an invalid command usage is detected.
        IndexError: If insufficient arguments are provided for a command.
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid command usage."
        except IndexError:
            return "Invalid command usage. Insufficient arguments provided. Please provide all required information."
    return inner


@input_error
def add_contact(args, contacts) -> str:
    """Adds a new contact to the dictionary."""
    if len(args) != 2:
        raise ValueError
    name, phone = args
    if name in contacts:
        return "This contact already exists. Please use the change command to update the phone number."
    contacts[name] = phone
    return f"Contact {name} added with number {phone}."


@input_error
def change_contact(args, contacts) -> str:
    """Changes an existing contact's phone number."""
    if len(args) != 2:
        raise ValueError
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f"Contact {name} updated to new number {new_phone}."
    else:
        raise KeyError


@input_error
def show_phone(args, contacts) -> str:
    """Shows a contact's phone number."""
    if len(args) != 1:
        raise ValueError
    name = args[0]
    if name in contacts:
        return f"{name}'s number is {contacts[name]}"
    else:
        raise KeyError

@input_error
def show_all(contacts) -> str:
    """Displays all contacts."""
    if contacts:
        return '\n'.join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts saved."


def main():
    """
    The main function of the assistant bot program.
    
    This function initializes an empty dictionary to store contacts and then enters a loop to prompt the user for commands.
    The user can enter commands such as "hello", "add", "change", "phone", "all", "close", or "exit" to interact with the assistant bot.
    The function calls different helper functions based on the user's command and displays the corresponding output.
    The loop continues until the user enters "close" or "exit" to exit the program.
    """
    
    contacts = {}  # Dictionary to store contacts
    
    print("Welcome. I am an assistant bot!")

    # Main loop to interact with the user
    while True:  
        user_input = input("Enter a command: ").strip()  # Prompt the user for input
        
        if not user_input: # Check if the user entered an empty string
            print("Please enter a command.") 
            continue
        if user_input.lower() in ["close", "exit"]:  # Check if the user wants to exit
            print("Good bye!")
            break

        command, args = parse_input(user_input)

        # Helper functions to handle different commands
        def switch_commands(command):
            switcher = {
                "hello": "How can I help you?",
                "add": lambda: add_contact(args, contacts),
                "change": lambda: change_contact(args, contacts),
                "phone": lambda: show_phone(args, contacts),
                "all": lambda: show_all(contacts),
            }
            result = switcher.get(command, "Invalid command. Available commands: hello, add, change, phone, all, close, exit")
            return result() if callable(result) else result
        print(switch_commands(command))


if __name__ == "__main__":
    main()
