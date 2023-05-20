# 1
numbers = []

for i in range(1, 101):
    numbers.append(i)

for number in numbers:
    print(number, end=' ')

print()

# 2
numbers = [number for number in range(1, 101)]

for number in numbers:
    print(number, end=' ')
