n = int(input())

def sum_function (n) :
    if n == 1 :
        return 1
    
    return sum_function(n-1) + n

print(sum_function(n))