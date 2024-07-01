#### Task ####
# Description: Read data from a CSV file, perform operations like filtering or aggregation, and write the processed data to a new CSV file.
# Task: Read data.csv, filter rows where column 'age' is greater than 30, and write the filtered data to filtered_data.csv.
import csv

def filter_data(input_file, output_file):
    """Function to filter data from input_file to output_file"""
    try:
        # for reading
        with open(input_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            
            # Getting the fieldnames from the input file
            fieldnames = reader.fieldnames
            
            # for writing
            with open(output_file, 'w', newline='') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                
                # Writing the header
                writer.writeheader()
                
                # Filtering rows where 'age' is greater than 30 and saving them to output_file
                for row in reader:
                    if int(row['age']) > 30:
                        writer.writerow(row)
        
        print(f"Filtered data has been written to {output_file}.")
    
    except FileNotFoundError:
        print(f"The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# input and output file names
input_file = 'data.csv'
output_file = 'filtered_data.csv'

# Calling the function
filter_data(input_file, output_file)