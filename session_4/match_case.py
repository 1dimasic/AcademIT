command = input('Введите команду: ')

match command:
    case 'print':
        string = input('Введите строку: ')
        print(f'Введена новая строка: {string}')
    case 'sum':
        a = float(input('Введите число а: '))
        b = float(input('Введите число b: '))
        print(f'Сумма чисел а и b равна {a + b}')
    case _:
        print('Неизвестная команда')
