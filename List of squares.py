data = int(input())
i = 1
j = 1
square = 0
data_list = []

while square <= data:
    j = j * j
    square = j
    if square < data or square == data:
        data_list.append(j)
    i += 1
    j = i
print(*data_list)
