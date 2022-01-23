data_list = []
data = 1
i, j, count = 0, 1, 1

while data != 0:
    data = input()
    if data == "0":
        break
    data_list.append(data)

while i <= len(data_list):
    if j == len(data_list):
        break

    x = int(data_list[i])
    y = int(data_list[j])

    if x == y:
        count += 1

    j += 1
    i += 1

print(count)
