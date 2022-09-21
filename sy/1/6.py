dict1 = {'赵广辉': '13299887777', '特朗普': '814666888', '普京': '522888666', '吴京': '13999887777'}
name = input()
res = dict1.get(name)
if res:
    print("姓名：" + name + "，电话：" + res)
else:
    print("数据不存在")
