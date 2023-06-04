with open('input.txt', 'r', encoding='utf-8') as input_file, \
        open('output.txt', 'w', encoding='utf-8') as output_file:
    for line in input_file:
        output_file.write(line.upper())
