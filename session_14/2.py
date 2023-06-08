def f(line):
    pass


with open('input.csv', 'r') as csv_file, open('html_file.html', 'w') as html_file:
    html_file.write('<table>')

    for line in csv_file:
        html_file.write(f'<tr>{line.split(",")}</tr>')

    html_file.write('</table>')