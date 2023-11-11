n = int(input())

num = 2

for i in range(n) :
    for j in range(n) :
        if num > 8 :
            num = 2
        print(num, end= " ")
        num += 2
    
    print()