def get_occurrences_count(string, desired_string):
    lower_case_string = string.lower()
    occurrences_count = 0
    current_index = 0
    lower_case_string.find(desired_string, current_index)

    while True:
        if lower_case_string.find(desired_string, current_index) == -1:
            break

        occurrences_count += 1
        current_index = lower_case_string.find(desired_string, current_index) + len(desired_string)

    return occurrences_count


#print(get_occurrences_count('лес лес лес поле лес лес ЛЕС', 'лес'))

count = 0

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        count += get_occurrences_count(line, 'лес')

print(count)