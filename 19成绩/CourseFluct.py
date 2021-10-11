"""
@ author：片片
@ 功能: 成绩波动性
@ 输入：id是班别*100+学号，datList是list类，里面都是DataFrame类型，四次大考的数据，格式为【'班别','座号'，'语文','数学','英语','生物','化学','物理'，'id'】
@ 输出：波动性，DataFrame类型，格式【'语文波动性','数学波动性','英语波动性','生物波动性','化学波动性','物理波动性'】
"""
import numpy as np
import pandas as pd

def CourseFluct(id,datList):
    l = len(datList)
    dat = np.zeros((l,datList[0].shape[1]))
    for i in range(l):
        dat[i,:] = datList[i][datList[i].id == id].values

    var = np.sqrt(np.var(dat,axis=0,keepdims=True))
    flu = pd.DataFrame(var[:,2:8],columns=['语文波动性','数学波动性','英语波动性','物理波动性','化学波动性','生物波动性'])
    return flu

