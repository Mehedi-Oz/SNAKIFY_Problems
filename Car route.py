N = int(input())
M = int(input())

days = M / N
days_ = M % N

print(int(days_))

if days_ != 0:
    days += 1

print(int(days))
