data = input()
data_len = len(data)

print(data[2])
print(data[-2])
print(data[0:5])
print(data[0:data_len - 2])
print(data[0::2])
print(data[1::2])
print(data[::-1])

reversed_data = data[::-1]
print(reversed_data[::2])
print(data_len)
