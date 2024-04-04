
def check_number(num):
    try:
        num = int(num)
        if num > 7:
            print("Hello")
    except ValueError:
        print("Please enter a valid integer.")

# Continuously ask for input until user enters "exit"
while True:
    user_input = input("Enter a number (or 'exit' to stop): ")
    if user_input.lower() == 'exit':
        break
    else:
        check_number(user_input)

