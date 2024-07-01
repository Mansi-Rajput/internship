#### Task ####
# Description: Create a Python script that reads a text file, manipulates its contents, and writes the modified content to a new file.
# Task: Read a text file input.txt, capitalize every word, and write the modified text to output.txt.

def capitalize_words_in_file(input_file, output_file):
    """Function to capitalize words in the file"""
    try:
        # to open the input file for reading 
        with open(input_file, 'r') as file:
            # reading content of the file
            content = file.read()
            print(content)

        # capitalizing every word in the file
        capitalized_content = content.title()

        # open the output file for write
        with open(output_file, 'w') as file:
            # writing the capitalized content in the output file
            written_content = file.write(capitalized_content)
            print(written_content)

        print(f"The contents of the {input_file} have been capitalized and written to {output_file}.")

    except FileNotFoundError:
        print(f"The file {input_file} does not exist")
    except Exception as e:
        print(f"An error occured: {e}")

# input and output file names 
input_file = 'input.txt'
output_file = 'output.txt'

# caliing the function to capitalize words in the file
capitalize_words_in_file(input_file, output_file)