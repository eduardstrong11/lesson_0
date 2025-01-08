#Неизменяемые объекты (кортеж)
immutable_var = 1.5, 'Example ', 2
print(immutable_var)
#Попытки изменения элементов кортежа
immutable_var[0] = 2.5
print(immutable_var)
immutable_var[1] = 'Example_2'
print(immutable_var)
immutable_var[2] = 3
print(immutable_var)

#Элементы кортежей нельзя изменить, потому что кортежи неизменяемы (как константа).
#Котреж для того и придуман, что в отличие от списка, элементы в нем при попытке их поменять всегда остаются в неизменном виде.

#Изменяемые объекты (список)
mutable_list = [1.5, 'Example ', 2]
print(mutable_list)
mutable_list[0] = 2.5
mutable_list[1] = 'Example_2'
mutable_list[2] = 3
print(mutable_list)




