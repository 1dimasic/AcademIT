with open('input.csv', 'r', encoding='utf-8') as csv_file, open('output.html', 'w') as html_file:
    html_file.write('<table border=1>\n')

    html_line = ''
    a = 0
    for line in csv_file:
        html_line += line
        a += line.count('"')

        if a % 2 != 0:
            continue

        c = []
        b = -1

        while True:
            b = html_line.find('"', b + 1)
            if b != -1:
                c.append(b)
                continue

            break

        if c:
            html_line = html_line[:c[0]] + html_line[c[0] + 1:] + html_line[:c[-1]] + html_line[c[-1] + 1:]
            print(html_line)

        html_line = ''
        a = 0



    #     tables_detail = html_line.split(',')
    #
    #     for i in range(len(tables_detail)):
    #         html_file.write(f'<td>{tables_detail[i]}</td>\n')
    #

    #
    #     html_file.write('</tr>\n')
    #
    # html_file.write('</table>')
