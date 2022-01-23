data_list = []
data = 1
count = 0

while data != 0:
    data = int(input())

    if data == 0:
        break
    if (data % 2) == 0:
        count += 1

print(count)