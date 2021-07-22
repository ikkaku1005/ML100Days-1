#NumPy 陣列運算 - 四則運算
#運算的時候，陣列的形狀 (shape) 必須相同，或是遵循廣播 (broadcasting) 規則，才能正確進行 element-wise 運算。規則如下：
#兩個陣列形狀完全相同
#比較兩個陣列的維度，如果維度的形狀相同的話，可以進行廣播
#比較兩個陣列的維度，其中一個維度為1的話，可以進行廣播
#相同大小的陣列運算
#相同大小的陣列運算會符合「對齊」運算的特性：
import numpy as np
a = np.array([20,30,40,50])
b = np.arange(4)
print(b)
print(a+b)
print(a*b)

#常數與陣列運算
#常術與陣列運算會符合「廣播（Broadcast）」運算的特性，廣播特並會將常數補齊成多維的陣列。
print(a-2)
print(a / 10)

#不同大小的陣列運算
#不同大小的陣列運算也會符合「廣播」運算的特性：
data = np.array([[1,2],[3,4],[5,6]])
ones_row = np.array([[1,1]])
print(data + ones_row) #row列
# array([[2, 3],
#        [4, 5],
#        [6, 7]])

#陣列運算與容器運算的差異
#陣列有「對齊」跟「廣播」兩種重要的運算特性，這個其實就是我們講的向量運算特性。換句話說，在向量的運算中，是以「整組」為單位在進行運算，這是和 Python 容器最大的差異之一。
#以「所有元素 +1」這個例子來看，兩種截然不同的做法：
#method1
a = np.array([20,30,40,50])
print(a+1)
#method2
a = [20,30,40,50]
b = []
for i in a:
    b.append(i+1)
print(b)

#用於陣列的矩陣運算
#在 NumPy 中的二維陣列支援了許多的矩陣算法：
a = np.array([[1.0, 2.0],[3.0, 4.0]])
print(a)
y = np.array([[5.],[7.]])
print(y)
print("轉置矩陣:",a.transpose()) #轉至矩陣 :行列互換
print("逆矩陣:",np.linalg.inv(a))
print(np.trace(y)) #np.trace() 會回傳 array 的對角線數值總和且這個 array 必須是 2 維以上
#a = np.array([[1.0, 2.0], [3.0, 4.0]])
# [[1. 2.]
#  [3. 4.]]    所以np.trace(a) >>> 5.0 (= 左上的 1 + 右下的 4)
np.trace(a)
# 5.0 (= 左上的 1 + 右下的 4)
print(np.linalg.solve(a,y))  #函數用於求解線性矩陣方程或線性標量方程組。 Solve（）函數計算矩陣方程ax = b的精確x，其中a和b為矩陣。

#NumPy 陣列運算 – 次方 np.power()
a  = np.array([1,4,6])
print(np.power(a,2))
#NumPy 陣列運算 – 平方根 np.sqrt()
#基本語法: np.sqrt(a)，對陣列進行 element-wise 的平方根。
print(np.sqrt(4))
print(np.sqrt(a))
#NumPy 陣列運算 – 歐拉數 (Euler's number) 及指數函式 np.exp()
#NumPy 提供歐拉常數 e (np.e)，以及指數函式 np.exp()，表示 ex。
print(np.e)
print(np.exp(1))
print(np.exp(np.arange(5)))
#NumPy 陣列運算 – 對數函式
print(np.log(2)) #底數為e  ln(2)
print(np.log2(4)) #底數為2
print(np.log10(100)) #底數為100
print(np.log1p(2))  #底數為e，計算log(1+x)
#使用其他底數:
print(np.log(9)/np.log(3))
#若是 log(負數) 則會產生 nan 常數，NaN / NAN 為 nan (not a number) 的別名。
#NumPy 陣列運算 – 取近似值.
#

#NumPy 陣列運算 – 取近似值
a = np.array([1.4354, 5.65])
print(np.round(a,decimals=0))  #四捨，五取最近偶數
print(np.rint(a)) #round至最近整數
print(np.trunc(a))  #無條件捨去小數
print(np.floor(a)) #向下取整
print(np.ceil(a)) #向上取整

#NumPy 陣列運算 – 取絕對值：np.abs(), np.absolute(), np.fabs()
#np.abs() 是 np.absolute() 的簡寫，兩者完全相同；np.fabs() 的差異在於無法處理複數 (Complex)。
#如果傳入複數至 fabs() 的話則會產生錯誤。
