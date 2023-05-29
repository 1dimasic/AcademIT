string = '1,2,3,4,5'

numbers_list = string.split(',')
numbers_sum = 0

for number in numbers_list:
    numbers_sum += int(number)

print(numbers_sum)
