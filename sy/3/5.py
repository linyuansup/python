try:
    ip = input("Enter IP address: ")
    ip = ip.split(".")
    if len(ip) != 4:
        raise ValueError
    for i in ip:
        if int(i) > 255 or int(i) < 0:
            raise ValueError
    print("Yes")
except:
    print("No")
