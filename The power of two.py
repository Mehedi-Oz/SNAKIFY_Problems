data = int(input())
i = 1

while pow(2, i) <= data:
    i += 1

print(i - 1, pow(2, i - 1))
