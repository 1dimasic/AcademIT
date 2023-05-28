def get_max_substring_length(string):
    if not string:
        return 0

    max_length = 1
    current_length = 1
    lower_case_string = string.lower()

    for i in range(1, len(string)):
        if lower_case_string[i] == lower_case_string[i - 1]:
            current_length += 1

            if current_length > max_length:
                max_length = current_length

        else:
            current_length = 1

    return max_length


entered_string = input('Введите строку: ')
max_substring_length = get_max_substring_length(entered_string)
print(f'Максимальная длина подстроки из одного и того же символа = {max_substring_length}')
