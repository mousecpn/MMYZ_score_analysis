"""
@ author：片片
@ 功能: 单科系数函数，计算每一个人每一科的单科系数
@ 输入：DataFrame类型的四组大考数据，格式为【'语文','数学','英语','生物','化学','物理'，'id','总分'】
@ 输出：DataFrame类型的 result，综合了四次大考的成绩，格式为【'语文相关性','数学相关性','英语相关性','生物相关性','化学相关性','物理相关性'】
"""
import pandas as pd
import numpy as np


def SingleCov(train_data):
    temp=train_data[['总分']].rank(method='first', ascending= False)
    train_data[['总分排名']]=temp
    
    temp=train_data[['语文','数学','英语','物理','化学','生物']]
    temp=-temp.values+train_data[['总分']].values
    train_data[['缺语文','缺数学','缺英语','缺物理','缺化学','缺生物']]=pd.DataFrame(temp,columns=['缺语文','缺数学','缺英语','缺生物','缺化学','缺物理'])
    
    temp=train_data[['缺语文']].rank(method='first', ascending= False)
    train_data[['缺语文排名']]=temp
    
    temp=train_data[['缺数学']].rank(method='first', ascending= False)
    train_data[['缺数学排名']]=temp
    
    temp=train_data[['缺英语']].rank(method='first', ascending= False)
    train_data[['缺英语排名']]=temp
    
    temp=train_data[['缺物理']].rank(method='first', ascending= False)
    train_data[['缺物理排名']]=temp
    
    temp=train_data[['缺生物']].rank(method='first', ascending= False)
    train_data[['缺生物排名']]=temp
    
    temp=train_data[['缺化学']].rank(method='first', ascending= False)
    train_data[['缺化学排名']]=temp
    
    temp=train_data[['缺语文排名','缺数学排名','缺英语排名','缺物理排名','缺化学排名','缺生物排名']]
    temp=-temp.values+train_data[['总分排名']].values
    temp = pd.DataFrame(temp,columns=['语文相关性','数学相关性','英语相关性','物理相关性','化学相关性','生物相关性'])
    temp['id'] = train_data[['id']]
    return temp