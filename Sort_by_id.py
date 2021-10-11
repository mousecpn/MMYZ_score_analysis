# -*- coding: utf-8 -*-
"""
Created on Thu May 31 22:17:43 2018

@author: mouse
"""
import pandas as pd
def Sort_by_id(dat):
    id = dat[['班别']].values*100 + dat[['座号']].values
    dat[['id']] = pd.DataFrame(id,columns=['id'])
    return dat.sort_values(by='id',ascending= True)