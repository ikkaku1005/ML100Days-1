#範例
import matplotlib.pyplot as plt
import numpy as np
#畫一個sin波 從0~180度
x = np.arange(0,180) 
y = np.sin(x * np.pi/180.0) #x * np.pi/180.0 轉成弧度  1度 = pi/180 弧度
# 設定要畫的的x,y數據list....
plt.plot(x,y)
plt.show() #呼叫


import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,180)
y = np.sin(x * np.pi / 180.0)
plt.plot(x,y)
#設定x、y的邊界範圍 ，不設的話，系統會自行決定
plt.xlim(-30,390)
plt.ylim(-1.5,1.5)
# 照需要寫入x 軸和y軸的 label 以及title
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("The Title")
plt.show()

#散點圖: Scatter Plots
#顏色由（X，Y）的角度給出。
#注意標記的大小，顏色和透明度。
X = np.random.normal(0, 1, 100)
Y = np.random.normal(0, 1, 100)
#loc：float，此概率分佈的均值（對應著整個分佈的中心centre）
#scale：float，此概率分佈的標準差（對應於分佈的寬度，scale越大越矮胖，scale越小，越瘦高）
#size：int or tuple of ints，輸出的shape，預設為None，只輸出一個值
plt.scatter(X,Y)
plt.title("Scatter plot")
n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
plt.scatter(X,Y)
plt.show()

#給定顏色與圖形形狀

t = np.arange(0., 10., 0.7) # 產出數值介於0~10的array，並以0.7為間隔，
#t: [0.  0.7 1.4 2.1 2.8 3.5 4.2 4.9 5.6 6.3 7.  7.7 8.4 9.1 9.8]
plt.plot(t, t, 'r--', t, t**2, 'bs', t**3, 'g^')
# 畫出y=x, r 代表紅色、兩個-代表虛線，
# y=x², b代表藍色、s代表方塊
# y=x³ 的圖表， g代表綠色，^代表三角形
plt.show()

x = np.arange(0., 10., 0.7)
y = np.arange(0., 10., 0.7)
plt.bar(x,y)
plt.show()
