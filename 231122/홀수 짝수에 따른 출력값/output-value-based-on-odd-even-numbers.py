n = int(input())

def fuction (n) :
    if n == 1 :
        return 1
    if n == 2 :
        return 2
    return fuction(n-2) + n
            
print(fuction(n))