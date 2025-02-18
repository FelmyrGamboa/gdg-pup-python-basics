# Loops – For and While Assignment

# Part 1: 
# - Write a Python program that demonstrates the use of both `for` and `while` loops.
# - The program will have two main parts:
#   1.  **Iterating Through a List Using a `for` Loop**:
#       - Create a list of at least five of your favorite foods (e.g., `['pizza', 'sushi', 'pasta', 'tacos', 'ice cream']`).
#       - Use a `for` loop to iterate through the list and print each food item on a new line.
#   2.  **Countdown Using a `while` Loop**:
#       - Ask the user for a starting number (e.g., `10`).
#       - Use a `while` loop to count down from the starting number to `1`, printing each number.
#       - After reaching `1`, print `"Countdown complete!"`.

# No. 1
# created a list of my favorite foods 
fav_foods = ['ice cream', 'chocolate', 'boiled egg', 'sushi', 'cake', 'fried chicken']

# made a print statement here to make it more organized and aesthetic
print("My Favorite Foods: ")
# enumerated the listed foods in the assigned variable fav_foods then iterated them using for loop
for idx, foods in enumerate(fav_foods):
    print(f'    {idx+1}. {foods}')

# No. 2
try:
    # ask user for a reference number 
    countdown_input = int(input("\nPlease enter your desired starting number for countdown: "))
    # raise an error if the entered input is non-numerical value

    # checks if the input is negative number
    if countdown_input <= 0:
        print("Invalid input: Please enter a positive number only or a number greater than 0.")
    
    # will approve every response if it is a positive number to initiate while loop
    elif countdown_input > 0:
        while countdown_input != 0:
            print(countdown_input)
            countdown_input -= 1
        print("Countdown complete!")

except ValueError:
    print(f"Invalid input: Please enter a valid number.")


# Part 2:
# - **For Loop Section**:
#   - Create a list of your favorite items (foods, movies, colors, etc.).
#   - Use a `for` loop to iterate through the list and print each item.
# - **While Loop Section**:
#   - Prompt the user to enter a positive integer as the starting number.
#   - Validate the input:
#     - If the input is not a valid positive integer, display: `"Invalid input: Please enter a number greater than zero."`
#     - If the input is valid, start the countdown.
#   - Use a `while` loop to count down from the starting number to `1`.
#   - Once the countdown reaches `1`, print `"Countdown complete!"`.

# created a list of my favorite items
fav_items = ['badminton', 'guitar', 'earphones', 'perfume', 'shirebound and busking', 'music']

# made a print statement to contain the iteration of my favorite things aesthetically
print("\nMy Favorite items: ")

# added a built-in function enumerate to iterate the list with numbers to make it better visually.
for idx, items in enumerate(fav_items):
    print(f"    {idx+1}. {items}")

# try syntax to detect all possible errors that may rise
try:
    # created a user input for starting number
    start_num = int(input("\nPlease enter a positive number as starting number: "))

    # checks if the the input is a positive number
    if start_num < 0:
        print("Invalid input: Please enter a number greater than zero.")
    
    # initiates the while loop if the input has been verified
    else:
        while start_num > 0:
            print(start_num)
            start_num -= 1
        
        # print statement after the while loop is finished
        print("Countdown complete!")

# except syntax that will catch potential error in the user input
except ValueError:
    print("Invalid input: Please enter a positive integer.")

# Sample Code
# # Part 1: For Loop - Printing a list of favorite foods
# # Let's create a list of some favorite foods
# favorite_foods = ['Pizza', 'Burger', 'Ice Cream', 'Pasta', 'Sushi']

# # Using a for loop to print each food in the list
# print("Here are my favorite foods:")
# for food in favorite_foods:
#     print(f"- {food}")  # Print each food item with a bullet point

# print("\n")  # Add a blank line to separate the outputs of the two parts

# Part 2: While Loop - Countdown from a number
# Ask the user to enter a starting number for the countdown
# try:
#     starting_number = int(input("Enter a positive number to start the countdown: "))

#     # Check if the number is positive
#     if starting_number <= 0:
#         print("Invalid input: Please enter a number greater than zero.")
#     else:
#         print("Countdown:")
#         # Use a while loop to count down from the starting number to 1
#         while starting_number > 0:
#             print(starting_number)  # Print the current number
#             starting_number -= 1   # Reduce the number by 1 for the next step

#         print("Countdown complete!")  # Message when the countdown ends

# # Handle invalid inputs (e.g., if the user enters a non-number)
# except ValueError:
#     print("Invalid input: Please enter a valid number.")
