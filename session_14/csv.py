# def f(line):
#     c = []
#     b = -1
#
#     while True:
#         b = line.find('"', b + 1)
#         if b != -1:
#             c.append(b)
#             continue
#
#         break
#
#     return c


with open('input.csv', 'r', encoding='utf-8') as csv_file, open('output.html', 'w') as html_file:
    html_file.write('<table border=1>\n')

    html_line = ''
    a = 0
    for line in csv_file:
        html_line += line
        a += line.count('"')

        if a % 2 != 0:
            continue

        d = f(html_line)

        if d:
            html_line = html_line[:d[0]] + html_line[d[0] + 1:d[-1]] + html_line[d[-1] + 1:]
            f = f(html_line)


    # tables_detail = html_line.split(',')

    for i in range(len(tables_detail)):
        html_file.write(f'<td>{tables_detail[i]}</td>\n')

        html_file.write('</tr>\n')

    html_file.write('</table>')

    html_line = ''
    a = 0
