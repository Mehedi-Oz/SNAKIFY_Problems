data = input().split()
removed_data = []
flag = 0

for i in data:
    if i not in removed_data:
        removed_data.append(i)

print(len(removed_data))
