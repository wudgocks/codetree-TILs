string = input()
num  = int(input())
if num > len(string) :
    num = len(string)
for i in range(len(string)-1, len(string) - num-1, -1) :
    print(string[i], end = "")