string = input('Введите строку: ')

digits_count = 0
letters_count = 0
whitespaces_count = 0
other_symbols_count = 0

for symbol in string:
    if symbol.isdigit():
        digits_count += 1
    elif symbol.isalpha():
        letters_count += 1
    elif symbol.isspace():
        whitespaces_count += 1
    else:
        other_symbols_count += 1

print(f'Количество цифр в строке = {digits_count}, букв = {letters_count}, '
      f'пробельных символов = {whitespaces_count}, других символов = {other_symbols_count}')
