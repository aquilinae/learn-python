# [STEPIK]
# Программирование на Python https://stepik.org/67
# 03_07_05 Задачи по материалам недели

'''
Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов.

Напишите программу, которая прочитает этот файл и подсчитает для каждого класса средний рост учащегося.

Файл состоит из набора строк, каждая из которых представляет собой три поля:
Класс Фамилия Рост

Класс обозначается только числом. Буквенные модификаторы не используются. Номер класса может быть от 1 до 11 включительно. В фамилии нет пробелов, а в качестве роста используется натуральное число, но при подсчёте среднего требуется вычислить значение в виде вещественного числа.

Выводить информацию о среднем росте следует в порядке возрастания номера класса (для классов с первого по одиннадцатый). Если про какой-то класс нет информации, необходимо вывести напротив него прочерк, например:

Sample Input:
6	Вяххи	159
11	Федотов	172
7	Бондарев	158
6	Чайкина	153
Sample Output:
1 -
2 -
3 -
4 -
5 -
6 156.0
7 158.0
8 -
9 -
10 -
11 172.0
'''

class_rawinfo = {}
#new_heights = 0
#new_students = 0
class_info = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
#class_info = []

with open('03_07_05_input.txt') as in_f_obj:
	for line in in_f_obj:
		#print(line)
		string = line.rstrip().split('\t')
		#print(string)
#n = int(input())
#for _ in range(n):
	#string = input().split('	')
		if string[0] not in class_rawinfo:
			class_rawinfo[string[0]] = [int(string[2]), 1]
		elif string[0] in class_rawinfo:
			heights = class_rawinfo[string[0]][0] + int(string[2])
			students = class_rawinfo[string[0]][1] + 1
			class_rawinfo[string[0]] = [heights, students]

for k, v in class_rawinfo.items():
	#print(k, str(v[0] / v[1]))
	#list.pop([int(k)-1])
	class_info[int(k)-1] = v[0] / v[1]
	#print(class_rawinfo)
	#print(class_info)

with open('03_07_05_output.txt', 'w') as out_f_obj:	
	for i in range(len(class_info)):
		#print(i+1, str(class_info[i]))
		output = str(i+1) + ' ' + str(class_info[i]) + '\n'
		#print(output)
		out_f_obj.write(output)