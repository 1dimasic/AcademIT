deposit = float(input('Введите Ваш депозит: '))
percent_per_year = float(input('Введите % годовых: '))
months_count = int(input('Введите количество месяцев: '))

MONTHS_IN_YEAR_COUNT = 12
HUNDRED_PERCENT = 100
deposit_with_capitalization = deposit
percent_per_month = percent_per_year / (MONTHS_IN_YEAR_COUNT * HUNDRED_PERCENT)

for month in range(1, months_count + 1):
    deposit_with_capitalization += deposit_with_capitalization * percent_per_month

profit = deposit_with_capitalization - deposit

print(f'Ваш вклад с капитализацией = $ {deposit_with_capitalization:.2f}, прибыль = $ {profit:.2f}')
