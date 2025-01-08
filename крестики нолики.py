def draw_area():
    for i in area:
        print(*i)
        print()

print('ИГРА НАЧАЛАСЬ')
print('-------------')
area = [['*', '*', '*'],['*', '*', '*'],['*', '*', '*']]
draw_area()
area[0][0] = 'X'
print()
draw_area()