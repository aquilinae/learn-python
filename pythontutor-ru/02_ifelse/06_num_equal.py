'''
http://pythontutor.ru/lessons/ifelse/problems/num_equal/
Даны три целых числа. Определите, сколько среди них совпадающих.
Программа должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).
'''

a = int(input())
b = int(input())
c = int(input())

equal = 0

if a == b == c:
    equal = 3
elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
    equal = 2
else:
    equal = 0

print(equal)
