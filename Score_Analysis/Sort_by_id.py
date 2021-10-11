"""
@ author：片片
@ 功能: 按照学号排序
@ 输入：DataFrame类型的大考数据，格式为【'班别'，'座号'，'语文','数学','英语','生物','化学','物理','总分'】
@ 输出：DataFrame类型，综合了四次大考的成绩，格式为【'班别'，'座号'，'语文','数学','英语','生物','化学','物理'，'id'】
"""

import pandas as pd
def Sort_by_id(dat):
    id = dat[['班别']].values*100 + dat[['座号']].values
    dat[['id']] = pd.DataFrame(id,columns=['id'])
    return dat.sort_values(by='id',ascending= True)