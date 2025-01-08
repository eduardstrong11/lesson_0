import random
digit_1 = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
a = random.choice(digit_1)
result = ''
for i in range(1, 21):
    for j in range(i, 21):
        k = i + j
        if i == j:
            continue
        if a % k != 0:
            continue
        else:
            result += str(i) + str(j)
print(a)
print(result)



















