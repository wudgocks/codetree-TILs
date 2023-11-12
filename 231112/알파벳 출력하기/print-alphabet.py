n = int(input())

target_chr = 'A'
for i in range(n) :
    for j in range(i + 1) :
        print(target_chr, end = "")
        target_chr = chr(ord(target_chr) + 1)
    print()