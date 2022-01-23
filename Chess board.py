rows = int(input())
cols = int(input())
arr = []

for i in range(rows):
    col = []
    for j in range(cols):
        if j % 2 == 0:
            col.append('.')
        else:
            col.append('*')
    arr.append(col)

print(*arr, sep=", ")
