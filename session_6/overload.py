def print_type(data):
    if isinstance(data, int):
        print(f'{data} - целое число')
    elif isinstance(data, float):
        print(f'{data} - вещественное число')
    elif isinstance(data, str):
        print(f'{data} - строка')
    elif isinstance(data, complex):
        print(f'{data} - комплексное число')
    else:
        print(f'{data} - bool тип')


types_list = [2, 2.2, 'hello world', 1 + 2j, bool]

for types in types_list:
    print_type(types)
