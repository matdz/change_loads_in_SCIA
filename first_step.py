import linecache
import csv

num_lines = []
my_array = []
file_csv = 'output.csv'
node_scia = 'N685'
first_file_txt = 'data.txt'

with open(first_file_txt, "r") as file:
    # Read every line in the file
    for line_number, line in enumerate(file, start=1):
        # Check if the line contains "<p2 v="
        if "<p2 v=\""+node_scia+"\"/>" in line:
            # Add the number of the line into the array
            num_lines.append(line_number)
            #print({line[-2]})
            a = linecache.getline(first_file_txt, line_number-10)
            start_index = a.find("n=\"") + len("n=\"")
            end_index = a.find("\"", start_index)
            a = a[start_index:end_index]
            print(a)

            b = linecache.getline(first_file_txt, line_number+3)
            start_index = b.find("t=\"") + len("t=\"")
            end_index = b.find("\"", start_index)
            b = b[start_index:end_index]
            print(b)
            c = linecache.getline(first_file_txt, line_number+4)
            start_index = c.find("t=\"") + len("t=\"")
            end_index = c.find("\"", start_index)
            c = c[start_index:end_index]
            print(c)
            d = linecache.getline(first_file_txt, line_number+5)
            start_index = d.find("v=\"") + len("v=\"")
            end_index = d.find("\"", start_index)
            d = d[start_index:end_index]
            #print(d)
            values = [a, b, c, d]
            
            my_array.append(values)


with open(first_file_txt, "r") as file:
    # Read every line in the file
    for line_number, line in enumerate(file, start=1):
        # Check if the line contains "<p3 v=" 
        if "<p3 v=\""+node_scia+"\"/>" in line:
            # Add the line number into the array
            num_lines.append(line_number)
            #print({line[-2]})
            a = linecache.getline(first_file_txt, line_number+3)
            start_index = a.find("n=\"") + len("n=\"")
            end_index = a.find("\"", start_index)
            a = a[start_index:end_index]
            print(a)

            b = linecache.getline(first_file_txt, line_number+6)
            start_index = b.find("t=\"") + len("t=\"")
            end_index = b.find("\"", start_index)
            b = b[start_index:end_index]
            print(b)
            c = linecache.getline(first_file_txt, line_number+7)
            start_index = c.find("t=\"") + len("t=\"")
            end_index = c.find("\"", start_index)
            c = c[start_index:end_index]
            print(c)
            d = linecache.getline(first_file_txt, line_number+8)
            start_index = d.find("v=\"") + len("v=\"")
            end_index = d.find("\"", start_index)
            d = d[start_index:end_index]
            #print(d)
            values = [a, b, c, d]
            
            my_array.append(values)



print(num_lines)
print(my_array)

# Open the file in write mode
with open(file_csv, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)
    
    # Write each row of the matrix to the CSV file
    csv_writer.writerows(my_array)

print("CSV file has been created successfully.")