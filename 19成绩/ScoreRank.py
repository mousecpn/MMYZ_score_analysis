"""
@ author：片片
@ 功能: 成绩级别函数，计算每一个人每一科的成绩级别
@ 输入：DataFrame类型的四组大考数据，格式为【'语文','数学','英语','生物','化学','物理'，'id','总分'】
@ 输出：DataFrame类型的
        rank，格式为【'语文评级','数学评级','英语评级','生物评级','化学评级','物理评级','总分评级'】
        rankMat，格式为【'语文排名','数学排名','英语排名','生物排名','化学排名','物理排名','总分排名','id'】
"""

import numpy as np
import pandas as pd
def ScoreRank(dat):
    temp = dat[['总分']].rank(method='first', ascending=False)
    rankMat = temp

    temp = dat[['语文']].rank(method='first', ascending=False)
    rankMat[['语文排名']] = temp

    temp = dat[['数学']].rank(method='first', ascending=False)
    rankMat[['数学排名']] = temp

    temp = dat[['英语']].rank(method='first', ascending=False)
    rankMat[['英语排名']] = temp

    temp = dat[['生物']].rank(method='first', ascending=False)
    rankMat[['生物排名']] = temp

    temp = dat[['化学']].rank(method='first', ascending=False)
    rankMat[['化学排名']] = temp

    temp = dat[['物理']].rank(method='first', ascending=False)
    rankMat[['物理排名']] = temp
    rankMat[['id']] = dat[['id']]
    return rankMat




