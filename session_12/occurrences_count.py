def get_occurrences_count(string, substring):
    lower_case_string = string.lower()
    lower_case_substring = substring.lower()
    count = 0
    current_index = 0

    while True:
        current_index = lower_case_string.find(lower_case_substring, current_index)

        if current_index == -1:
            break

        count += 1
        current_index += len(lower_case_substring)

    return count


occurrences_count = 0
verification_substring = input('Введите строку для поиска количества её вхождений: ')

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        occurrences_count += get_occurrences_count(line, verification_substring)

print(f'Количество вхождений строки "{verification_substring}" = {occurrences_count}')
