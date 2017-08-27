#[STEPIK]
# Программирование на Python https://stepik.org/67
# 3.4.2 Файловый ввод/вывод

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

test_string = a12b10c3d1

digits = set('0123456789')
i = 1

with open('input.txt') as input_f_obj:
    string = input_f_obj.readline().lower().strip()

    while (i + 1) < len(string):
        if string[i] in digits:
            number += string[i]
            i += 1

with open('ouput.txt', 'w') as ouput_f_obj:
