n = int(input())

for i in range(2*n + 1) :
    if i % 2 == 0 :
        for j in range(2*n + 1) :
            print("* ", end = "")
    # i가 홀수인 경우 =>  한개씩 띄우면서 출력
    else : 
        for j in range(2 * n + 1) :
            if j % 2 == 0 :
                print("* ", end ="")
            else :
                print("  ", end= "")
    print()