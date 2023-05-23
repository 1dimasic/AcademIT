def is_palindrome(string):
    forward_index = 0
    reverse_index = len(string) - 1
    lower_case_string = string.lower()

    while forward_index < len(string) // 2:
        while not lower_case_string[forward_index].isalpha() and forward_index < len(string) - 1:
            forward_index += 1

        while not lower_case_string[reverse_index].isalpha() and reverse_index > 0:
            reverse_index -= 1

        if lower_case_string[forward_index] != lower_case_string[reverse_index]:
            return False

        forward_index += 1
        reverse_index -= 1

    return True


entered_string = input('Введите строку: ')

if is_palindrome(entered_string):
    print('Введенная строка является палиндромом')
else:
    print('Введенная строка не является палиндромом')
