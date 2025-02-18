#    Write a Python function `create_greeting(name)` that:

#    - Accepts one parameter: `name` (a string).
#    - Returns a greeting message in the format: `"Hello, <name>!, welcome to the GDG Web Development Team! You're doing great, and I truly believe that someday you'll be an amazing developer. Life may feel challenging right now, and programming can be overwhelming at times, but remember, all your hard work will pay off in the end. Keep pushing forward, you're on the right path!"`.

def create_greeting(name : str):
    return f"Hello, {name}!, welcome to the GDG Web Development Team! You're doing great, and I truly believe that someday you'll be an amazing developer. Life may feel challenging right now, and programming can be overwhelming at times, but remember, all your hard work will pay off in the end. Keep pushing forward, you're on the right path!"

try:
    user_name = input("Please enter your name: ")
    if user_name.strip():
        print(f"\nThe greeting message is: \n {create_greeting(user_name)}")
    else:
        raise ValueError

except ValueError:
    print("Invalid input: Please enter a valid name.")

# # Function to create a greeting message
# def create_greeting(name):
#     """
#     Create a personalized greeting message.
#     Parameters:
#         name (str): The name to include in the greeting.
#     Returns:
#         str: The greeting message.
#     """
#     return f"Hello {name}, welcome to the GDG Web Development Team! You're doing great, and I truly believe that someday you'll be an amazing developer. Life may feel challenging right now, and programming can be overwhelming at times, but remember, all your hard work will pay off in the end. Keep pushing forward, you're on the right path!"

# # Main program
# try:
#     # Get the user's name
#     name = input("Enter your name: ")

#     # Create and display the greeting message
#     greeting = create_greeting(name)
#     print(f"The greeting message is: {greeting}")

# except ValueError:
#     print("Invalid input: Please enter a valid name.")
