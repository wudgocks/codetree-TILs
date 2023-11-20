string = input()
idx = 0
if 'e' in string :
    idx = string.index('e')

print(string[0:idx] + string[idx+1: ])