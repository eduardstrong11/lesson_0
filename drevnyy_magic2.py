import random
digit_1 = [3,6,5,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
a = random.choice(digit_1)
password = []
print(a)
for i in range(1, 21):
    for j in range(1, 21):
        k = i + j
        if i == 21:
            break
        if a % k == 0:
            password.append(i)
            password.append(j)
        else:
            continue
print(password)