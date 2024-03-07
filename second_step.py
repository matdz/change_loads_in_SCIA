import re

node_scia = 'N685'

# Open the file data_2.txt
file_name = "data_2.txt"

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
input_file = "data.txt"
output_file = "data_3.txt"

# Read the content of the input file
with open(input_file, 'r') as input_file_handle:
    content = input_file_handle.read()

# Write the content to the output file
with open(output_file, 'w') as output_file_handle:
    output_file_handle.write(content)

# Copy the data.txt to the data_3.txt
print(f"File '{input_file}' copied to '{output_file}' successfully.")


with open('data_3.txt', 'r') as file:
    # Read all lines into a list
    lines = file.readlines()

line_number = 0
for line in lines:
    if "\""+node_scia+"\"" in line:
        #print(line_number)  # Return line number on first match
        if "Force" in lines[line_number+4].strip():
            if "\"BG7\"" in lines[line_number-10].strip():
                if "X" in lines[line_number+3].strip():
                    #print(f"Value containing 'BG7' found on line: {line_number}")
                    #print(lines[line_number].strip())
                    #print('Force')
                    #print('X')
                    #print('Value to replace: '+ lines[line_number+5].strip())
                    match = re.search(r'v="(-?\d+)"', lines[line_number+5].strip())
                    if match:
                        value = int(match.group(1))
                        print("Extracted value: ", value, " -> ", line_number+5+1)
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


# Read data_2.txt, the file that contains the numbers to replace
with open('data_2.txt', 'r') as file:
    # Read all lines into a list
    lines_f2 = file.readlines()
print(lines_f2[0])


parts = lines_f2[2].split(";")
parts[-1] = parts[-1].strip()

print(parts)
print('------------------------------')

with open('data_3.txt', 'r+') as file:
    lines = file.readlines()
    line_number = 0
    for line in lines:
        if "\"" + node_scia + "\"" in line:
            if "Force" in lines[line_number + 4].strip():
                if "\"" + parts[0] + "\"" in lines[line_number - 10].strip():
                    if parts[1] in lines[line_number + 3].strip():
                        match = re.search(r'v="(-?\d+)"', lines[line_number + 5].strip())
                        if match:
                            value = int(match.group(1))
                            print("Extracted value: ", value, " -> ", line_number + 5 + 1)
                            new_text = lines[line_number + 5].replace(str(value), str(parts[2]))
                            print(new_text)
                            lines[line_number + 5] = new_text
                            #file.write(new_text)  # Write the modified line back to the file
                            print('done')
                        else:
                            print("No value found in the given text.")
                        print(lines[line_number + 5])
        line_number += 1
    pass


with open("data_3.txt", "w") as file:
    for line in lines:
        file.write(line)
