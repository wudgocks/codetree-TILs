n = int(input())
fsti = 11
fstj = 11
for i in range(fsti, 11+ n * 2, 2) :
    for j in range(fstj, fstj + n * 2,2) :
        print(j, end= " ")
    print()
    fstj += 2