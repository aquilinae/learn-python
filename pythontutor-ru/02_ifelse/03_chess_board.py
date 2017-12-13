'''
http://pythontutor.ru/lessons/ifelse/problems/chess_board/
Заданы две клетки шахматной доски.
Если они покрашены в один цвет, то выведите слово YES, а если в разные цвета — то NO.
Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
'''

a_x = int(input())
b_y = int(input())
c_x = int(input())
d_y = int(input())

if (a_x + b_y + c_x + d_y) % 2 == 0:
    print('YES')
else:
    print('NO')

'''
# before taking the pattern
cell_01_col = int(input())
cell_01_row = int(input())
cell_02_col = int(input())
cell_02_row = int(input())

cell_01_is_colored = ((cell_01_col % 2 == 1) and (cell_01_row % 2 == 1)) or ((cell_01_col % 2 == 0) and (cell_01_row % 2 == 0))
cell_02_is_colored = ((cell_02_col % 2 == 1) and (cell_02_row % 2 == 1)) or ((cell_02_col % 2 == 0) and (cell_02_row % 2 == 0))
cell_01_is_uncolored = ((cell_01_col % 2 == 0) and (cell_01_row % 2 == 1)) or ((cell_01_col % 2 == 1) and (cell_01_row % 2 == 0))
cell_02_is_uncolored = ((cell_02_col % 2 == 0) and (cell_02_row % 2 == 1)) or ((cell_02_col % 2 == 1) and (cell_02_row % 2 == 0))

if cell_01_is_colored and cell_02_is_colored:
    print('YES')
elif cell_01_is_uncolored and cell_02_is_uncolored:
    print('YES')
else:
    print('NO')
'''
