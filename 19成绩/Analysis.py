# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 22:50:03 2019

@author: mouse
"""

import pandas as pd
import numpy as np
from ScoreRank import ScoreRank
from SingleCov import SingleCov
from Data_Setup import Data_Input
from Data_Setup import Data_Setup
from basicFun import normalize
from DL import train

def Analysis_all(dat,dat_matrix):
    rankdat = ScoreRank(dat)
    rankdat = rankdat[['总分','语文排名','数学排名','英语排名','生物排名','化学排名','物理排名']]
    
    SingCov = SingleCov(dat)
    var = np.var(dat_matrix,axis=2)
    rankdat[["语文波动","数学波动","英语波动","生物波动","化学波动","物理波动"]] = pd.DataFrame(var[:,2:8],columns=["语文波动","数学波动","英语波动","生物波动","化学波动","物理波动"])
    rankdat[['语文相关性','数学相关性','英语相关性','物理相关性','化学相关性','生物相关性']] = pd.DataFrame(SingCov.values[:,0:6],columns=['语文相关性','数学相关性','英语相关性','物理相关性','化学相关性','生物相关性'])
    rankdat[['总分值','语文','数学','英语','物理','化学','生物']] = dat[['总分','语文','数学','英语','物理','化学','生物']]
    preddat = rankdat
    preddat = normalize(preddat)
    preddat['id'] = dat['id']
    rankdat['id'] = dat['id']
    
    return rankdat,preddat

def Analysis_single(idx,preddat,rankdat,model0,model1,pca0,pca1): # 理科
    pred = rankdat[preddat.id==idx]
    predval = preddat[preddat.id==idx].values[:,0:26]
#    pred = Analysis_single(index,preddat,model0,model1,pca0,pca1)
    predval0 = pca0.transform(predval)

    pred_2b = model0.predict(predval0)
    
    predval1 = pca1.transform(predval)
    pred_985 = model1.predict(predval1)
    
    print("你的综合【总分】【语文】【数学】【英语】【生物】【化学】【物理】排名分别为: %d %d %d %d %d %d %d"%(pred['总分'],pred['语文排名'],pred['数学排名'],pred['英语排名'],pred['生物排名'],pred['化学排名'],pred['物理排名']))
    print("六科相对应的波动性为: %d %d %d %d %d %d"%(pred['语文波动'],pred['数学波动'],pred['英语波动'],pred['生物波动'],pred['化学波动'],pred['物理波动']))
    print("六科相对应的相关性为: %d %d %d %d %d %d"%(pred['语文相关性'],pred['数学相关性'],pred['英语相关性'],pred['生物相关性'],pred['化学相关性'],pred['物理相关性']))
#    print("六科相对应的波动性为: %d %d %d %d %d %d"%(pred['语文波动'],pred['数学波动'],pred['英语波动'],pred['生物波动'],pred['化学波动'],pred['物理波动']))
    
    print("考上985大学的概率为 %f"%(pred_985))
    print("考上一本的概率: %f"%(1-pred_2b))

    return pred

if __name__ == '__main__':
    datList = Data_Input(r'train_data_nature.xlsx')
    dat,dat_matrix = Data_Setup(datList)
    dat['id'] = dat['id'].add(190000)
    rankdat,preddat = Analysis_all(dat,dat_matrix)
    
    model0,pca0 = train(0) #理科 二本概率
    model1,pca1 = train(1) #理科 九八五概率
    
    index = 192509 # 19届 班别 学号
    
    pred = Analysis_single(index,preddat,rankdat,model0,model1,pca0,pca1)
#    pt = preddat[preddat.id==index].values[:,0:26]
#    pt = pca.transform(pt)
#    y_pt = model.predict(pt)
#    print(y_pt)
#    