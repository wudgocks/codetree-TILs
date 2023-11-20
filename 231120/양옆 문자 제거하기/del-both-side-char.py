string = input()

ary = list(string)

ary.pop(1)
ary.pop(-2)

print(''.join(ary))