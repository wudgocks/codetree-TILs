n = int(input())

def function (n) :
    if n == 1 :
        return 1
    if n == 2 :
        return 2
    else :
        return function(n-1) + function(n//3)

print(function(n))