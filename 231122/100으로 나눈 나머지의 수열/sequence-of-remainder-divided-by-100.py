n = int(input())

def fuc(n) :
    if n == 1 :
        return 2
    if n == 2 :
        return 4
    else :
        return (fuc(n-2) * fuc(n-1))%100

print(fuc(n))