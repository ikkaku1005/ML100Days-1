# 範例重點
# 如何使用亂數, 資料集來操作
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 3*np.pi , 0.1)  #0.1為間隔
y_sin = np.sin(x)
y_cos = np.cos(x)

#設定subplot大小
plt.subplot(2, 1, 1) #2個row、1個column、第1個位置
plt.plot(x, y_sin)  #畫出
plt.title('Sine')

#設定subplot大小
plt.subplot(2, 1, 2) #2個row、1個column、第2個位置
plt.plot(x, y_cos)
plt.title('Cosine')

plt.show()


# 從 `sklearn` 載入 `datasets`
from sklearn import datasets 
#載入digits
digits = datasets.load_digits()
fig = plt.figure(figsize = (4, 2))# 設定圖形的大小（長、寬）
fig.subplots_adjust(left = 0, right = 1, bottom = 0, top=1, hspace=0.05, wspace=0.05)
#調整子圖的間距  

# 把前 8 個手寫數字顯示在子圖形
for i in range(8):      #2個row、4個column、指定子圖位置  且每個子圖不顯示個度
    ax = fig.add_subplot(2, 4, i + 1, xticks = [], yticks = []) 
    # 在 2 x 4 網格中第 i + 1 個位置繪製子圖形，並且關掉座標軸刻度
    ax.imshow(digits.images[i], cmap = plt.cm.binary) # 顯示圖形，色彩選擇灰階
            #digits.images[i] 是一個數字圖片  cm.binary  color map 是 binaru
    ax.text(0, 7, str(digits.target[i])) # 在左下角標示目標值
    #在subplot寫下文字   str(digits.target[i])寫下要的文字
plt.show()
  

#軸與子圖非常相似
#但是可以將圖放置在圖中的任何位置。因此，如果要在較大的圖中放置較小的圖，則可以使用軸。
import matplotlib.pyplot as plt
#決定最外框  如果要在較大的圖中放置較小的圖 使用.axes()
plt.axes([0.1,0.1,.8,.8]) #0.1, 0.1 軸域原點坐標（從左下角計算的)，.8,.8 長寬
plt.xticks([]), plt.yticks([]) #不顯示座標
plt.text(0.6,0.6, 'axes([0.1,0.1,.8,.8])',ha='center',va='center',size=20,alpha=.5)
#0.6,0.6,字體在axes的位置。寫下文字 'axes([0.1,0.1,.8,.8])'。ha='center' 水平對其   va='center'垂直對其
 
#決定內框  如果要在較大的圖中放置較小的圖 使用.axes()
plt.axes([0.2,0.2,.3,.3])  #0.2, 0.2 軸域原點坐標（從左下角計算的)，.3,.3 長寬
plt.xticks([]), plt.yticks([])
plt.text(0.5,0.5, 'axes([0.2,0.2,.3,.3])',ha='center',va='center',size=16,alpha=.5)
##0.5,0.5自已在axes的位置。寫下文字'axes([0.2,0.2,.3,.3])' 
plt.show()



#等高線圖
#定義函數與回傳的值
def f(x,y): return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)
n = 256       
x = np.linspace(-3,3,n) #起始-3終止3 平分256個value
y = np.linspace(-3,3,n)
X,Y = np.meshgrid(x,y) 
########################################################
#捕充
# x = np.array([1,2,3])
# y = np.array([4,5])
# X,Y = np.meshgrid(x,y) #回傳x , y 組成的座標
# print(X,Y)  #把xy轉成大的matrix表示  #形成6個座標點(14)(24)(34)(15)(25)(35)
# # [[1 2 3] [1 2 3]]  
# # [[4 4 4] [5 5 5]]
# plt.plot(X,Y, color = 'red', marker = '.', linestyle = "")
##################################################################
#contourf 畫出色塊  contour 畫出線條
                    #f(X,Y)回傳位高 z 高
plt.contourf(X, Y, f(X,Y), 8, alpha=.75, cmap='jet')
C = plt.contour(X, Y, f(X,Y), 8, colors='black', linewidth=.5)
plt.show()




# Axes3D
# 3D圖形在資料分析、資料建模、圖形和影像處理等領域中都有著廣泛的應用
# 主要把想要觀察的重點與場景實現兩種交互
#  一種是可以操縱場景從而能夠從不同的角度觀察模型
#  一種是擁有添加與操作修改模型物件的能
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 創建一個3d坐標系
fig = plt.figure()
ax = Axes3D(fig)

# 利用x軸和y軸繪製sin曲線
x = np.linspace(0,1,100) #公差為100的等差級數
y = np.cos(x *2 * np.pi) / 2 +0.5
# 通過zdir = 'z' 將資料繪製在z軸，zs = 0.5 表示z高，則是將資料繪製在z = 0.5的地方
ax.plot(x, y, zs = 0.5, zdir = 'z', color = 'black', label = 'curve in (x, y)')
#畫出的是水平那一條

# 繪製散點數據 （每個顏色20個2D點）在x軸和z軸
colors = ('r', 'g', 'b', 'k')  
np.random.seed(19680801) # 設置隨機函數複現 #使每次執行random.sample都可得到一樣結果

x = np.random.sample(20 * len(colors)) #sample80個數字  #len(colors) : colors tuple長度
y = np.random.sample(20 * len(colors)) 
z = np.random.sample(20 * len(colors))
#得到80個點

#給每個點顏色
c_list = []
for i in colors:   #[i] * 20 有20個element :rrrr..20個 gggg...20個.....共80個顏色
    c_list.extend([i] * 20)  #extend()方法追加序列內容到列表。
#print(c_list)
# ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 
# 'r', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k']

# 繪製散點座標 通過zdir = 'y' 將資料繪製在y為 0 的地方 => x,z平面
ax.scatter(x, y, z, zdir = 'y', c = c_list, label = 'point in (x, z)')

# 設置圖例
ax.legend()
#限制個軸的範圍
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)

# 軸添加標籤
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

