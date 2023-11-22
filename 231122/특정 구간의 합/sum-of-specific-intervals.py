n,m = map(int,input().split())
A = list(map(int,input().split()))

def function(arr) :
    sumArr = []
    a_lst = []
    b_lst = []
    for i in range(m) :
        a,b = map(int,input().split())
        a_lst.append(a)
        b_lst.append(b)

    for i in range(m) :
        sumVal = 0
        for j in range(a_lst[i]-1, b_lst[i]) :
            sumVal += arr[j]
        sumArr.append(sumVal)
    
    return sumArr
       
for element in function(A) :
    print(element)