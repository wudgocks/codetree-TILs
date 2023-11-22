n = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort()

checker = False 

for i in range(n) :
    if A[i] != B[i] :
        checker = False
    else :
        checker = True

if checker :
    print('Yes')
else :
    print('No')