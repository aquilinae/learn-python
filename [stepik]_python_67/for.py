'''
a,b,c,d=int(input()),int(input()),int(input()),int(input())#запрашиваем числа
for i in range(c,d+1):#присваиваем переменной i диапазон столбиков
    print('\t',i, end='')#начиная с отступа печатаем заданный диапазон столбиков


for l in range(a,b+1):#присваиваем переменной l диапазон строк
    print()#печатаем пропуск иначе будет печатать в строчке где указан диапазон столбиков
    print(l,end='')#печатаем строчку
    for i in range(c,d+1):#присваиваем переменной i диапазон столбиков
        print('\t',i*l, end='')#печатаем в строчку умножение вертикальных значений на горизонтальные
'''

a = int(input())
b = int(input())
c = int(input())
d = int(input())


# Выводим первую строчку, отрезок [c;d]
print(end='')
for j in range (c, d+1):
    print('\t', j, end='')
    j +=1
    if j == d+1:
        print()

# Выводим остальные строчки
for i in range (a, b+1):
    print(i, end='')
    for j in range (c, d+1):
        print('\t', i*j, end='')
        j += 1
    i += 1
    print()
