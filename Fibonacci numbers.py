data = int(input())
first, second, next_move = 0, 1, 1
i = 0
if data == 0:
    print("0")
else:
    while i <= data:
        if (i == (data - 1)):
            print(next_move)
            break

        next_move = first + second
        first = second
        second = next_move
        i += 1
