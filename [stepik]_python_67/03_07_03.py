# [STEPIK]
# Программирование на Python https://stepik.org/67
# 03_07_03 Задачи по материалам недели

'''
Простейшая система проверки орфографии основана на использовании списка известных слов. Каждое слово в проверяемом тексте ищется в этом списке и, если такое слово не найдено, оно помечается, как ошибочное.

Напишем подобную систему.

Через стандартный ввод подаётся следующая структура: первой строкой — количество dd записей в списке известных слов, после передаётся  dd строк с одним словарным словом на строку, затем — количество ll строк текста, после чего — ll строк текста.

Напишите программу, которая выводит слова из текста, которые не встречаются в словаре. Регистр слов не учитывается. Порядок вывода слов произвольный. Слова, не встречающиеся в словаре, не должны повторяться в выводе программы.

Sample Input:
3
a
bb
cCc
2
a bb aab aba ccc
c bb aaa
Sample Output:
aab
aba
c
aaa
'''

d = int(input())
#words = []
words = set()
#unknow_words = []
unknow_words = set()	

for _ in range(d):
	#words.append(input().lower())
	words.add(input().lower())

l = int(input())


for _ in range(l):
	string = input().lower().split()
	
	for i in range(len(string)):
		if string[i] not in words:
			#unknow_words.append(string[i])
			unknow_words.add(string[i])
			
for word in unknow_words:
	print(word)