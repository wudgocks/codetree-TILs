n = int(input())
sumStr = 0
counter = 0
for i in range(n) :
    string = input()
    sumStr += len(string)
    if string[0] == 'a' :
        counter += 1
    
print(sumStr, counter)