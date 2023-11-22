n = int(input())

def function(n) :
    if n == 0 :
        return
    else :
        print(n, end = " ")
        function(n-1)
        print(n, end = " ")
        
function(n)