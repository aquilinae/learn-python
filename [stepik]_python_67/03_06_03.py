#[STEPIK]
# Программирование на Python https://stepik.org/67
# 03_06_03 Установка дополнительных модулей

'''
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора. 

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.
'''

import requests

url_pattern = 'https://stepik.org/media/attachments/course67/3.6.3/'

with open('03_06_03_input.txt') as in_f_obj:
	url = in_f_obj.read().strip()

counter = 0


while True:
	r = requests.get(url)
	if 'We' in str(r.text.strip()):
		break
	url = url_pattern + str(r.text.strip())
	#print(str(counter) + ' ' + url)
	#counter += 1

text = r.text.strip()

with open('03_06_03_output.txt', 'w') as out_f_obj:
	out_f_obj.write(text)

'''
with open('test.txt') as f_obj:
	text = f_obj.read().strip()

print()
print('*' * 40)
print(text)
print()
print(text[:2])
print('*' * 40)

with open('ntest.txt') as f_obj:
	text = f_obj.read().strip()

print()
print('*' * 40)	
print(text)
print()
print(text[:2])
if 'We' in text:
	print(True)
print('*' * 40)
'''