n1, n2 = map(int,input().split())

Aseq = list(input().split())
Bseq = list(input().split())

whole = ''.join(Aseq)
part = ''.join(Bseq)

if part in whole :
    print("Yes")
else :
    print("No")