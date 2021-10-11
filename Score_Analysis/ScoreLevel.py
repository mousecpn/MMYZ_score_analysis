import numpy as np
import pandas as pd
def ScoreLevel(rankMat,id):
    numOfStudent = rankMat.shape[0]

    EX = int(numOfStudent * 0.005)
    A_plus = int(numOfStudent * 0.025)
    A = int(numOfStudent * 0.05)
    A_minus = int(numOfStudent * 0.15)
    B_plus = int(numOfStudent * 0.20)
    B = int(numOfStudent * 0.25)
    B_minus = int(numOfStudent * 0.30)
    C_plus = int(numOfStudent * 0.35)
    C = int(numOfStudent * 0.40)
    C_minus = int(numOfStudent * 0.50)
    D = int(numOfStudent * 0.66)
    E = int(numOfStudent * 0.83)

    rank = rankMat[rankMat.id == id].values
    level = []
    for i in range(rank.shape[1] - 1):
        if rank[0,i] < EX:
            level.append("EX") #EX级
        elif rank[0,i] < A_plus and rank[0,i] >= EX:
            level.append("A+")
        elif rank[0,i] < A and rank[0,i] >= A_plus:
            level.append("A")
        elif rank[0,i] < A_minus and rank[0,i] >= A:
            level.append("A-")
        elif rank[0,i] < B_plus and rank[0,i] >= A_minus:
            level.append("B+")
        elif rank[0,i] < B and rank[0,i] >= B_plus:
            level.append("B")
        elif rank[0,i] < B_minus and rank[0,i] >= B:
            level.append("B-")
        elif rank[0,i] < C_plus and rank[0,i] >= B_minus:
            level.append("C+")
        elif rank[0,i] < C and rank[0,i] >= C_plus:
            level.append("C")
        elif rank[0,i] < C_minus and rank[0,i] >= C:
            level.append("C-")
        elif rank[0,i] < D and rank[0,i] >= C_minus:
            level.append("D")
        elif rank[0,i] < E and rank[0,i] >= D:
            level.append("E")
        else:
            level.append("F")


    """
        rank[rankMat.values < EX] = 1  # EX级
        rank[rankMat.values < A_plus and rankMat.values >= EX] = 1  # A+级
        rank[rankMat.values < A and rankMat.values >= A_plus] = 2  # A级
        rank[rankMat.values < A_minus and rankMat.values >= A] = 3  # A-级
        rank[rankMat.values < B_plus and rankMat.values >= A_minus] = 4  # B+级
        rank[rankMat.values < B and rankMat.values >= B_plus] = 5  # B级
        rank[rankMat.values < B_minus and rankMat.values >= B] = 6  # B-级
        rank[rankMat.values < C_plus and rankMat.values >= B_minus] = 7  # C+级
        rank[rankMat.values < C and rankMat.values >= C_plus] = 8  # C级
        rank[rankMat.values < C_minus and rankMat.values >= C] = 9  # C-级
        rank[rankMat.values < D and rankMat.values >= C_minus] = 10  # D级
        rank[rankMat.values < E and rankMat.values >= D] = 11  # E级
        rank[rankMat.values >= E] = 11  # F级
    """

    return level