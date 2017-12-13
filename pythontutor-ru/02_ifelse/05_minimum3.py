'''
http://pythontutor.ru/lessons/ifelse/problems/minimum3/
Даны три целых числа. Выведите значение наименьшего из них.
'''

a = int(input()) #10
b = int(input()) #30
c = int(input()) #4

lowest = a

if lowest > b and (b < c or b == c):
    lowest = b
elif lowest > c and (c < b or c == b):
    lowest = c
elif lowest <= b and lowest <= c:
    pass
else:
    print("DEBUG lost condition")

print(lowest)
