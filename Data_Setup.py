# -*- coding: utf-8 -*-
"""
Created on Wed May 30 21:26:15 2018

@author: mouse
"""


import pandas as pd
import numpy as np

# 输入历年数据，这里用了四年，没有解决循环输入的问题
train_data_0 = pd.read_excel('training_data_1.xlsx',sheetname=0)
train_data_1 = pd.read_excel('training_data_1.xlsx',sheetname=1)
train_data_2 = pd.read_excel('training_data_1.xlsx',sheetname=2)
train_data_3 = pd.read_excel('training_data_1.xlsx',sheetname=3)

#对每一年数据进行学号排序
train_data_1=Sort_by_id(train_data_1);
train_data_1=Sort_by_id(train_data_1);
train_data_2=Sort_by_id(train_data_2);
train_data_3=Sort_by_id(train_data_3);

dat0 = train_data_0.values
dat1 = train_data_1.values
dat2 = train_data_2.values
dat3 = train_data_3.values
count=0
count0=0
count1=0
count2=0
count3=0
dat = np.zeros((3000,10))
for i in range(1,np.max(train_data_0.班别)+1):
    #jnum 这一个班里有多少人
    jnum = np.max(train_data_0[train_data_0.班别==i].座号)
    for j in range(1,jnum+1):
        flag=0
        if (count0 < dat0.shape[0] and dat0[count0,0] == i and dat0[count0,1] == j):
            dat[count] = dat[count] + dat0[count0]
            count0 = count0 + 1
            flag=1
        if (count1 < dat1.shape[0] and dat1[count1,0] == i and dat1[count1,1] == j):
            dat[count] = dat[count] + dat1[count1]
            count1 = count1 + 1
            flag=1
        if (count2 < dat2.shape[0] and dat2[count2,0] == i and dat2[count2,1] == j):
            dat[count] = dat[count] + dat2[count2]
            count2 = count2 + 1
            flag=1
        if (count3 < dat3.shape[0] and dat3[count3,0] == i and dat3[count3,1] == j):
            dat[count] = dat[count] + dat3[count3]
            count3 = count3 + 1
            flag=1
        if flag==1:
            count = count + 1

train_data_0['总分'] = np.sum(train_data_0[['语文','数学','英语','生物','化学','物理']],axis=1)
train_data_1['总分'] = np.sum(train_data_1[['语文','数学','英语','生物','化学','物理']],axis=1)
train_data_2['总分'] = np.sum(train_data_2[['语文','数学','英语','生物','化学','物理']],axis=1)
train_data_3['总分'] = np.sum(train_data_3[['语文','数学','英语','生物','化学','物理']],axis=1)

train_data_0 = train_data_0[train_data_0.总分>100]

train_data = train_data_0.values + train_data_1.values + train_data_2.values + train_data_3.values
train_data = train_data.div(4)

np.zeros(())
def Data_Setup(train_data):
    train_data_1 = pd.read_excel('training_data_1.xlsx',sheetname=0)
    train_data['总分'] = np.sum(train_data[['语文','数学','英语','生物','化学','物理']],axis=1)
    
    return result

