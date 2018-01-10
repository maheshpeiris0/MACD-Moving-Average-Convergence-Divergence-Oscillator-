# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 10:34:08 2018

@author: peirmah
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from EMA import Exponential_Moving_Average
style.use('ggplot')

file_path = r'Z:\Tech Smart Beta Project\Python\ML\Technical Models\BP.csv'

df = pd.read_csv(file_path)
df['Date'] = pd.to_datetime(df['Date'])



def Moving_Average_Convergence_Divergence_Indicator(share_price,):
    EMA_12 = Exponential_Moving_Average(share_price,12)
    EMA_26 = Exponential_Moving_Average(share_price,26)
    EMA_12 = pd.to_numeric(EMA_12)
    EMA_26 = pd.to_numeric(EMA_26)
    MACD_Line = EMA_12 -EMA_26
    MACD_Line = pd.DataFrame(MACD_Line)
    Signal_Line = (Exponential_Moving_Average(MACD_Line,9))


    plt.plot(df['Date'],MACD_Line,label ='MACD Line')
    plt.plot(df['Date'],Signal_Line,label ='Signal Line')
    plt.xlabel('Date')
    plt.legend()
    plt.show()
    

    
    


Moving_Average_Convergence_Divergence_Indicator((df['Adj Close']))
#print(df.iloc[:,1])

    
#print(Exponential_Moving_Average(df['Adj Close'],12) )  