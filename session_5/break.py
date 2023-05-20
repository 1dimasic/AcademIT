string = 'qwerty'

while True:
    entered_string = input('Введите строку: ')

    if entered_string == string:
        print('Строка введена верно, программа завершена.')
        break

    print('Строка введена не верно, попробуйте еще раз')
