class_list = dict()
data = input('Enter name & score separated by ":" ')
temp = data.split(':')
class_list[temp[0]] = int(temp[1])

print(class_list)
