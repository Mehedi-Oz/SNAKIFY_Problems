count = 0
i = 1
maximum = int(input())

while i != -1:
    data = int(input())

    if maximum < data:
        maximum = data
    if data == 0:
        break

print(maximum)
