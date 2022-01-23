string = input()

first_half = string[:string.find('h') + 1]
second_half = string[string.rfind('h'):]
reverse = string[string.find('h') + 1: string.rfind('h'):]

new_string = first_half + reverse[::-1] + second_half
print(new_string)
