# 1
for i in range(101):
    print(i, end=' ')

print()

# 2
for i in range(7, 122):
    print(i, end=' ')

print()

# 3
for i in range(100, 29, -1):
    print(i, end=' ')

print()

# 4
for i in range(100, 0, -1):
    if i % 4 == 0:
        print(i, end=' ')

print()

# 5
numbers_count = int(input('Введите количество чисел n = '))

for i in range(1, numbers_count + 1):
    print(i ** 2, end=' ')

print()

# 6
start_number = int(input('Введите начало диапазона: '))
end_number = int(input('Введите конец диапазона: '))

numbers_sum = 0
numbers_count = 0

for i in range(start_number, end_number + 1):
    numbers_sum += i
    numbers_count += 1

arithmetic_average = numbers_sum / numbers_count
print(f'Среднее арифметическое = {arithmetic_average}')

# 7
for i in range(1, 101):
    print(i, end=' ')

    if i >= 30:
        break

print()

# 8
for i in range(101):
    if i == 5 or i % 3 == 0 or 60 <= i <= 80:
        continue

    print(i, end=' ')

print()

# 8.1

i = 1

while i <= 100:
    if i == 5 or i % 3 == 0 or 60 <= i <= 80:
        i += 1
        continue

    print(i, end=' ')
    i += 1
