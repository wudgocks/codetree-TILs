n = int(input())

def function(n) :
    if n == 0 :
        return
    else :
        function(n-1)
        print("*" * n) 
        
function(n)