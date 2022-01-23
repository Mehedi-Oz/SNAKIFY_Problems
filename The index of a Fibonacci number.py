data = int(input())
first, second, next_move = 0, 1, 1
count = 1

while next_move < data:
    next_move = first + second
    count += 1
    first = second
    second = next_move

print(count)