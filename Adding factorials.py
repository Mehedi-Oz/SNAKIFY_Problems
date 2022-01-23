n = int(input())
multiply = 1
sum = 0

for i in range(1, n + 1):
    for j in range(1, i + 1):
        multiply = j * multiply

    sum += multiply
    multiply = 1

print(sum)
