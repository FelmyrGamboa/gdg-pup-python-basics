# A program that checks the age and categorizes into different age groups with exception handling for invalid inputs
#  - If the age is below 13, display: `"You are categorized as: Child"`
#  - If the age is between 13 and 19 (inclusive), display: `"You are categorized as: Teenager"`
#  - If the age is between 20 and 59 (inclusive), display: `"You are categorized as: Adult"`
#  - If the age is 60 or above, display: `"You are categorized as: Senior"`

# try syntax to handle all potential errors in the code
try:
    # ask the user a number then convert it into an integer
    age_input = int(input("Please enter your age: "))

    # check the number and determine the age group
    if age_input < 0:
        # this if statement will raise an error if they are n-egative numbers/integers
        raise ValueError("Age cannot be a negative number.")
    elif age_input < 13:
        print("You are categorized as: Child")
    elif 13 <= age_input <= 19:
        print("You are categorized as: Teenager")
    elif 20 <= age_input <= 59:
        print("You are categorized as: Adult")
    elif age_input >= 60:
        print("You are categorized as: Senior")
    else: 
        # else will raise an error if they are not categorized as an integer
        raise ValueError("Age cannot be a non-numeric value.")

# catch the potential errors that may rise in the categorization of the user input eg. non numerical values
except ValueError as e:
    print(f"Invalid input: {e}")






# Sample code
# # This program checks the age and categorizes the person into different age groups.
# # It also demonstrates exception handling using try and except.

# try:
#     # Input: Get age from the user
#     user_input = int(input("Please enter your age: "))

#     # Check the age category
#     if user_input < 0:
#         raise ValueError("Age cannot be negative.")
#     elif user_input < 13:
#         print("You are categorized as: Child")
#     elif user_input < 20:
#         print("You are categorized as: Teenager")
#     elif user_input < 60:
#         print("You are categorized as: Adult")
#     else:
#         print("You are categorized as: Senior")
        
# except ValueError:
#     print("Invalid input: Age cannot be a non-number.")
