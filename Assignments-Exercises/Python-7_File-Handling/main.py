# ### **Instructions**

# 1. **Program Goal**:

#    - Write a Python program that:
#      - Reads the contents of a file and prints it to the console.
#      - Creates a new file and writes content to it.

# 2. **Steps**:

#    - **Step 1**: Create a file named `sample.txt` (or use any existing file you have) and add some text to it, such as:
#      ```
#      Hello, this is a test file.
#      Python file handling is easy and fun!
#      ```
#    - **Step 2**: In your Python program, use the `open()` function to open the file in read mode (`'r'`).
#      - Use the `read()` or `readlines()` method to read the contents of the file.
#      - Print the contents of the file to the console.
#    - **Step 3**: Create a new file named `newfile.txt` using the `open()` function in write mode (`'w'`).
#      - Write some content to the file using the `write()` method.
#      - Close the file after writing the content.
#    - **Step 4**: Optionally, read the contents of the newly created file to ensure that the content was written correctly.

# Step 1 & 2:
# try syntax to catch potential errors when opening and accessing the file
try:
    # stored the opened file into a variable
    file = open('./sample.txt', 'r')

    # printed a marker for the contents
    print("Contents of the sample.txt: \n")
    # used readlines and for loop to print the contents of the file
    for texts in file.readlines():
        print(texts)
    
    # close file to free memory
    file.close()

# handles and catches the error when file being opened is not found 
except FileNotFoundError:
    print("File not found.")

# Step 3:
# created a new file using new filename
new_file = open('./new_sample.txt', 'w')

# written some text on a file
new_file.write(
'''O Mga Awit ng Hiraya Para sa Guni-guning Sinta
    - The million little things I'll never tell you
    - About a million little things you and I feel
''')

# close file to free memory
new_file.close()

# Step 4: 
# opened the new file
new_file_sample = open('./new_sample.txt', 'r')

# printed a marker for the contents
print("\nContents of the new file: ")

# used for loops to read all contents
for lines in new_file_sample.readlines():
    print(lines)

# close file to free memory
new_file_sample.close()




# sample code
# Step 1: Read contents from a file
# try:
#     with open('sample.txt', 'r') as file:
#         contents = file.read()
#         print("Contents of the file:")
#         print(contents)
# except FileNotFoundError:
#     print("The file 'sample.txt' was not found.")

# # Step 2: Write to a new file
# with open('newfile.txt', 'w') as file:
#     file.write("This is a new file, like New Year New Me XD.\n")
#     print("\nNew file created with content:")

# # Step 3: Verify content in the new file by reading it
# with open('newfile.txt', 'r') as file:
#     newfile_contents = file.read()
#     print(newfile_contents)