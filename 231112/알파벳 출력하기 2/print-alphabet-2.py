n = int(input())
target = 'A'
for i in range(n) :
    for j in range(i) :
        print("  ", end = "")
    for j in range(n-i) :
        print(target, end = " ")
        target = chr(ord(target) + 1)
    print()