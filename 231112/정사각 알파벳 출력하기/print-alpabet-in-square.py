n = int(input())

target = 'A'
for i in range(n) :
    for j in range(n) :
        print(target, end = "")
        target = chr(ord(target) + 1)

    print()