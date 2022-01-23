from math import ceil

string = input()
length = ceil(len(string) / 2)

first_half = string[:length]
second_half = string[length:]
new_string = second_half + first_half
print(new_string)
