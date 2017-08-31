# [STEPIK]
# Программирование на Python https://stepik.org/67
# 02_05_10 Списки

'''
Напишите программу, на вход которой подаётся список чисел одной строкой. Программа должна для каждого элемента этого списка вывести сумму двух его соседей. Для элементов списка, являющихся крайними, одним из соседей считается элемент, находящий на противоположном конце этого списка. Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).

Если на вход пришло только одно число, надо вывести его же.

Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.

Sample Input 1:
1 3 5 6 10
Sample Output 1:
13 6 9 15 7

Sample Input 2:
10
Sample Output 2:
10
'''

string = [int(i) for i in input().split()]
#string = [1, 3, 5, 6, 10] # Expected output is "13 6 9 15 7"
newString = [0 for i in range(len(string))]

if len(string) == 1:
    print(string[0])
else:
    for i in range(len(string)):
        if i + 1 < len(string):
            newString[i] = string[i-1] + string[i+1]
        else:
            newString[i] = string[i-1] + string[0]

    for _ in range(len(newString)):
        print(str(newString[_]) + ' ', end='')

# Элегантное решение с отрицательной длиной списка
'''
initial_list = [1, 3, 5, 6, 10]
sum_list = []

left_index = -1
right_index = -len(initial_list) + 1
middle_index = 0

while middle_index < len(initial_list):
    print(left_index, right_index)
    sum_list.append(initial_list[left_index] + initial_list[right_index])
    left_index += 1
    right_index += 1
    middle_index += 1

print(sum_list)
'''
