# ### **Instructions**

# 1. **Program Goal**:
#    - Write a Python program that creates a list of integers.
#    - You will:
#      - Access elements by their index.
#      - Add an element to the list using the `append()` method.
#      - Remove an element from the list using the `remove()` method.
#      - Sort the list in ascending order using the `sort()` method.
# 2. **Steps**:
#    - **Step 1**: Create a list of integers and print it to the screen.
#      - Example list: `[5, 3, 8, 1]`.
#    - **Step 2**: Add an integer (for example, `6`) to the list and print the updated list.
#      - Use `list.append()` to add the element.
#    - **Step 3**: Remove the first occurrence of an element (for example, `8`) from the list and print the updated list.
#      - Use `list.remove()`.
#    - **Step 4**: Sort the list in ascending order using `list.sort()` and print the sorted list.
# 3. **Test the Program**:
#    - Try different numbers in the list and test your program to ensure each operation works correctly.
# 4. **Before Reviewing the Provided File**:
#    - Try implementing the assignment on your own first.
#    - Use the provided file (`main.py`) only as a reference after you’ve attempted your own solution.


# created a list of integers
int_list = [34, 5, 6, 7, 90, 99, 10000, 21, 23, 28]
print(f"Original list: {int_list}")

# added an element to the list 
int_list.append(12233)
print(f"List after adding an element {int_list}")

# removed an element from the list
int_list.remove(10000)
print(f"List after removing an element {int_list}")

# sorted the list in ascending order
print(f"List after sorting: {sorted(int_list)}")

# sample code
# # Step 1: Create a list of integers
# my_list = [5, 3, 8, 1]
# print("Original list:", my_list)

# # Step 2: Add an element to the list
# my_list.append(6)
# print("List after adding an element:", my_list)

# # Step 3: Remove an element from the list
# my_list.remove(8)
# print("List after removing an element:", my_list)

# # Step 4: Sort the list in ascending order
# my_list.sort()
# print("List after sorting:", my_list)


