string = input()

string = string[:1] + 'a' + string[2:-2] + 'a' + string[-1:]

print(string)