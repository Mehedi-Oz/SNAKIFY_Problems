string = input()

first_half = string[:string.find('h')]
second_half = string[string.rfind('h') + 1:]
new_string = first_half + second_half

print(new_string)
