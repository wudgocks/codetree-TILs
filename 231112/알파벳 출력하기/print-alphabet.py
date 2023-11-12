n = int(input())

target_chr = 'A'
for i in range(n) :
    for j in range(i + 1) :
        if ord(target_chr) == ord('Z') + 1 :
            target_chr = 'A'
        print(target_chr, end = "")
        target_chr = chr(ord(target_chr) + 1)
    print()