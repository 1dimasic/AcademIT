day = int(input('Введите день: '))
month = int(input('Введите месяц: '))
year = int(input('Введите год: '))

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    days_in_month_count = 31
elif month == 2:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days_in_month_count = 29
    else:
        days_in_month_count = 28
else:
    days_in_month_count = 30

if day < 1 or day > days_in_month_count or month < 1 or month > 12:
    print("Дата введена некорректно!")
else:
    if day != days_in_month_count:
        print(f'Следующая дата: {day + 1:02d}.{month:02d}.{year:04d}')
    else:
        if month != 12:
            print(f'Следующая дата: {1:02d}.{month + 1:02d}.{year:04d}')
        else:
            print(f'Следующая дата: {1:02d}.{1:02d}.{year + 1:04d}')
