N = int(input())
maxi = N
total = 0

for i in range(N - 1):
    N = int(input())
    total += N

for i in range(maxi):
    maxi += i
    i += N

print(maxi - total)
