import pandas

if __name__ == '__main__':
    data = pandas.read_csv("C:/Users/93601/Code/python/dzy/bz/zfsj.csv")
    # 去除平方米
    for i in range(len(data['面积(㎡)'])):
        data['面积(㎡)'][i] = data['面积(㎡)'][i][:-2]
    # 转型
    data['面积(㎡)'] = data['面积(㎡)'].astype('float64')
    # 更改单位
    for i in range(len(data['户型'])):
        data['户型'][i].replace('房间', '室').replace('卫', '厅')
    # 重置表格（按行列）
    areacount = data['区域'].value_counts().to_frame().reset_index()
    areacount.columns = ['区域', '小区数量']
    roomcount = data['户型'].value_counts().to_frame().reset_index()
    roomcount.columns = ['户型', '数量']
    # 筛选数据
    roomcountabove = roomcount[roomcount['数量'] > 50]
    print(roomcountabove)
    roomcountabove.to_csv("C:/Users/93601/Code/python/dzy/bz/zfsj4_after.csv")
