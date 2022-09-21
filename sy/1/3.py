per = int(input("输入每学分应缴纳的学费："))
if per <= 0:
    print("？")
else:
    print("学分：17\n学费：" + str(per * 17))
