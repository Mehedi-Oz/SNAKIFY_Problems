n = int(input())
data_list = []
distinct = []

for i in range(0, n):
    data = input()
    data_list.append(data)

print(len(data_list))

for i in data_list:
    if i not in distinct:
        distinct.append(i)

print(len(distinct))
print(len(data_list) - len(distinct))
