n = int(input())
num = 1
for i in range(1, n +1) :
    for j in range(i, n+1) :
        print(f'{i} * {num} = {i * num}', end = "")
        num += 1
        if j != n : 
            print(" / ", end = "")
    num = 1
    print()