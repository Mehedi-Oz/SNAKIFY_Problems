first_list = input().split(" ")
second_list = input().split(" ")
count = 0
distinct = []

for i in first_list:
    if i in second_list:
        distinct.append(i)

print(' '.join(list(distinct)))

