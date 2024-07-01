#### Task ####
# Description: Write a Python script that handles exceptions during file 
# operations like reading from a non-existent file or writing to a read-only file.

# Task: Try to read from a file non_existent.txt and handle the FileNotFoundError. 
# Also, try to write to a file read_only.txt and handle the PermissionError.
def handle_file_operations():
    """Function to handle file operations and handle 
    exceptions through try-except block"""
    try:
        # reading from a non-existent file
        with open('non_existent.txt', 'r') as file:
            file.read()
        print("Successfully read from non_existent.txt")
    except FileNotFoundError:
        print("Error: The file 'non_existent.txt' does not exist.")

    try:
        # writing to a read-only file
        with open('read_only.txt', 'w') as file:
            file.write("Trying to write to a read-only file.")
        print("Successfully wrote to read_only.txt")
    except PermissionError:
        print("Error: You do not have permission to write to 'read_only.txt'.")

# Call the function to handle file operations
handle_file_operations()