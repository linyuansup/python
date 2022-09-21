month = input()
da = [1, 3, 5, 7, 8, 10, 12]
if month == "2":
    print(28)
elif int(month) in da:
    print(31)
else:
    print(30)
