fh = input()
mh = input()
sex = input()
if sex == "男":
    print(int((int(fh) + int(mh)) * 0.54))
elif sex == "女":
    print(int(int(fh) * 0.923 + int(mh) / 2))
else:
    print("无对应公式")
