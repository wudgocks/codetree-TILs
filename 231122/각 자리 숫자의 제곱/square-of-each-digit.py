n = int(input())

def function(n) :
    if n < 10 :
        return n **2
    
    return function(n//10) + (n%10)**2

print(function(n))