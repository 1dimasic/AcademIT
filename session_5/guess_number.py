import random

random_number = random.randint(1, 100)
attempts_count = 0

print('Добро пожаловать в игру "Угадай число!"')

while True:
    entered_number = int(input('Введите число от 1 до 100: '))

    if entered_number < 1 or entered_number > 100:
        print('Число некорректно!')
        continue

    attempts_count += 1

    if entered_number == random_number:
        print(f'Вы угадали число за количество попыток = {attempts_count}')
        break

    if entered_number > random_number:
        print('Ваше число больше. Попробуйте еще!')
    else:
        print('Ваше число меньше. Попробуйте еще!')
