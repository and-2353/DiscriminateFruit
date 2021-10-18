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
        return X_std

def lda(X, y):
    clf = LDA()
    clf.fit(X, y)

    print(clf.predict(X))
    print(clf.score(X, y))
    print(clf.coef_)


def loo(X, y):
    clf = LDA()
    loo = LeaveOneOut()
    scores = cross_validate(clf, X, y, cv=loo)

    print(scores)
    print(scores['test_score'].mean())


def main(Standardization_flag=1):
    data = pd.read_csv('RGBValue_cutdata.csv', encoding='utf-8', header=0)

    X = data.drop('Label', axis=1)
    y = data['Label']

    if Standardization_flag:
        X = Standardization(X)
        print('X is Standardized')
    print(X)
    lda(X, y) # 判別的中率0.85 (train_data=test_data)
    loo(X, y) # 判別的中率0.8


if __name__ == '__main__':
    Standardization_flag = 1 # 標準化する:1, 標準化しない:0
    main(Standardization_flag=Standardization_flag)