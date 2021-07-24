#D7：NumPy 陣列的索引、切片和迭代
#從陣列中存取元素
#從 Python 容器中取出元素的方法有索引（index）跟切片（slice），在 NumPy 的陣列中，也一樣保留了這兩種存取資料的用法。
L = [0,1,8]
print(L)
print(L[-1]) #8
print(L[0])
print(L[1:3])
import numpy as np
a = np.arange(3) **3
print(a)
print(a[-1])
print(a[0])
print(a[1:3])

#一維陣列的切片與索引
#從一維陣列中取出元素的索引跟切片用法：
data = np.array([1,2,3])
print(data[0]) #取出第0個
print(data[1]) #取出第1個
print(data[0:2]) #取出0~1
print(data[1:]) #取出1~最後一個
print(data[-2:]) #取出倒數第2個到最後一個

#一維陣列的的迭代
#如果想要對每個元素作運算的話，我們可以會想到用「迴圈」的方法，對陣列進行迭代：
a = np.arange(3) **3
for i in a:
    print(i)

#多維陣列的切片與索引
#而在多維陣列的資料存取中可以分層存取，也可以用多維座標的方法進行存取：

#多維陣列的多層迴圈
#對於多維陣列如果想要迭代的話，可能就必須要一層一層的迴圈逐步取出資料：
a = np.arange(6).reshape(3,2)
for row in a:
    print(row)
for row in a:
    for d in row:
        print(d)
#攤平後再迭代多維陣列
#因此，實務上我們會建議可以先攤平在進行迴圈的操作：
for d in a.flat:
    print(d)

#np.nditer 迭代物件
#正確的用法會建立改成使用 np.nditer 迭代物件，這樣才可以享有向量運算的特性。
for d in np.nditer(a):  #迭代物件nditer提供了一種靈活訪問一個或者多個數組的方式
    print(d)
#迭代物件的儲存方向
#正確的用法會建立改成使用 np.nditer 迭代物件，這樣才可以享有向量運算的特
for d in np.nditer(a, order='c'): #order= c :列
    print(d)
for d in np.nditer(a, order = 'F'): #order = F :行
    print(d)

#np.nditer 迭代物件
#正確的用法會建立改成使用 np.nditer 迭代物件，這樣才可以享有向量運算的特性。

#NumPy陣列的索引和切片 (Slicing)
#透過索引存取陣列元素或進行切片 (slicing)，可以使用索引值，或是 [start:stop:step] 語法取得範圍內的元素，要留意的是起始-結束範圍仍是 half-open 的，所以回傳的元素將不包含結束索引的元素。
#索引 -1 表示取得最後一個元素。切片如果只有給定 step 值為 -1 的話，則代表是反向取出，元素值是從最後一筆開始取出。
#若沒有給定 start 或 stop 值的話則代表是取出該索引之前或之後的所有元素。若 start 和 stop 值都沒有給定的話，就是取出所有元素值

