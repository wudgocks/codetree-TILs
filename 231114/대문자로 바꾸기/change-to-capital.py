# 2차원 배열을 구현해 각 줄에 알파벳 소문자 저장
lst_2d = [
    list(input().split())
    for _ in range(5)
]

for i in range(5) :
    for j in range (3) :
        lst_2d[i][j] = lst_2d[i][j].upper()
        print(lst_2d[i][j], end = " ")
    print()