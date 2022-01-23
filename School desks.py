first_class = int(input())
second_class = int(input())
third_class = int(input())

desk1 = int(first_class / 2)
total = desk1 * 2
if first_class != total:
    desk1 += 1
total = 0

desk2 = int(second_class / 2)
total = desk2 * 2
if second_class != total:
    desk2 += 1
total = 0

desk3 = int(third_class / 2)
total = desk3 * 2
if third_class != total:
    desk3 += 1

print(desk1 + desk2 + desk3)
