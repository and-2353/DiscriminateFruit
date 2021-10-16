import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.model_selection import cross_validate
from sklearn.model_selection import LeaveOneOut
from sklearn.preprocessing import StandardScaler

def Standardization(X):
        scaler = StandardScaler()
        scaler.fit_transform(X)
        X_std = pd.DataFrame(scaler.transform(X), columns=X.columns)
        #print(X_std)
        return X_std
    

def main(Standardization_flag):

    data = pd.read_csv('RGBValue.csv', encoding='utf-8', header=None, names=['B', 'G', 'R', 'a_or_o'])
    #print(data)

    X = data.drop('a_or_o', axis=1)
    y = data['a_or_o']

    if Standardization_flag:
        X = Standardization(X)
        print('X is Standardized')
    print(X)
    # クラスタリングもする

    clf = LDA()
    clf.fit(X, y)

    print(clf.predict(X))
    print(clf.score(X, y))
    print(clf.coef_)

if __name__ == '__main__':
    Standardization_flag = 1 # 標準化する:1, 標準化しない:0
    main(Standardization_flag=Standardization_flag)