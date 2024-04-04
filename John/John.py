def greet(name):
    if name.lower() == "john":
        print("Hello, John")
    else:
        print("There is no such name")

# Taking input from the user
user_input = input("Enter a name: ")

# Greeting the user based on the input
greet(user_input)
