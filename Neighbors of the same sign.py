data = input().split()
j = 1

for i in range(len(data)):
    if j == len(data):
        break

    x = int(data[i])
    y = int(data[j])
    x_plus = 0

    if x > 0:
        x_plus = x
        x_plus += 1
    elif x < 0:
        x_plus = x
        x_plus -= 1

    j += 1

    if x == y:
        print(x, y)
        break
    elif x < y & y == x_plus:
        print(x, y)
        break
    elif x > y & y == x_plus:
        print(x, y)
        break
