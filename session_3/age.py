age = input('Введите Ваш возраст: ')

if int(age) < 1:
    print('Вы слишком малы')
elif int(age) > 112:
    print('Вы слишком стары')
else:
    last_two_age_digits = int(age[-2:])

    if 5 <= last_two_age_digits <= 19:
        print(f'Вам {age} лет')
    else:
        last_age_digit = last_two_age_digits % 10

        if last_age_digit == 0 or last_age_digit >= 5:
            print(f'Вам {age} лет')
        elif last_age_digit == 1:
            print(f'Вам {age} год')
        else:
            print(f'Вам {age} года')
