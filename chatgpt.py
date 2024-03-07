def replace_last_word(input_file, output_file, replacement_word):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    with open(output_file, 'w') as file:
        for line in lines:
            parts = line.strip().split(';')
            parts[-1] = replacement_word
            new_line = ';'.join(parts) + '\n'
            file.write(new_line)

# Example usage:
input_file = 'data_2.txt'
output_file = 'data_4.txt'
replacement_word = 'Replacement'  # Change this to the word you want to replace with

replace_last_word(input_file, output_file, replacement_word)
