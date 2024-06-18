# Сам по себе кортеж считается неизменяемым в таком виде:
immutable_var = (1, 0.5, 'Hello', True)
print(immutable_var)
# Если я попытаюсь ввести команду immutable_var [0] = 4 то программа не будет выполненна
# Но если создать внутри кортежа список, то тогда мы можем изменить элементы внутреннего списка:
immutable_var = ([1],[0.5],['Hello'],[True])
print(immutable_var)
immutable_var[0][0] = 4
print(immutable_var)
# Изменяемая структура данных (Списки)
mutable_list = [1, 0.5, 'Hello', True]
print(mutable_list)
# Списки всегда заключаются в квадратные скобки, в таком случае мы можем изменять каждый элемент по отдельности
# Например я хочу поменять 'Hello' на 'Goodbye'
mutable_list[-2] = 'Goodbye'
print(mutable_list)
