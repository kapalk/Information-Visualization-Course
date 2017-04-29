#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 17:54:09 2017

@author: kasperipalkama
"""

from sklearn.decomposition import PCA
import pandas as pd
from matplotlib import style,pyplot as plt
import numpy as np

def getData(path):
    return pd.read_table(path,sep = ',',header = None)    

def dimReduction(data):
    pca = PCA(n_components=2).fit(data)
    return pca.transform(data)

def scatterPlot(data,party,label,xlabel,ylabel):
    style.use('ggplot')
    plt.figure()
    plt.plot(data[np.where(party == 0)[0],0],
         data[np.where(party == 0)[0],1],'bo',label = label[0])
    plt.plot(data[np.where(party == 1)[0],0],
         data[np.where(party == 1)[0],1],'ro',label = label[1])
    plt.legend(loc = 'best')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig('congress_votes.png')

if __name__ == '__main__':
    votes = getData('input data/congress_votes.dat')
    votes = votes.iloc[:,1:]
    party = getData('input data/congress_party.dat')
    dim_red_votes = dimReduction(votes)
    scatterPlot(data = dim_red_votes,party = party,
                label = ['democrat', 'rebublican'],
                xlabel='PC1', ylabel='PC2')
    