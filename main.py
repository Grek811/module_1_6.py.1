my_dict = {'Вася': 1990, 'Петя': 1993, 'Леша': 1988 }
print(my_dict)
print(my_dict['Вася'])
print(my_dict.get('Сережа', 'Такого ключа нет'))
my_dict.update({'Люся': 1991, 'Оля': 1994})
print(my_dict)
my_dict.pop('Петя')
print(my_dict)
my_set = {1,2,3,4,5,6,1,2,5,3, 'Леша', True, (1,2,3,4,5)}
print(my_set)
print(my_set.add('Ася'))
print(my_set.add(45))
print(my_set)
print(my_set.discard('Ася'))
print(my_set)

