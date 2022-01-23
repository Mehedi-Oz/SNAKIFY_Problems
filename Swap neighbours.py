data = input().split()
new_data = []
len_data = int(len(data))
print(len_data)

if len_data % 2 == 0:
    divide = len_data % 2
    for i in range(divide):
        x = data[i]
        y = data[i + 1]

        temp = x
        y = x
        x = temp

        new_data.append(y, x)
        i += 2
else:
    last_element = data[len_data - 1]

    divide = (len_data - 1) % 2
    for i in range(divide):
        x = data[i]
        y = data[i + 1]

        temp = x
        y = x
        x = temp

        new_data.append(x, y)
        i += 2

if len_data % 2 == 0:
    print(' '.join(new_data))
else:
    new_data.append(last_element)
    print(' '.join(new_data))
