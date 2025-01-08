import random
def lottery(eduard, nastya):
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    win_1 = random.choice(tickets)
    tickets.remove(win_1)
    win_2 = random.choice(tickets)
    return win_1, win_2
win_1, win_2 = lottery('eduard','nastya')
print(win_1, win_2)



