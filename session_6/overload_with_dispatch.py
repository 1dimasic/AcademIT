from multipledispatch import dispatch


@dispatch(int)
def print_type(data):
    print(f'{data} - целое число')


@dispatch(float)
def print_type(data):
    print(f'{data} - вещественное число')


@dispatch(str)
def print_type(data):
    print(f'{data} - строка')


@dispatch(complex)
def print_type(data):
    print(f'{data} - комплексное число')


@dispatch(bool)
def print_type(data):
    print(f'{data} - bool тип')


types_list = [2, 2.2, 'hello world', 1 + 2j, True]

for types in types_list:
    print_type(types)
