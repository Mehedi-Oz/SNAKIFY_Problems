string = str(input())

for element in string:
    string = string.replace('@', "")

print(string)