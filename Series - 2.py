A = int(input())
B = int(input())

data = []

if A == B:
    print(A)
elif A < B:
    for i in range(A, B + 1):
        data.append(i)
else:
    for i in range(B, A + 1):
        data.append(i)
    data.reverse()

for i in data:
    print(i)

