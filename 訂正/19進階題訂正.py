# 題目 : 將資料夾中boston.csv讀進來，並用圖表分析欄位。
# 1.畫出箱型圖，並判斷哪個欄位的中位數在300~400之間?
# 2.畫出散佈圖 x='NOX', y='DIS' ，並說明這兩欄位有什麼關係?
import pandas as pd
import numpy as np

df = pd.read_csv("boston.csv")
#2. 畫出散佈圖 x='NOX', y='DIS' ，並說明這兩欄位有什麼關係?
df.plot.scatter(x='NOX', y='DIS')  #x、y 座標的scale改變而呈現反比
