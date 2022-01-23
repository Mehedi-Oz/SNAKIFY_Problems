data_list = []
data = 1

while data != 0:
    data = int(input())
    if data == 0:
        break
    data_list.append(data)

first_max = max(data_list)
data_list.remove(first_max)

second_max = max(data_list)
print(second_max)
