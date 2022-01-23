string = input()

first_half = string.find('h')
last_half = string.rfind('h')

new_string = string[first_half + 1: last_half]

new_string = new_string.replace('h', 'H')
print(string[:first_half + 1] + new_string + string[last_half:])
