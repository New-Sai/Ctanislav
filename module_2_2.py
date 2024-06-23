
first = int(input('Введите первое целое число: '))
second =int(input('Введите второе целое число: '))
third = int(input('Введите третье целое число: '))
if first == second == third:
    print('Вывод: 3')
elif first == second or first == third or second == third:
    print('Вывод: 2')
else:
    print('Вывод: 0')