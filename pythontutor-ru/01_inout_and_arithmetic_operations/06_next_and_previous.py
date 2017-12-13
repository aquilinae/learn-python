'''
http://pythontutor.ru/lessons/inout_and_arithmetic_operations/problems/next_and_previous/
Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере (пробелы важны!).
'''

number = input()
print("The next number for the number " + number + " is " + str(int(number) + 1))
print("The previous number for the number " + number + " is " + str(int(number) - 1))
