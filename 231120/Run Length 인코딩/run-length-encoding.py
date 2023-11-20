string = input()

encoded = ""

# 첫번째 값을 읽고 초기화
currentChar = string[0]
numChar = 1

for target_char in string[1:] :
    if target_char == currentChar :
        numChar += 1
    else :
        encoded += currentChar
        encoded += str(numChar)

        currentChar = target_char
        numChar = 1

encoded += currentChar
encoded += str(numChar)

print(len(encoded))
print(encoded)