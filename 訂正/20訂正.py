# #軸圖進階
# 但是可以將圖放置在圖中的任何位置。因此，如果要在較大的圖中放置較小的圖，則可以使用軸。
# #特別提醒: tick 刻度線定位器
# 格式正確的刻度線是準備發布的數據的重要組成部分。Matplotlib為滴答提供了一個完全可配置的系統。有刻度線定位器可以指定刻度線應出現的位置，刻度線格式化程序可以為刻度線提供所需的外觀。主刻度線和次刻度線可以相互獨立地定位和格式化。
import matplotlib.pyplot as plt
fig = plt.figure()
# 设置背景色
fig.patch.set_facecolor('black')
#決定底框
plt.axes([0.1,0.1,.5,.5])
#給定刻度, 若不給定值, 圖的周邊無文字
plt.xticks([]), plt.yticks([]) #空白，無刻度顯示
plt.text(0.1,0.1, 'axes([0.1,0.1,.5,.5])',ha='left',va='center',size=16,alpha=.5)
        #0.1,0.1字體在每層框的位置

#決定第二層框
plt.axes([0.3,0.3,.5,.5])
# plt.xticks([0,0.2,0.4,0.6,0.8,1]), plt.yticks([0,0.2,0.4,0.6,0.8,1])  #若不打上會自動顯示刻度
plt.text(0.1,0.1,'axes([0.3,0.3,.5,.5])',ha='left',va='center',size=16,alpha=.5)

#決定第三層框
plt.axes([0.5,0.5,.5,.5])
plt.xticks([0,0.2,0.4,0.6,0.8,1]), plt.yticks([0,0.2,0.4,0.6,0.8,1])
plt.text(0.1,0.1,'axes([0.5,0.5,.5,.5])',ha='left',va='center',size=16,alpha=.5)
        
#決定第四層框
plt.axes([0.7,0.7,.5,.5])
plt.xticks([]), plt.yticks([])  #空白，無刻度顯示
plt.text(0.1,0.1,'axes([0.7,0.7,.5,.5])',ha='left',va='center',size=16,alpha=.5)
plt.show()



#設定bar的圖型
# 問題: 嘗試通過添加紅色條形標籤重現右側的圖形。
import numpy as np
import matplotlib.pyplot as plt

 #配置12 組 Bar
n = 12 
X = np.arange(n)

 #給定數學運算式
Y1 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
Y2 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)

#指定上半部繪製區域, 給定 Bar 顏色, 邊界顏色
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
# +Y 指的是 XY 四象限的第一象限
# -Y 指的是 XY 四象限的第二象限


#在此coding
#指定下半部繪製區域, 給定 Bar 顏色, 邊界顏色
#顏色除了用色標外, 也可以用顏色文字描述, red: 紅色
plt.bar(X, -Y2, facecolor='red', edgecolor='black')


 #設定繪圖圖示區間
for x,y in zip(X,Y1):
    plt.text(x+0.4, y+0.05, '%.2f' % y, ha='center', va= 'bottom')

 #設定Y軸區間
plt.ylim(-1.25,+1.25)
plt.show()


