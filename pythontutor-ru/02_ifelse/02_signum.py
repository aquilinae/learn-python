'''
http://pythontutor.ru/lessons/ifelse/problems/signum/
В математике функция sign(x) (знак числа) определена так:
sign(x) = 1, если x > 0,
sign(x) = -1, если x < 0,
sign(x) = 0, если x = 0.
Для данного числа x выведите значение sign(x).
Эту задачу желательно решить с использованием каскадных инструкций if... elif... else.
'''

x = int(input())

if x > 0:
    print(1)
elif x < 0:
    print(-1)
else:
    print(0)
