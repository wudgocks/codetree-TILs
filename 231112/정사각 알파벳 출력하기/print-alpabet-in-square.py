n = int(input())

target = 'A'
for i in range(n) :
    for j in range(n) :
        print(target, end = "")
        target = ord(target)
        target += 1
        target = chr(target)
        
    print()