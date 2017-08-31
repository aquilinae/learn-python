#[STEPIK]
# Программирование на Python https://stepik.org/67
# 03_04_02 Файловый ввод/вывод

'''
На прошлой неделе мы сжимали строки, используя кодирование повторов. Теперь нашей задачей будет восстановление исходной строки обратно.

Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.

Запишите полученный текст в файл и прикрепите его, как ответ на это задание.

В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

Sample Input:
a3b4c2e10b1
Sample Output:
aaabbbbcceeeeeeeeeeb
'''
# o10l11Y19t19C6u14p7J19S18b7T16B6s9k10N19C4X9v11t5e2o15W18
# o10l11y19t19c6u14p7j19s18b7t16b6s9k10n19c4x9v11t5e2o15w18

#test_string = 'a12b10c3d1'

digits = set('0123456789')
i = 0
multiplier = ''
decrypted = ''

with open('03_04_02_input.txt') as in_f_obj:
    string = in_f_obj.readline().strip()
	
char = string[i]
i += 1

while i < len(string):    
	
	while string[i] in digits:
		multiplier += string[i]
		i += 1
		if i > (len(string) - 1):
			break
	
	#print(char * int(multiplier), end='')
	decrypted += (char * int(multiplier))
   
	multiplier = '' 
	if i > (len(string) - 1):
			break
	char = string[i]
	
	i += 1	

with open('03_04_02_ouput.txt', 'w') as out_f_obj:
	out_f_obj.write(decrypted)