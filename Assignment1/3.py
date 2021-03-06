#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 12:42:28 2017

@author: kasperipalkama
"""

from matplotlib import style,pyplot as plt
from matplotlib.ticker import MaxNLocator
import pandas as pd
import numpy as np
import seaborn as sns



def overestimate_debt(debt):
    scale = 2
    df = debt.copy()
    highest_debt = scale*df.ix[2015][' debt in million euros']
    lowest_debt = df.ix[1940][' debt in million euros']
    high_debt_txt = 'Year 2015, Debt: ' + str(int(highest_debt/scale*10**6)) + ' !!!'
    low_debb_txt = 'Year 1940, Debt:'  + str(lowest_debt)+'M'
    
    plt.axis([1930,2200,0,highest_debt+10000])
    plt.xticks([])
    plt.yticks([])
    df.ix[2015][' debt in million euros'] = highest_debt
    print(df.ix[2015][' debt in million euros'])
    plt.annotate(high_debt_txt,xy = (2015,highest_debt))
    plt.annotate(low_debb_txt,xy = (1940,lowest_debt))
    plt.plot(df[' debt in million euros'],'-r',linewidth = 2)
    plt.savefig('results/lying_debt.png')

def underestimate_debt(debt):
    height = (100 - debt.iloc[10:25][' debt / GDP %'])+100
    print(height)
    plt.bar(debt.index.values[10:25],height,
                color = 'g')
    plt.ylabel('debt / GDP %')
    plt.xlabel('Year')
    newYax = [tick for tick in debt.iloc[10:25][' debt / GDP %']]
    plt.axis([2002,2018,142,173.8])
    plt.yticks([150, 159.5 , 173.8],['50','40','30'])  
    plt.savefig('results/lying_against_debt.png')
    

def realistic_debt(debt):
    plt.plot(debt.iloc[0:23][' debt / GDP %'],'go-',label = 'historial data')
    plt.plot(debt.iloc[22:24][' debt / GDP %'],'bo-',label = 'This year')
    plt.plot(debt.iloc[23:26][' debt / GDP %'],'ro-',label = 'prediction')
    plt.xlabel('Year')
    plt.ylabel('debt as a percentage of GDP (%)')
#    plt.axis[[1940,2017,debt.min()[1],debt,max()[1]]]
    ax = plt.gca()
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
#    ax.spines['left'].set_position('zero')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.get_xaxis().get_major_formatter().set_useOffset(False)
    ax.grid(color='grey', linestyle='--',linewidth = 0.2)
#    plt.fill('white')
    plt.rcParams['figure.facecolor'] = 'white'
    plt.box(False)
    plt.legend(loc = 'upper left')
    plt.annotate('financial crisis',xy = (2008,debt.ix[2008][' debt / GDP %']),
                                          xytext =(2008,debt.ix[2008][' debt / GDP %']-5),
                                              arrowprops=dict(facecolor='black',
                                                              shrink=0.05))
    plt.annotate("90's depression",xy = (1995,debt.ix[1995][' debt / GDP %']),
                 xytext =(1995,debt.ix[1995][' debt / GDP %']+4),
                                              arrowprops=dict(facecolor='black',
                                                              shrink=0.05))
    plt.savefig('results/true_debt.png')

def trellis_visualization(wine):
    wine['wine'] = wine['wine'].astype(object)
    data = wine[['alcohol','malic acid','ash','alcalinity of ash','wine']]
    g = sns.PairGrid(data,hue='wine',vars= ['alcohol','malic acid','ash',
    'alcalinity of ash'],aspect=1)
    g.map_offdiag(plt.scatter)
    plt.subplots_adjust(top=0.9)
    g.fig.suptitle('wine trellis, 1 = blue, 2 = red, 3 = purple')
    plt.savefig('results/trellis.png')
    
    
    
if __name__ == "__main__": 
    debt = pd.read_table('input data/debt.txt',sep = ',',
              skiprows = [1,2],header = 0,index_col = 0)
    style.use('ggplot')
    overestimate_debt(debt)
#    underestimate_debt(debt)
#    realistic_debt(debt)
    wine = pd.read_csv('input data/wine.data',header = None)
    wine.columns = ['wine','alcohol','malic acid','ash','alcalinity of ash',
                          'magnesium','total phenols','flavonoids','nonflavonoid phenols',
                          'proanthocyanins','color intensity','hue','OD280/OD315 of diluted wines',
                          'Proline']
#    trellis_visualization(wine)
