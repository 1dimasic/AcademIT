def do_upper_strings_list(strings_list):
    for i in range(len(strings_list)):
        strings_list[i] = strings_list[i].upper()


strings_in_list = ['spam', 'Hello', 'gOod', 'HELp']
do_upper_strings_list(strings_in_list)
print(f'Список строк в верхнем регистре: {strings_in_list}')
