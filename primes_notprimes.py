n = 1
list = [n, n+1]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
del_3 = []
not_del_3 = []
for i in numbers:
    if i % 3 == 0:
        is_del = True
        del_3.append(i)
    else:
        not_del_3.append(i)
print('Primes: ', (del_3))
print('Not primes: ', (not_del_3))
