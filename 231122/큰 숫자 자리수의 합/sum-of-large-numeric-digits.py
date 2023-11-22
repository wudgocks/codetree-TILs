lst = list(map(int,input().split()))

number = lst[0] * lst[1] * lst[2]

def f(n):
    if n < 10:
        return n

    return f(n // 10) + (n % 10)


print(f(number))