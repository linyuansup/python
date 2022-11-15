total = input("输入年月日：")
year = int(total[:4])
month = int(total[4:6])
day = int(total[6:])
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("闰年\n")
if month == 2:
    print("28 天\n")
elif month in [4, 6, 9, 11]:
    print("30 天\n")
elif month in [1, 3, 5, 7, 8, 10, 12]:
    print("31 天\n")
print(day + "/" + month + "/" + year)
if month <= 1 or month >= 12 or day <= 1 or day >= 31:
    print("输入错误\n")
if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
