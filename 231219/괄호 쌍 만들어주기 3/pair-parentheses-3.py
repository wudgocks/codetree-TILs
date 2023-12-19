string = list(input())
n = len(string)
counter = 0

for i in range(n) :
    for j in range(i + 1, n) :
        if string[i] == '(' :
            if string[j] == ')' :
                counter += 1

print(counter)