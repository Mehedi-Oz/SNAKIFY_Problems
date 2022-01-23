first_list = input().split(" ")
second_list = input().split(" ")
data = 0
distinct = []

for i in first_list:
    if i in second_list:
        data = int(i)
        distinct.append(data)

distinct.sort()
print(*distinct)
