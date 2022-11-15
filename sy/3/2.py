try:
    num = int(input("Enter a number: "))
    print("The 3^number is: ", 3**num)
except ValueError:
    print("输入错误，请输入数字！")
