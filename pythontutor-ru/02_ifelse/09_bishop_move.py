'''
http://pythontutor.ru/lessons/ifelse/problems/bishop_move/
Шахматный слон ходит по диагонали.
Даны две различные клетки шахматной доски, определите, может ли слон попасть с первой клетки на вторую одним ходом.
'''

a_x = int(input())
a_y = int(input())
b_x = int(input())
b_y = int(input())

if abs(a_x - b_x) == abs(a_y - b_y):
    print('YES')
else:
    print('NO')
