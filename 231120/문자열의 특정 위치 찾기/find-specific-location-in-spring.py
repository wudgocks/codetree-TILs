str1, str2 = map(str,input().split())

if str2 in str1 :
    print(str1.index(str2))
else :
    print('No')