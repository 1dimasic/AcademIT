with open('input.csv', 'r', encoding='utf-8') as csv_file, open('output.html', 'w') as html_file:
    html_file.write('<table border=1>')

    input_line = ''
    quotes_count = 0

    for line in csv_file:
        input_line += line
        quotes_count += line.count('"')

        if quotes_count % 2 != 0:
            continue

        if input_line == '\n':
            input_line = ''
            quotes_count = 0
            continue

        row = []
        current_index = 0

        for i in range(len(input_line)):
            if input_line[i] == ',':
                if input_line[current_index:i].count('"') % 2 == 0:
                    row.append(input_line[current_index:i])
                    current_index = i + 1

        row.append(input_line[current_index:].rstrip())

        for i in range(len(row)):
            if row[i]:
                if row[i][0] == '"' and row[i][-1] == '"':
                    row[i] = row[i][1:-1]

        for i in range(len(row)):
            row[i] = row[i].replace('""', '"')
            row[i] = row[i].replace('\n', '<br/>')

        html_file.write('<tr>')

        for i in range(len(row)):
            html_file.write(f'<td>{row[i]}</td>\t')

        html_file.write('</tr>')
        html_file.write('<br/>')

        input_line = ''
        quotes_count = 0

    html_file.write('</table>')
