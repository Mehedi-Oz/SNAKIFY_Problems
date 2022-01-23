string = str(input())
new_string = ""

for i in range(len(string)):
    if (i % 3 != 0):
        new_string = new_string + string[i]

print(new_string)
