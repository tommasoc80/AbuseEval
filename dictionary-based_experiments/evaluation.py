# -*- coding: utf-8 -*-

"""
evaluation script for the HaSpeeDe 2018 shared task

USAGE: eval.py [reference] [predicted]
"""

import argparse, sys
from pandas_ml import ConfusionMatrix
from sklearn.metrics import precision_recall_fscore_support as score
from sklearn.metrics import classification_report as report
from operator import itemgetter

def preproc(infile):
    y_test = []
    y_gold = []
    
    reader = infile.read().splitlines() 
    for row in reader:
        gold_label_abusive = row.split('\t')[-3].replace('EXP', 'ABU').replace('IMP', 'ABU')
        gold_label_explicit = row.split('\t')[-3]
        dict_pred_binary = row.split('\t')[-2]
        dict_pred_ter = row.split('\t')[-1].replace('O', 'NOTABU')

        #print(gold_label)
        y_gold.append(gold_label_abusive)
#        y_gold.append(gold_label_explicit)
#        y_test.append(dict_pred_ter)
        y_test.append(dict_pred_binary)


    return y_gold, y_test

#def preproc1(infile):
#    y = []
#
#    reader = infile.read().splitlines()
#    for row in reader:
#        print(row)
#        label = row.split('\t')[-1]
#        y.append(label)
#
#    return y



def eval(y_test, y_predicted):    

    print(set(y_test) - set(y_predicted))

    #print(report(y_test, y_predicted))

    precision, recall, fscore, _ = score(y_test, y_predicted)
    print('\n     {0}   {1}'.format("OFF","NOT"))
    print('P: {}'.format(precision))
    print('R: {}'.format(recall))
    print('F: {}'.format(fscore))

    mprecision, mrecall, mfscore, _ = score(y_test, y_predicted, average='macro')
    print('\n MACRO-AVG')
    print('P: {}'.format(mprecision))
    print('R: {}'.format(mrecall))
    print('F: {}'.format(mfscore))
                        
    print('\n CONFUSION MATRIX:')
    print (ConfusionMatrix(y_test, y_predicted))

    
if __name__ == "__main__":
    
    """
    The evalution script assumes all labels (gold and predicted) are in the same file.
    Order of data: id, message, gold lables, predicted labels
    """    
    with open(sys.argv[1], 'r') as tf:
        y_gold, y_predicted = preproc(tf)

    eval(y_gold, y_predicted)
            
      
  