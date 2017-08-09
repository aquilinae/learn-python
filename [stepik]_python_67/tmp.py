string = input()
newString = string + ' '
counter = 1

for i in range(len(newString)):
    if newString[i] == ' ':
        break
    elif newString[i] == newString[i+1]:
        counter += 1
    else:
        print(newString[i] + str(counter), end='')
        counter = 1
