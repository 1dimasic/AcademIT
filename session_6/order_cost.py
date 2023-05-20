FOR_DISCOUNT_MIN_COUNT = 10
FOR_DISCOUNT_MIN_ORDER_COST = 1000
MIN_DISCOUNT = 5
MAX_DISCOUNT = 10
HUNDRED_PERCENT = 100


def get_order_cost(price_1, count_1, price_2, count_2):
    order_cost = price_1 * count_1 + price_2 * count_2
    total_count = count_1 + count_2

    if total_count >= FOR_DISCOUNT_MIN_COUNT and order_cost >= FOR_DISCOUNT_MIN_ORDER_COST:
        return order_cost * (1 - MAX_DISCOUNT / HUNDRED_PERCENT)

    if total_count >= FOR_DISCOUNT_MIN_COUNT or order_cost >= FOR_DISCOUNT_MIN_ORDER_COST:
        return order_cost * (1 - MIN_DISCOUNT / HUNDRED_PERCENT)

    return order_cost


product_1_price = float(input('Введите стоимость первого продукта: '))
product_1_count = int(input('Введите количество первого продукта: '))

product_2_price = float(input('Введите стоимость второго продукта: '))
product_2_count = int(input('Введите количество второго продукта: '))

order = (product_1_price, product_1_count, product_2_price, product_2_count)

print(f'Стоимость Вашего заказа с учетом скидки = {get_order_cost(*order)}')
