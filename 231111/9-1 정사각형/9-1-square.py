n = int(input())

num = 9

for i in range(n) :
    for j in range(n) :
        if num < 1 :
            num = 9
        print(num, end ="")
        num -= 1
    print()