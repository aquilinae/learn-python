'''
http://pythontutor.ru/lessons/ifelse/problems/knight_move/
Шахматный конь ходит буквой “Г” — на две клетки по вертикали в любом направлении и на одну клетку по горизонтали, или наоборот.
Даны две различные клетки шахматной доски, определите, может ли конь попасть с первой клетки на вторую одним ходом.
'''

a_x = int(input())
a_y = int(input())
b_x = int(input())
b_y = int(input())

diff_x = abs(a_x - b_x)
diff_y = abs(a_y - b_y)
diff_xy = abs(diff_x - diff_y)

if (diff_x == 0 or diff_y == 0) and (diff_x == 1 or diff_y == 1):
    print('NO')
elif (diff_x <= 2 and diff_y <= 2) and diff_xy == 1:
    print('YES')
else:
    print('NO')
