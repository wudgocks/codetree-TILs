n,B = map(int,input().split())
digits = []

while True :
    if n < B :
        digits.append(n) 
        break
    
    digits.append(n%B)
    n //= B

for digit in digits[::-1] :
    print(digit, end = "")