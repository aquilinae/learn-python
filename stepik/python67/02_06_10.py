# [STEPIK]
# Программирование на Python https://stepik.org/67
# 02_06_10 Задачи по материалам недели

'''
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк, заканчивающихся строкой, содержащей только строку "end" (без кавычек)

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). 
У крайних символов соседний элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.

Sample Input 1:
9 5 3
0 7 -1
-5 2 9
end
Sample Output 1:
3 21 22
10 6 19
20 16 -1

Sample Input 2:
1
end
Sample Output 2:
4
'''

row = ''
matrix = []

while True:
	row = input()
	if row == 'end':
		break
	matrix.append([int(i) for i in row.split()])
	
ai = len(matrix)
aj = len(matrix[0])

newMatrix =[
    [(matrix[i-1][j] + matrix[(i+1)%ai][j] + matrix[i][j-1] + matrix[i][(j+1)%aj]) 
        for j in range(aj)] 
            for i in range(ai)]

for i in range(ai):
    for j in range(aj):
        print(newMatrix[i][j], end=' ')
    print()