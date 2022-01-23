year = int(input())

if year % 400 == 0:
    print('LEAP')
elif year % 4 == 0:
    if year % 100 == 0:
        print('COMMON')
    else:
        print('LEAP')
else:
    print('COMMON')
