str1, str2 = map(str,input().split())

len1 = len(str1)
len2 = len(str2)

if len1 > len2 :
    print(str1, len1)
elif len2 > len1 :
    print(str2, len2)
else :
    print("same")