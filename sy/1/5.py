ip = input("")
strlist = ip.split('.')
if len(strlist) != 4:
    print("No")
else:
    for stringdata in strlist:
        if int(stringdata) < 0 or int(stringdata) > 255:
            print("No")
            break
    else:
        print("Yes")
