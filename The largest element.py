data = input().split()
largest = data[0]
index = 0
flag = 0

if len(data) == 1:
    print(data[0], "0")
else:
    for i in range(1, len(data)):
        if int(largest) < int(data[i]):
            largest = data[i]
            index = i

    print(largest, index)
