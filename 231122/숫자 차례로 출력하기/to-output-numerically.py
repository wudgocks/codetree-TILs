n = int(input())

def function1(n) :
    if n == 0 :
        return
    else :
        function1(n-1)
        print(n, end = " ")

def function2 (n) :
    if n == 0 :
        return
    else :
        print(n, end = " ")
        function2(n-1)

function1(n)
print()
function2(n)