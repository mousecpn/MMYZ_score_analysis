import numpy as np
import pandas as pd
from SingleCov import SingleCov
from ScoreRank import ScoreRank
from CourseFluct import CourseFluct
from courseCov import courseCov
from Data_Setup import Data_Setup
from ScoreLevel import ScoreLevel
from Data_Setup import Data_Input

datList = Data_Input(r'C:\Users\mouse\Desktop\score\training_data_1.xlsx')
dat,dat_matrix = Data_Setup(datList)
SingCov = SingleCov(dat)
rankMat = ScoreRank(dat)
level = ScoreLevel(rankMat,1842)
pt = SingCov[SingCov.id == 1842]
coherence = np.zeros((6,6))
for i in range(1,7):
    for j in range(1,7):
        coherence[i-1,j-1] = courseCov(rankMat.values[i],rankMat.values[j])
coherence = pd.DataFrame(coherence,columns=['语文','数学','英语','物理','化学','生物'],index=['语文','数学','英语','物理','化学','生物'])

var = CourseFluct(1842,datList)

x=1
while(x==1):
    x=1