data = int(input())
value = 1
i = 2

while value != 0:
    value = data % i

    if value == 0:
        print(i)
    i += 1
