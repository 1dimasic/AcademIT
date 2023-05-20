def get_max_substring_length(string):
    max_length = 0

    for unique_symbol in set(string):
        substring_length = 0

        for symbol in string:
            if unique_symbol.lower() == symbol.lower():
                substring_length += 1

                if substring_length > max_length:
                    max_length = substring_length

            else:
                substring_length = 0

    return max_length


entered_string = input('Введите строку: ')

max_substring_length = get_max_substring_length(entered_string)

print(f'Максимальная длина подстроки из одного и того же символа = {max_substring_length}')
