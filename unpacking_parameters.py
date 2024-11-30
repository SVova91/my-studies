def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

value_list = [2, 'вторая строка', False]
value_dict = {'a': 10, 'b': 'третья строка', 'c': True}
value_list_2 = [54.32, 'Строка']
print_params(*value_list_2, 42)
