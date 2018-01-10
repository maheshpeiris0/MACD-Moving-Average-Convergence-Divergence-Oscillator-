# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 11:47:21 2018

@author: peirmah
"""
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

file_path = r'Z:\Tech Smart Beta Project\Python\ML\Technical Models\BP.csv'
df = pd.read_csv(file_path)
df['Date']  = pd.to_datetime(df['Date'])

def Exponential_Moving_Average(share_price,window_size):
    multiplier = (2/(window_size+1))
    EMA = []
    for i in range(len(share_price)):
        if (len(EMA)==0) == True:
            EMA.append(share_price.iloc[i])
        else:
            EMA.append(share_price.iloc[i]*(multiplier)+(EMA[i-1])*(1-multiplier))
    return EMA
            

                
#    print(EMA)
#    plt.plot(df['Date'],EMA,label='EMA')
#    plt.plot(df['Date'],share_price,label='Share Price')
#    plt.xlabel('Date')
#    plt.ylabel('USD')
#    plt.legend()
#    plt.show()
    
    

    

        
 
#Exponential_Moving_Average((df['Adj Close']),10)
    
    
    