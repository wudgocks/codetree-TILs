n = int(input())

def fuction (n) :
    sumVal = 0
    if n == 1 :
        return 1
        
    if n == 0 :
        return 2
    return fuction(n-2) + n
            
print(fuction(n))