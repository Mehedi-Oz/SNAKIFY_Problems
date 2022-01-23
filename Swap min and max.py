data = input().split()
largest = data[0]
minimum = data[0]
large_index = 0
min_index = 0

for i in range(1, len(data)):
    if int(largest) < int(data[i]):
        largest = data[i]
        large_index = i
    if int(minimum) > int(data[i]):
        minimum = data[i]
        min_index = i

data[min_index] = largest
data[large_index] = minimum

print(*data)
