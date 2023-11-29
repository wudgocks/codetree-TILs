n1,n2 = map(int,input().split())
lst1 = list(map(int,input().split()))
lst2 = list(map(int,input().split()))

def seq_checker (arr1,arr2,n1,n2) :
    for i in range(n1-n2 + 1) :
        arr = [] 
        for j in range(i,n2+1) :
            arr.append(arr1[j]) 
        
        if arr == arr2 :
            return True
    
    return False

if seq_checker(lst1,lst2,n1,n2) :
    print("Yes")
else :
    print("No")