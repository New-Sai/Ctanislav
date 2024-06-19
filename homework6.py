my_dict = {'Alexander': 1978, 'Yuliya': 1998, 'Petyua': 2003}
print('Dict:', my_dict)
print('Existing value:', my_dict['Yuliya'])
print('Not existing value:', my_dict.get('Vladimir'))
my_dict.update({'Kamila' : 2005,
                'Artem' : 1999})
Deleted_value = my_dict.pop('Alexander')
print('Deleted value:', Deleted_value)
print('Modified dictionary:', my_dict)

#Работа с множествами
my_set = {'Стокгольм', 'Москва', 'Стокгольм', 89038856745, 2.556, True, 2.556,}
print('Set:', my_set)
my_set.update({'Стамбул', 34})
my_set.remove(True)
print('Modified set:', my_set)