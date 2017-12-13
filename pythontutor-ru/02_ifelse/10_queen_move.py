'''
http://pythontutor.ru/lessons/ifelse/problems/queen_move/
Шахматный ферзь ходит по диагонали, горизонтали или вертикали.
Даны две различные клетки шахматной доски, определите, может ли ферзь попасть с первой клетки на вторую одним ходом.
'''

a_x = int(input())
a_y = int(input())
b_x = int(input())
b_y = int(input())

if (a_x == b_x) or (a_y == b_y):
    print('YES')
elif abs(a_x - b_x) <= 1 and abs(a_y - b_y) <= 1:
    print('YES')
elif abs(a_x - b_x) == abs(a_y - b_y):
    print('YES')
else:
    print('NO')
