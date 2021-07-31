#D1：資料介紹與評估資料
#初入資料科學的探索流程
#找到問題 → 初探 → 改進 → 分享 → 練習 → 實戰
#面對問題需要思考的關鍵點
#為什麼這個問題重要
#資料從何而來
#資料的型態是什麼
#回答問題的關鍵指標是什麼

# 統計指標實作範例
## 常見於迴歸問題的評估指標
#* 平均絕對誤差 - Mean Absolute Error (MAE)
#* 平均平方誤差(均方差) - Mean Squared Error (MSE)

## 常見於分類問題的指標
#* Binary Cross Entropy (CE)
## [教學目標]
#1.開始的第一堂課 : 我們先一些機器學習的基礎開始, 需要用到一些 Python 語法 ，如果不熟 Python, 但是至少熟悉過一門語言, 可以從這些範例開始熟悉
#2.所謂評價函數 (Metric), 就是機器學習的計分方式, 範例會展示平均絕對誤差 (MAE) 的寫法
#3.我們來了解意義並寫作一個函數吧!!


# [範例重點]
#1.複習 / 熟悉 Python 載入套件的語法, 了解什麼是代稱 (In[1], Out[1])
#1.了解 Python 如何使用 Numpy 套件, 計算我們所需要的數值與繪圖 (In[2], Out[2], In[3], Out[3])
#3.如何寫作平均絕對誤差 (MAE) 函數 (In[4], Out[4])

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# numpy 常用於數值/陣列運算, pandas 擅長資料格式的調整, matplotlib 擅長繪圖

w = 3
b = 5
x_lin = np.linspace(0, 100, 101) 
# np.linspace(0, 100, 101)是指 0~100 劃分成 101 個刻度(含頭尾), 所也就是 0, 1, 2,...,100 這 101 個數
# 這時候, x_lin 因為要記錄不只一個數, 因為 np.linspace() 傳回的是一個 Array, 所以 x_lin 就變成 Array 了
y = (x_lin + np.random.randn(101) * 5) * w + b # np.random.randn(101) 表示取樣了101次, 型態是 Array
plt.plot(x_lin, y , 'b.' , label = 'data points') ## 這邊就是將 x_lin 以及剛剛算完的 y, 當作座標值, 將101個點在平面上畫出來
# b. : b 就是 blue, 點(.) 就是最小單位的形狀, 詳細可以查 matplotlib 的官方說明
plt.title("Assume we have data points")    
plt.legend(loc = 2)
plt.show()
