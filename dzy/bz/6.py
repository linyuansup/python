if __name__ == '__main__':
    x = input()
    try:
        x = int(x)
        if x>250:
            print('严重污染')
        elif x>150:
            print('重度污染')
        elif x>115:
            print('中度污染')
        elif x>75:
            print('轻度污染')
        elif x>35:
            print('良')
        else:
            print('优')
    except:
        print('输入数值有误')