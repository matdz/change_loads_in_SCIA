import re

node_scia = 'N216'

# Assign a variable to the files name
file_name = "data_2.txt"
input_file = 'data.txt'
output_file = 'data_3.txt'

# Initialize a list to store modified lines
modified_lines = []

# Read the contents of the file and modify the lines
with open(file_name, 'r') as file:
    for line in file:
        # Replace comma with a point
        line = line.replace(',', '.')
        # Append the modified line to the list
        modified_lines.append(line.strip())

# Write the modified lines back to the file
with open(file_name, 'w') as file:
    for line in modified_lines:
        file.write(line + '\n')


# Specify the file names

# Read the content of the input file
with open(input_file, 'r') as input_file_handle:
    content = input_file_handle.read()

# Write the content to the output file
with open(output_file, 'w') as output_file_handle:
    output_file_handle.write(content)

# Copy the data.txt to the data_3.txt
print(f"File '{input_file}' copied to '{output_file}' successfully.")


with open(output_file, 'r') as file:
    # Read all lines into a list
    lines = file.readlines()


# Find the content of line number 10
line_number_10 = lines[9].strip()  # Indexing starts from 0, so line number 10 corresponds to index 9

# Find the content of line number 10 + 10
line_number_20 = lines[19].strip()  # Indexing starts from 0, so line number 20 corresponds to index 19

# Print the contents
print("Line 10:", line_number_10)
print("Line 20:", line_number_20)


# Read data_2.txt, the file that contains the numbers to replace
with open(file_name, 'r') as file:
    # Read all lines into a list
    lines_f2 = file.readlines()
print(lines_f2)
matrix = []
for line_f2 in lines_f2:
    parts = line_f2.strip().split(';')  # strip to remove leading/trailing whitespaces and split by ';'
    print(parts)
    matrix.append(parts)

def replace_text(input_array):
    with open(output_file, 'r+') as file:
        lines = file.readlines()
        line_number = 0
        for line in lines:
            if "\"" + node_scia + "\"" in line:   # Find the node
                if "\"" + input_array[3] + "\"" in lines[line_number + 4].strip() and "\"" + input_array[3] + "\"" == "\"Force\"": # Force or Moment
                    if "\"" + input_array[0] + "\"" in lines[line_number - 10].strip():  # for example BG7
                        if input_array[1] in lines[line_number + 3].strip():  # X, Y or Z
                            match = re.search(r'v=\"(.*?)\"', lines[line_number + 5].strip())
                            if match:
                                value = match.group(1)
                                print("Extracted value: ", value, " -> ", str(input_array[2]), " -> ", line_number + 5 + 1)
                                new_text = lines[line_number + 5].replace(str(value), str(input_array[2]))
                                lines[line_number + 5] = new_text
                            else:
                                print("No value found in the given text.")
                if "\"" + input_array[3] + "\"" in lines[line_number + 7].strip() and "\"" + input_array[3] + "\"" == "\"Moment\"": # Force or Moment
                    if "\"" + input_array[0] + "\"" in lines[line_number + 3].strip():  # for example BG7
                        if input_array[1] in lines[line_number + 6].strip():  # Mx, My or Mz
                            match = re.search(r'v=\"(.*?)\"', lines[line_number + 8].strip())
                            if match:
                                print(match.group(1))
                                value = match.group(1)
                                print("Extracted value: ", value, " -> ", str(input_array[2]), " -> ", line_number + 8 + 1)
                                new_text = lines[line_number + 8].replace(str(value), str(input_array[2]))
                                lines[line_number + 8] = new_text
                            else:
                                print("No value found in the given text.")
            line_number += 1
        pass
    with open(output_file, "w") as file:
        for line in lines:
            file.write(line)
    return new_text



for row in matrix:
    print('Processing ', row)
    input_array = row
    output_array = replace_text(input_array)
    print("Extracted elements:", output_array)  # Output: ['a', 'd', 'f']

