# [STEPIK]
# Программирование на Python https://stepik.org/67
# 03_07_02 Задачи по материалам недели

'''
Дополнительная

В какой-то момент в Институте биоинформатики биологи перестали понимать, что говорят информатики: они говорили каким-то странным набором звуков. 

В какой-то момент один из биологов раскрыл секрет информатиков: они использовали при общении подстановочный шифр, т.е. заменяли каждый символ исходного сообщения на соответствующий ему другой символ. Биологи раздобыли ключ к шифру и теперь нуждаются в помощи: 

Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. Программа принимает на вход две строки одинаковой длины, на первой строке записаны символы исходного алфавита, на второй строке — символы конечного алфавита, после чего идёт строка, которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.

Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%

Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. Получаем следующие строки, которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac

Sample Input 1:
abcd
*d%#
abacabadaba
#*%*d*%
Sample Output 1:
*d*%*d*#*d*
dacabac

Sample Input 2:
dcba
badc
dcba
badc
Sample Output 2:
badc
dcba
'''

string = str(input())
cipher = str(input())

message_to_cipher = str(input())
cipher_to_message = str(input())
ciphered_message = ''
unciphered_message = ''

encryption = {}

# Наполняем шифровальный словарь
for i in range(len(string)):
    encryption[string[i]] = cipher[i]

# Зашифровываем сообщение по наполненному словарю    
for i in range(len(message_to_cipher)):
    for key in encryption.keys():
        if message_to_cipher[i] == key:
            ciphered_message += encryption[key]

# Расшифровываем сообщение по наполненному словарю             
for i in range(len(cipher_to_message)):
    for key, value in encryption.items():
        if cipher_to_message[i] == value:
            unciphered_message += key

print(ciphered_message)
print(unciphered_message)