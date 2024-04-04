def check_number_and_greet(num):
    """
    Checks if the input number is greater than 7 and greets the user if it is.

    Args:
        num (str): The input number provided by the user.

    Returns:
        None
    """
    try:
        num = int(num)
        if num > 7:
            print("Hello")
    except ValueError:
        print("Please enter a valid integer.")


def get_user_input():
    """
    Retrieves user input.

    Returns:
        str: The user's input.
    """
    return input("Enter a number (or 'exit' to stop): ")


def main():
    """
    Main function to execute the program.
    """
    try:
        # Continuously ask for input until user enters "exit"
        while True:
            user_input = get_user_input()
            if user_input.lower() == 'exit':
                break
            else:
                check_number_and_greet(user_input)
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()
