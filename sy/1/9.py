data = {'aaa': '123456', 'bbb': '888888', 'ccc': '33333'}
name = input("输入用户名")
res = data.get(name)
if res:
    pwd = input("输入密码")
    if pwd == res:
        print("Success")
    else:
        print("Fail")
else:
    print("Wrong User")
