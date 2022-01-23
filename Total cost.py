A = int(input())
B = int(input())
N = int(input())

price = (A * 100 + B) * N

dollars = price // 100
cent = price % 100

print(str(dollars) + " " + str(cent))
