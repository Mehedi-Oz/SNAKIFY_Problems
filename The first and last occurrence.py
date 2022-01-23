f_string = str(input())

if f_string.count("f") == 2:
    print(f_string.rfind("f"))
elif f_string.count("f") > 2:
    print(f_string.find("f", f_string.find("f") + 1))
elif f_string.count("f") == 1:
    print(-1)
else:
    print(-2)
