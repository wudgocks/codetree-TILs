n,m,k = map(int,input().split())

# 벌칙 카운터 
counter = [
    0 for _ in range(n)
]

# 벌칙을 받은 학생
students = [
    int(input())
    for _ in range(m)
]

for elem in students :
    counter[elem-1] += 1


chker = False

for element in counter :
    if element == k :
        print(counter[element + 1])
        chker = False
        break
    chker = True

if chker :
    print(-1)