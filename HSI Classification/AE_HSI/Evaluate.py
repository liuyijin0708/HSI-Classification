# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 15:12:34 2017

@author: Shenjunling
"""

from keras.utils.np_utils import categorical_probas_to_classes
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

#判断f1和总的准确率，输入的Y_test是概率形式的
def modelMetrics(model_fitted,X_test,Y_test):
    Y_predict=model_fitted.predict(X_test)
    if len(Y_predict.shape)!=1:
        #转换onehot编码
        Y_predict=categorical_probas_to_classes(Y_predict)
    report =classification_report(Y_predict, categorical_probas_to_classes(Y_test))#各个类的f1score
    accuracy = accuracy_score(Y_predict, categorical_probas_to_classes(Y_test))#总的准确度
    return report,accuracy

    
def cateAccuracy(model_fitted,X_test,Y_test):
    Y_test = categorical_probas_to_classes(Y_test)
    Y_predict=model_fitted.predict(X_test)
    if len(Y_predict.shape)!=1:
        #转换onehot编码
        Y_predict=categorical_probas_to_classes(Y_predict)
    
    accu_count={}
    accu_total = {}
    for cat in set(Y_test):
        total = list(Y_test).count(cat)
        accu_total[cat] = total
        accu_count[cat] = 0
        
    for iidx,cat in enumerate(Y_test):
        if cat == Y_predict[iidx]:
            accu_count[cat] = accu_count[cat]+1
    sum1 = 0
    sum2 = 0
    for i in range(len(set(Y_test))):
        sum1 = sum1+accu_total[i]
        sum2 = sum2+accu_count[i]
    print(sum2/float(sum1))
    return [accu_count[i]/float(accu_total[i]) for i in range(len(set(Y_test)))]
        


    
