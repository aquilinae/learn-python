# [STEPIK]
# Программирование на Python https://stepik.org/67
# 1.12 Задачи по материалам недели

'''
Паша очень любит кататься на общественном транспорте, а получая билет, сразу проверяет, счастливый ли ему попался. 
Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера билета.

Однако Паша очень плохо считает в уме, поэтому попросил вас написать программу, которая проверит равенство сумм и выведет "Счастливый", если суммы совпадают, и "Обычный", если суммы различны.

На вход программе подаётся строка из шести цифр.

Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы.

Sample Input 1:
090234
Sample Output 1:
Счастливый

Sample Input 2:
123456
Sample Output 2:
Обычный
'''   

#ticketNumber = int(input())
ticketNumber = 123456

print((ticketNumber // 10e4) % 10e0)
print((ticketNumber // 10e3) % 10e0)
print((ticketNumber // 10e2) % 10e0)
print((ticketNumber // 10e1) % 10e0)
print((ticketNumber // 10e0) % 10e0)
print((ticketNumber // 10e-1) % 10e0)

'''
number1 = 
print(number1)
number2 = 
print(number2)
number3 = 
print(number3)
number4 = 
print(number4)
number5 = 
print(number5)
number6 = 
print(number6)

if (number1 + number2 + number3) == (number4 + number5 + number6):
	print('Счастливый')
elif:
	print('Обычный')
'''