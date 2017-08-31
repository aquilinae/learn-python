# [STEPIK]
# Программирование на Python https://stepik.org/67
# 02_04_07 Строки и символы

'''
Узнав, что ДНК не является случайной строкой, только что поступившие в Институт биоинформатики студенты группы информатиков предложили использовать алгоритм сжатия, который сжимает повторяющиеся символы в строке.

Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются на этот символ и количество его повторений в этой позиции строки.

Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную последовательность на стандартный вывод.
Кодирование должно учитывать регистр символов.

Sample Input 1:
aaaabbcaa
Sample Output 1:
a4b2c1a2

Sample Input 2:
abc
Sample Output 2:
a1b1c1
'''

# Решение с костылем
'''
string = input()
newString = string + ' ' # Дописываем пробел в конец строки
counter = 1

for i in range(len(newString)):
    if newString[i] == ' ': # Если в итерации встречается дописанный пробел, завершаем цикл
        break
    elif newString[i] == newString[i+1]:
        counter += 1
    else:
        print(newString[i] + str(counter), end='')
        counter = 1
'''

# Решение без костыля

string = input()
counter = 1
i = 0

while (i + 1) < len(string): # Проверяем, не последний ли символ, чтобы избежать out of range
    if string[i] == string[i+1]:
        counter += 1
    else:
        print(string[i] + str(counter), end='')
        counter =1

    i += 1
# Т.к. последняя последовательность отсекается, чтобы не случилось out of range, выводим остаток принудительно
print(string[i] + str(counter))

# Элегантное решение с побуквенным сравнением
'''
message = str(input())
cnt = 1
x = 1
j = message[x:x+1]
for i in message:
    if i in j:
        cnt += 1
    else:
        print(i, end='')
        print(cnt, end='')
        cnt = 1
    x += 1
    j = message[x:x+1]
'''
