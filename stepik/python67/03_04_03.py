#[STEPIK]
# Программирование на Python https://stepik.org/67
# 03_04_03 Файловый ввод/вывод

'''
Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.

Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).

Слова, написанные в разных регистрах, считаются одинаковыми.

Sample Input:
abc a bCd bC AbC BC BCD bcd ABC
Sample Output:
abc 3
'''

dictionary = {}

with open('03_04_03_input.txt') as in_f_obj:
	for line in in_f_obj:
		line = line.lower()
		for word in line.split():
			if word not in dictionary:
				dictionary[word] = 1
			elif word in dictionary:
				dictionary[word] += 1			

max_quantity = 1
	
for key, value in dictionary.items():
	current_quantity = dictionary[key]
	if current_quantity > max_quantity:
		max_quantity = current_quantity
		word_with_max_quantity = key
	
with open('03_04_03_output.txt', 'w') as out_f_obj:
	most_popular = (word_with_max_quantity + ' ' + str(max_quantity))
	out_f_obj.write(most_popular)