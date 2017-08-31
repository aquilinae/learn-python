# [STEPIK]
# Программирование на Python https://stepik.org/67
# 02_06_11 Задачи по материалам недели

'''
Дополнительная

Выведите таблицу размером n×n, заполненную числами от 1 до n2 по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):

Sample Input:
5
Sample Output:
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
'''

n = int(input())

x = 0
y = 0
dx = 1
dy = 0

# Инициализация квадратной матрицы nxn с элементами типа None
matrix = [[None] * n for _ in range(n)]

for i in range(1, n**2+1):
    matrix[x][y] = i
    nx = x + dx
    ny = y + dy
    # Проверяем, не вышла ли позиция за границы и не занята ли уже ячейка
    if (0 <= nx < n) and (0 <= ny < n) and (not matrix[nx][ny]):
        x = nx
        y = ny
    else:
        #dx, dy = -dy, dx
        # Если позиция за границей и ячейка не пуста, разворачиваем матрицу на 90 градусов
        swap = -dy
        dy = dx
        dx = swap
        x = x + dx
        y = y + dy

# Выводим заполненную матрицу        
for y in range(n):
    for x in range(n):
        print(matrix[x][y], end = ' ')
    print()
