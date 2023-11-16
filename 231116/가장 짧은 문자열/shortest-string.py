s1 = input()
s2 = input()
s3 = input()

len_arr = []

a = len(s1)
b = len(s2)
c = len(s3)

len_arr.append(a)
len_arr.append(b)
len_arr.append(c)

result = max(len_arr) - min(len_arr)
print(result)