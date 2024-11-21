first = int(input('Введите число: '))
second = int(input('Введите число: '))
third = int(input('Введите число: '))
if first == second == third:
    print('Одинаковых чисел: 3')
elif first == third != second:
    print('Одинаковых чисел: 2')
elif third == second != first:
    print('Одинаковых чисел: 2')
elif first == second != third:
    print('Одинаковых чисел: 2')
else:
    print('Одинаковых чисел: 0')
    
