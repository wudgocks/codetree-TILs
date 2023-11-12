n = int(input())
cnt = 0
for i in range(n) :
    for j in range(i) :
        print("  ", end = "")
    for j in range(n-i) :
        if cnt >= 9 :
            cnt = 0
        cnt += 1
        print(cnt, end = " ")
    print()