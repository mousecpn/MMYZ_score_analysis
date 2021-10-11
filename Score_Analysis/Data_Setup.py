import pandas as pd
import numpy as np
from Sort_by_id import Sort_by_id
import xlrd

"""
@ author：片片
@ function：将四次输入成绩综合
@ 输入：DataFrame类型的四组大考数据，格式为【'班别','座号','语文','数学','英语','物理','化学','生物'】
@ 输出：DataFrame类型的 train_dat，综合了四次大考的成绩，格式为【'语文','数学','英语','物理','化学','生物'，'id','总分'】
        numpy narray类型的 datArrayReg，三维矩阵，规整过的原始数据，格式为【'班别','座号','语文','数学','英语','物理','化学','生物'】

"""
def Data_Setup(datList):

    length = len(datList)
    #对每一年数据进行学号排序
    for i in range(length):
        datList[i]=Sort_by_id(datList[i])

    datArray = {}
    #转换成array类型，0到8取的是班别座号和其他六科成绩
    for i in range(length):
        datArray['dat' + str(i)]=datList[i].values[:,0:8]

    """
    shape0 = np.concatenate([dat0.shape , dat1.shape])
    shape1 = np.concatenate([dat2.shape , dat3.shape])
    shape = np.concatenate([shape0,shape1])
    shape = np.max(shape,axis=0)
    """

    m,n_x = datArray['dat0'].shape
    datArrayReg = np.zeros((m,n_x,length))
    # 规整四个矩阵的格式，再把n个矩阵合并为一个矩阵
    count = np.zeros((1,length))
    for i in range(length):
        datArrayReg[:,0:2,i] = datArray['dat0'][:,0:2]
    for i in range(1,np.max(datList[0].班别)+1):
        #jnum 这一个班里有多少人
        jnum = np.max(datList[0][datList[0].班别==i].座号)
        for j in range(1,jnum+1):
            flag=0
            for k in range(length):
                if count[0,k] < datArray['dat' + str(k)].shape[0] and datArray['dat' + str(k)][int(count[0,k]), 0] == i and datArray['dat' + str(k)][int(count[0,k]), 1] == j:
                    datArrayReg[int(count[0,0]),2:8,k] = datArray['dat' + str(k)][int(count[0,k]),2:8]
                    if k == 0:
                        flag = 1
                    else:
                        count[0, k] = count[0, k] + 1
                if count[0,k] < datArray['dat' + str(k)].shape[0] :
                    if count[0, k] < m and datArray['dat' + str(k)][int(count[0, k]), 1] - j > 50:
                        while datArray['dat' + str(k)][int(count[0, k]), 1] - j != 1:
                            count[0,k] += 1
            if flag == 1:
                count[0,0] = count[0,0] + 1

    train_dat = np.sum(datArrayReg,axis=2)/length
    train_dat = pd.DataFrame(train_dat[:,2:8],columns=['语文','数学','英语','物理','化学','生物'])
    train_dat[['id']] = pd.DataFrame(datList[0].values[:,8],columns=['id'])
    train_dat['总分'] = np.sum(train_dat[['语文','数学','英语','物理','化学','生物']],axis=1)
    
    return train_dat,datArrayReg


'''
@ author    Modernchar
@ function  输入封装
@ param     文件路径
@ input     你的文件
@ output    数据列表 data_matrix
            返回值使用方法： 1. len(data_matrix) 获取全部考试次数
                            2. data_matrix[i-1] 返回第i次考试DataFrame类
'''
def Data_Input(Data_path):
    data = xlrd.open_workbook(Data_path)
    sheet = data.sheets()
    sheet_num = len(sheet) # 数据页数
    data_matrix = []

    for i in range(0,sheet_num):
        temp = pd.read_excel(Data_path,sheetname=i)
        data_matrix.append(temp)

    # print(data_matrix)
    return data_matrix

'''
@ author        ModernChar
@ function      测试列表相关状态
@ input         list类型考试数据
'''
def Data_Attribute(data_matric):
    print("考试总次数：",len(data_matric))
    i =1
    for item in data_matric:
        print("第",i,"次考试：")
        i = i+1
        print("总体情况：",item)
        print("考试总人数：",len(item))

