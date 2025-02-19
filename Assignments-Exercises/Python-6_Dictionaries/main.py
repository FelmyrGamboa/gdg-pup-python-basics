# ### **Instructions**

# 1. **Program Goal**:
#    - Write a Python program that creates a dictionary and performs the following operations:
#      - Add a new key-value pair using the dictionary's assignment syntax.
#      - Update the value of an existing key.
#      - Remove a key-value pair using the `del` statement or the `pop()` method.
# 2. **Steps**:
#    - **Step 1**: Create a dictionary with at least two key-value pairs and print it.
#      - Example dictionary: `{'name': 'Sparky', 'age': 25}`.
#    - **Step 2**: Add a new key-value pair to the dictionary.
#      - Add a `city` key with a value of `'New York'` and print the updated dictionary.
#    - **Step 3**: Update an existing key-value pair.
#      - Update the `age` key to `26` and print the updated dictionary.
#    - **Step 4**: Remove a key-value pair.
#      - Remove the `age` key and print the updated dictionary.

# created a dictionary
bini_dict = {'name' : 'Maloi', 'age' : 22, 'color' : 'dilaw', 'role' : 'main vocalist'}
print(f"Original dictionary: {bini_dict}")

# added a new key-value pair in the dictionary
bini_dict['city'] = 'New York'
print(f"Dictionary after adding an item: {bini_dict}")

# updated an existing key-value pair
bini_dict['name'] = 'Mary Loi Yves'
print(f"Dictionary after updating an item: {bini_dict}")

# removed a key-value pair
bini_dict.pop('city')
print(f"Dictionary after removing an item: {bini_dict}")

# sample
# # Step 1: Create a dictionary
# my_dict = {'name': 'Sparky', 'age': 25}
# print("Original dictionary:", my_dict)

# # Step 2: Add a new key-value pair
# my_dict['city'] = 'New York'
# print("Dictionary after adding an item:", my_dict)

# # Step 3: Update an existing key-value pair
# my_dict['age'] = 26
# print("Dictionary after updating an item:", my_dict)

# # Step 4: Remove a key-value pair
# del my_dict['age']
# print("Dictionary after removing an item:", my_dict)