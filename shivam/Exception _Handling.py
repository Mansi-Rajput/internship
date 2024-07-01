def handle_file_operations():
  
  try:
    # Attempt to read from a non-existent file
    with open("non_existent.txt", 'r') as in_file:
      print("Successfully read from non_existent.txt (This shouldn't be printed)")

  except FileNotFoundError:
    print("Expected Error: File 'non_existent.txt' not found.")

  try:
    # Attempt to write to a read-only file (assuming read_only.txt exists)
    with open("read_only.txt", 'w') as out_file:
      out_file.write("This will fail due to permission errors.")

  except Exception as e:
    print("Expected Caught:",e)

print("Script execution completed.")

handle_file_operations()
