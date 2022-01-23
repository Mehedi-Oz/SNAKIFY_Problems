data_list = [int(i) for i in input().split()]

for i in range(len(data_list)):
    for j in range(len(data_list)):
        if i != j and data_list[i] == data_list[j]:
            break
    else:
        print(data_list[i], end=" ")
