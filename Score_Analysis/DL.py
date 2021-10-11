# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 14:44:53 2018

@author: Ed Song
"""

import numpy as np
import pandas as pd
from Data_Setup import Data_Input
from Data_Setup import Data_Setup
from basicFun import normalize
from ScoreRank import ScoreRank
from keras.models import Sequential
from keras.layers import Dense,Activation,Dropout
from SingleCov import SingleCov
import xlrd

#预测数据提取
datList3 = Data_Input(r'C:\Users\mouse\Desktop\score\train_data_3.xlsx')
dat3,dat_matrix3 = Data_Setup(datList3)
dat3['id'] = dat3['id'].add(180000)

#训练数据提取
datList2 = Data_Input(r'C:\Users\mouse\Desktop\score\train_data_2.xlsx')
Y_label2 = pd.read_excel(r'C:\Users\mouse\Desktop\score\train_data_2_label.xlsx',sheetname=0)
dat2,dat_matrix2 = Data_Setup(datList2)
dat2['id'] = dat2['id'].add(160000)

datList1 = Data_Input(r'C:\Users\mouse\Desktop\score\train_data_1.xlsx')
Y_label1 = pd.read_excel(r'C:\Users\mouse\Desktop\score\train_data_1_label.xlsx',sheetname=0)
dat1,dat_matrix1 = Data_Setup(datList1)
dat1['id'] = dat1['id'].add(170000)

dat = np.concatenate((dat1,dat2),axis=0)
dat = pd.DataFrame(dat,columns=dat1.columns)
dat_matrix = np.concatenate((dat_matrix1,dat_matrix2),axis=0)
Y_label = np.concatenate((Y_label1["九八五"].values,Y_label2["九八五"].values),axis=0)

#数据处理，归一化
var = np.var(dat_matrix,axis=2)
rankdat = ScoreRank(dat)
rankdat = rankdat[['总分','语文排名','数学排名','英语排名','生物排名','化学排名','物理排名']]
SingCov = SingleCov(dat)
rankdat[["语文波动","数学波动","英语波动","生物波动","化学波动","物理波动"]] = pd.DataFrame(var[:,2:8],columns=["语文波动","数学波动","英语波动","生物波动","化学波动","物理波动"])
rankdat[['语文相关性','数学相关性','英语相关性','物理相关性','化学相关性','生物相关性']] = pd.DataFrame(SingCov.values[:,0:6],columns=['语文相关性','数学相关性','英语相关性','物理相关性','化学相关性','生物相关性'])
rankdat[['总分值','语文','数学','英语','物理','化学','生物']] = dat[['总分','语文','数学','英语','物理','化学','生物']]
rankdat = normalize(rankdat)
rankdat['id'] = dat['id']
rankdat['label'] = Y_label

#预测数据处理
var3 = np.var(dat_matrix3,axis=2)
preddat = ScoreRank(dat3)
preddat = preddat[['总分','语文排名','数学排名','英语排名','生物排名','化学排名','物理排名']]
predSingCov = SingleCov(dat3)
preddat[["语文波动","数学波动","英语波动","生物波动","化学波动","物理波动"]] = pd.DataFrame(var3[:,2:8],columns=["语文波动","数学波动","英语波动","生物波动","化学波动","物理波动"])
preddat[['语文相关性','数学相关性','英语相关性','物理相关性','化学相关性','生物相关性']] = pd.DataFrame(predSingCov.values[:,0:6],columns=['语文相关性','数学相关性','英语相关性','物理相关性','化学相关性','生物相关性'])
preddat[['总分值','语文','数学','英语','物理','化学','生物']] = dat3[['总分','语文','数学','英语','物理','化学','生物']]
preddat = normalize(preddat)
preddat['id'] = dat3['id']

# 抽取训练集
rankdat = rankdat.sample(frac=1)
X_train = rankdat.values[0:3500,0:26]
Y_train = rankdat.values[0:3500,27]
X_val = rankdat.values[3500:4086,0:26]
Y_val = rankdat.values[3500:4086,27]

# 实测数据
X_pred = preddat.values[:,0:26]


#训练模型
model=Sequential()
model.add(Dense(30,input_shape=(26,),activation='relu'))
model.add(Dense(30,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(20,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

model.compile(loss='binary_crossentropy',optimizer='rmsprop',metrics=['accuracy'])
model.fit(X_train,Y_train,epochs=200,batch_size=400)
score = model.evaluate(X_val, Y_val, batch_size=508)
print('val score:', score[0])
print('val accuracy:', score[1])

#预测
pt = rankdat[rankdat.id==171935].values[:,0:26]
lk= rankdat[rankdat.id==171807].values[:,0:26]
y_pt = model.predict(pt)
y_lk = model.predict(lk)
cxz = rankdat[rankdat.id==170125].values[:,0:26]
jc= rankdat[rankdat.id==172713].values[:,0:26]
y_jc = model.predict(jc)
y_cxz = model.predict(cxz)
pred = model.predict(X_train)
print(y_jc)
print(y_lk)
print(y_pt)
print(y_cxz)
pred18 = model.predict(X_pred)
pred18 = pd.DataFrame(pred18,columns=['掉到二本概率'])
pred18['id'] = dat3['id']