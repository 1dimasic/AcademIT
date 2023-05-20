numbers_list = [4, 6, 8, 10, 8]

# 1
reverse_numbers_list = numbers_list[::-1]
print(f'Список в обратном порядке: {reverse_numbers_list}')

# 2
reverse_numbers_list = []

for i in range(len(numbers_list) - 1, -1, -1):
    reverse_numbers_list.append(numbers_list[i])

print(f'Список в обратном порядке: {reverse_numbers_list}')

# 3
for i in range(len(numbers_list) // 2):
    numbers_list[i], numbers_list[-i - 1] = numbers_list[-i - 1], numbers_list[i]

print(f'Список в обратном порядке: {numbers_list}')
