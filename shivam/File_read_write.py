def capitalize_file(input_file, output_file):
  """
  This function reads a text file, capitalizes every word, and writes the modified content to a new file.

  Args:
    input_file (str): The path to the input text file.
    output_file (str): The path to the output text file where capitalized content will be written.
  """
  try:
    # Open the input file for reading
    with open(input_file, 'r') as in_file:
      # Read the entire file content
      text = in_file.read()

    # Capitalize each word using list comprehension
    capitalized_text = " ".join([word.capitalize() for word in text.split()])

    # Open the output file for writing
    with open(output_file, 'w') as out_file:
      # Write the capitalized text to the output file
      out_file.write(capitalized_text)

    print(f"Successfully capitalized text and wrote to {output_file}")
  except FileNotFoundError:
    print(f"Error: Input file {input_file} not found.")

# Specify the input and output file paths
input_file = "input.txt"
output_file = "output.txt"

capitalize_file(input_file, output_file)
