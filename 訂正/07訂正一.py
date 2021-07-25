import numpy as np
#2. 如何從一個陣列中，找出出現頻率最高的數值與位置？
Z = np.random.randint(0,10,50) #(min,max,size)
print(Z)
rint = (np.bincount(Z).argmax())  #np.bincount() 計算每個元素出現的次數
print(rint)
print(np.where(Z == rint)[0]) 
#np.where()能夠返回符合某一條件的下標函數：
#np.where()[0] 表示行的索引；
#Numpy.bincount()這個函數，其實是在閱讀機器學習的程式碼裡常常出現。常用來
#處理類別標籤的向量。
#它原始設計的概念就是類似桶子排序法的基本概念，是一個很有趣的函數，所以也
#特別用它實作一簡單的桶子排序。
#numpy.bincount(x, weights=None, minlength=None)
#1.假設輸入Ｘ＝[0,1,2,2,3,4,4]，那麼產生bins（桶子）的數量為該X最大值４
#再加１＝５，於是我們產生了５個bins（桶子）的排序編號為indx0~indx4，
#可以視為一向量[indx0,indx1,indx2,indx3,indx4]
# 2.接著來看如何放原本的資料到這５的桶子(bins，分別indx0~indx4)
#原本的輸入Ｘ＝[0,1,2,2,3,4,4]裡有＂一個＂資料0，表示要放到indx0桶子的只有一個，
#故indx0=１。
#接著，原本的輸入Ｘ＝[0,1,2,2,3,4,4]裡有＂一個＂資料１，表示要放到indx１桶子的只有
#一個，故indx１=１。
#接著，原本的輸入Ｘ＝[0,1,2,2,3,4,4]裡有＂兩個＂資料２，表示要放到indx２桶子的有
#兩個，故indx１=2。
#依序放完所以桶子，indx3及 indx4桶子，可以得到indx3＝1，indx4=2
#故得到輸出結果為[1,1,2,1,2]即：[indx0=1,indx1=1,indx2=2,indx3=1,indx4=2]
#使用Python語言程式如下：
#EX1：
X=[0,1,2,2,3,4,4]
print(np.bincount(X))
#[1,1,2,1,2]
#0出現1次。1出現1次，2出現2次，3出現1次，4出現2次
#EX2：
X=[0,5,3,2,3,1,4,2,4]
print(np.bincount(X))
#[1,1,2,2,2,1]



#3. 如何利用 list(...) 實現 a.tolist() 的效果？試著用程式實作。
a = np.random.randint(10, size=6) 
print(a.tolist())
print(list(a))
b = np.random.randint(10, size=(3,4)) 
print(b.tolist())
print(list(b))
c = np.random.randint(10, size=(2,3,2)) 
print(c.tolist())
print(list(c))
##進階
def tolist(iterable):
    if type(iterable) != np.ndarray:  # 若 input 的型態不是 numpy array，我們就把 input 原封不動回傳出來
        
        return iterable
    return [ tolist(obj) for obj in iterable] # 若 input 的型態是 numpy array，我們就把該 array 拆開，再次用一樣的邏輯，也就是拆開後的每個元素變成 input
        
print(tolist(a))
print(tolist(b))
print(tolist(c))