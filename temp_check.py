data = input().split()
output = []
j = 1

for i in range(len(data)):
    if j == len(data):
        break

    x = int(data[i])
    y = int(data[j])

    if x < y:
        output.append(data[j])

    j += 1

print(*output, sep=" ")