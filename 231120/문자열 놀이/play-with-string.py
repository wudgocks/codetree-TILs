s, q = map(str,input().split())
q = int(q)

str_lst = list(s)

for i in range(q) :
    check_lst = list(input().split())
    check_lst[0] = int(check_lst[0])
    # 1번 질의
    if check_lst[0] == 1 :
        check_lst[1] = int(check_lst[1])
        check_lst[2] = int(check_lst[2])
        idx1, idx2 = check_lst[1]-1, check_lst[2]-1
        temp = str_lst[idx1]
        str_lst[idx1] = str_lst[idx2]
        str_lst[idx2] = temp
        print(''.join(str_lst))

    # 2번 질의
    if check_lst[0] == 2 :
        for i in range(len(str_lst)) :
            if str_lst[i] == check_lst[1] :
                str_lst[i] = check_lst[2]
        print(''.join(str_lst))