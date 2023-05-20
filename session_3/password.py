correct_password = 'qwer'

user_password = input('Введите пароль: ')

if user_password == correct_password:
    print('Пароль верный')
elif len(user_password) > len(correct_password):
    print('Пароль неверный и слишком длинный')
elif len(user_password) < len(correct_password):
    print('Пароль неверный и слишком короткий')
else:
    print('Пароль неверный')
