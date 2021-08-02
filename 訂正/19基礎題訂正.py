#使用亂數、資料集遭做
import matplotlib.pyplot as plt
import numpy as np

#畫一個 cos 波 從0~180度
x = np.arange(0,180)  #0~179
y = np.cos(x *np.pi / 180.0)  #轉成弧度
plt.plot(x,y) #開始畫圖
plt.show() #秀圖

#畫出完整的 sin 圖形
x = np.arange(0, 3*np.pi, 0.1)  #x從0到3pi
y_sin = np.sin(x)
plt.plot(x, y_sin)
plt.show()

#畫出完整 cos 圖形
x = np.arange(0, 3*np.pi, 0.1)
y_cos = np.cos(x)
plt.plot(x , y_cos)
plt.show() 

#散點圖: Scatter Plots
# 顏色由（X，Y）的角度給出。
# 注意標記的大小，顏色和透明度。
n = 1024       #常態分配sample1024個sample
X = np.random.normal(0,1,n) #平均0，標準差1，size = n
Y = np.random.normal(0,1,n)

#每個點的透明度好想不同 ，應該是和xy有關
T = np.arctan2(Y,X) #x、y的角度
# print(T)
# [ 2.16364628 -0.10195237 -0.25978224 ...  1.23805564 -2.42701083
#  -0.13751921]
plt.scatter(X,Y, s = 75, c = T, alpha = .5)
                       #T對應xy每個點的顏色
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)
plt.show()