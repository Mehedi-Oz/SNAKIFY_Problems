data_list = []
data = 1
count = 0
i = 0

while data != 0:
    data = int(input())

    if data == 0:
        break
    else:
        data_list.append(data)

length = len(data_list)
maxi = max(data_list)

while i < length:
    if data_list[i] == maxi:
        count += 1

    i += 1

print(count)
