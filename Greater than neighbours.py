data = input().split()
j = 0
flag = 0

if len(data) >= 3:
    for i in range(1, len(data) - 1):
        if j == len(data):
            break

        x = int(data[i - 1])
        y = int(data[i + 1])
        middle = int(data[i])

        j += 1

        if middle > x and middle > y:
            flag += 1

print(flag)
