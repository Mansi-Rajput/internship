def capitalize_file(input_file, output_file):
 try:
    # Open the input file for reading
    with open(input_file, 'r') as in_file:
      # it Reads  the entire file content
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
