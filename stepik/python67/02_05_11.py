# [STEPIK]
# Программирование на Python https://stepik.org/67
# 02_05_11 Списки

'''
Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения, которые повторяются в нём более одного раза.

Для решения задачи может пригодиться метод sort списка.

Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.

Sample Input 1:
4 8 0 3 4 2 0 3
Sample Output 1:
0 3 4

Sample Input 2:
10
Sample Output 2:

Sample Input 3:
1 1 2 2 3 3
Sample Output 3:
1 2 3

Sample Input 4:
1 1 1 1 1 2 2 2
Sample Output 4:
1 2
'''

string = [int(i) for i in input().split()]
#string = [4, 8, 0, 3, 4, 2, 0, 3]
#string = [1 ,1 ,1 ,1 ,1 ,2, 2, 2]
#newString = [0 for i in range(len(string))]
newString = []
i = 0

string.sort()

while i+1 < len(string):
    if string[i] == string[i+1]:
        if string[i] in newString:
            i += 1
            continue
        newString.append(string[i])
    i += 1

for _ in newString:
    print(_, end=' ')
