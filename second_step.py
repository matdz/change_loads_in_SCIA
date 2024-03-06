import re


# Open the file data_2.txt
file_name = "data_2.txt"

# Read the contents of the file
with open(file_name, 'r') as file:
    # Read each line in the file
    for line in file:
        # Replace comma with a point
        line = line.replace(',', '.')
        # Replace semicolon with a comma
        line = line.replace(';', ',')
        # Print the modified line
        print(line.strip())

# Specify the file names
input_file = "data.txt"
output_file = "data_3.txt"

# Read the content of the input file
with open(input_file, 'r') as input_file_handle:
    content = input_file_handle.read()

# Write the content to the output file
with open(output_file, 'w') as output_file_handle:
    output_file_handle.write(content)

print(f"File '{input_file}' copied to '{output_file}' successfully.")

"""
with open("data_3.txt", "r") as file:
    # Legge ogni riga nel file
    for line_number, line in enumerate(file, start=1):
        # Controlla se la riga contiene "<obj id="
        if " n=\"BG7\"/>" in line:
            print(line_number)
            if " n=\"BG7\"/>" in line:
"""


with open('data_3.txt', 'r') as file:
    # Read all lines into a list
    lines = file.readlines()

#print(lines)
line_number = 0
for line in lines:
    if "N685" in line:
        #print(line_number)  # Return line number on first match
        if "Force" in lines[line_number+4].strip():
            if "BG7" in lines[line_number-10].strip():
                if "Y" in lines[line_number+3].strip():
                    #print(f"Value containing 'BG7' found on line: {line_number}")
                    #print(lines[line_number].strip())
                    #print('Force')
                    #print('X')
                    #print('Value to replace: '+ lines[line_number+5].strip())
                    match = re.search(r'v="(-?\d+)"', lines[line_number+5].strip())
                    if match:
                        value = int(match.group(1))
                        print("Extracted value:", value)
                    else:
                        print("No value found in the given text.")
    line_number += 1


# Find the content of line number 10
line_number_10 = lines[9].strip()  # Indexing starts from 0, so line number 10 corresponds to index 9

# Find the content of line number 10 + 10
line_number_20 = lines[19].strip()  # Indexing starts from 0, so line number 20 corresponds to index 19

# Print the contents
print("Line 10:", line_number_10)
print("Line 20:", line_number_20)