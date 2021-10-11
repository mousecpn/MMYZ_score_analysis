"""
@ author：片片
@ 功能: 按照学号排序
@ 输入：Array类型的单科大考数据course1和course2，两数组大小必须一致
@ 输出：float类型，两学科相关性系数
"""

import numpy as np
import pandas as pd

def courseCov(course1,course2):
    E_xy = np.zeros(course1.shape)
    E_xy = course1 * course2
    E_xy = np.mean(E_xy,keepdims=False)
    E_x = np.mean(course1,keepdims=False)
    E_y = np.mean(course2,keepdims=False)
    cov = E_xy - E_x * E_y
    coh = cov/np.sqrt(np.var(course1,keepdims=False)*np.var(course2,keepdims=False))

    return coh