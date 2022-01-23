data = input().split()
output = []

for i in range(len(data)):
    int_data = int(data[i])

    if int_data % 2 == 0:
        output.append(int_data)

print(*output, sep=" ")