#NumPy 提供了一個同類型元素的多維容器型態，稱為是數組或陣列。陣列的全名是 N-dimensional Array，習慣簡寫為 NdArray 或 Array。
#一般來說，在 NumPy 當中建立/初始化陣列有四種方法：
#1.從內建型態作轉換
#2.從固定大小的初始值開始
#3.從固定大小的序列值開始
#4.從固定大小的亂數值開始

#1.從內建型態作轉換:
#Python 中內建的容器型態有列表、元祖、字典和集合，可以直接利用 np.array() 方法做型態轉換：
import numpy as np
np.array([1,2,3])
#np.array(...) 更多用法
#來看一下關於 np.array(...) 參數比較細節的用法：
#numpy.array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0, like=None)
#object：必填，任何 array_like 物件
#dtype：指定轉成陣列後的元素型態
#copy：預設為 True，是否產生一個新的物件
#order：指定元素在記憶體中的儲存方式
#會自動轉換成範圍比較大的型態：
x = np.array([1, 2, 3.0])
print(x) ## array([ 1.,  2.,  3.])
#也可以指定成想要的型態：
x = np.array([1, 2, 3], dtype=complex)  # array([ 1.+0.j,  2.+0.j,  3.+0.j])
print(x) #complex :虛數型態
#使用之後會發現，字典型態雖然可以成功被轉成陣列，不過好像不符合我們的預期。
x = np.array({0: 123, 1: 456})   #array({0: 123, 1: 456})
print(x)
#正確的寫法應該寫轉成有序的 List 再作轉換：
x = np.array(list({0:123,1:456}.items())) # array([[  0 123]  [  1 456]])
print(x)

#2.從固定大小的初始值開始
  #第二種方法可以先建立一個固定大小的初始值，例如由 0、1 或特定值所組成的陣列：
x = np.zeros((2,3))
print(x)
x = np.ones((2,3))
print(x)
x = np.full((2,3),9) # 建立由 9 組成的 2x3 陣列
print(x)
  #np.zeros 和 np.empty
  #如果想要產稱一個由 0 所組成的矩陣，可以使用 np.zeors(...) 的方法。除此之外，在文件中有另外一個類似的方法是 np.empty(...)：
x = np.zeros((2,3))
print(x)
x = np.empty((2,3)) #empty的結果唯一非常接近0的數
print(x)
#建立 NumPy array (陣列)
#呼叫 zeros()、ones() 函式，可以依照傳入的形狀引數，建立元素全為 0、全為 1 的陣列。
#使用 empty() 函式則是不需要給定起始值，但是可以建立給定形狀的陣列，元素值則會隨機給定。

#3.從固定大小的序列值開始
  #這個方法可以產生一個特定的序列值，有三種不同的序列：
#(1).固定長度的等差序列
#(2).固定區間的等差序列
#(3).等比序列
x = np.arange(10,30,5) #固定長度的等差序列
print("固定長度的等差序列:",x)
x = np.linspace(0,2,3) #固定區間的等差序列 #3個元素
print("固定區間的等差序列 #3個元素",x)  # array([0. 1. 2.])
x = np.logspace(0,2,3) #等比序列  #3個元素，底數預設為10
print("3個元素的等比序列 ",x)  # array([1. 10. 100.])
x = np.logspace(0,2,3,base = 2) #底數改為2
print(x)

#4.從固定大小的亂數值開始
#另外一種常見的情境是產生一組固定大小的亂數：
from numpy.random import default_rng
rng = default_rng()
x = normal = rng.standard_normal((3,2))
y = random = rng.random((3,2))
z = integers = rng.integers(0,10,size=(3,2))
print(x)
print(y)
print(z)
#我們為什麼習慣從固定大小的陣列開始初始化呢？主要原因是因為陣列的儲存特性，陣列的元素會配置在連續的記憶體位置。每次改動到大小對於記憶體的更動負擔是比較大的，因此希望在一開始就練利一組固定的尺寸避免頻繁改動記憶體。


##NumPy 結構化陣列 (Structured Arrays)
#普通的陣列就是陣列中存放了同一型別的物件。而結構化陣列是指陣列中存放不同物件的格式。
#1.建立結構化陣列可透過 dictionary 型別的資料建立 np.dtype 物件，並指定 dtype 給陣列。
#2.資料型別可以使用 Python 的資料型別、NumPy 的資料型別、或是字母代表的型別皆可。在範例中我們混用了 3 種型別的表示方式
#因為結構化陣列中包含了不同型別的物件，所以每一個物件型別都被稱為一個field。
#每個field都有3部分，分別是：string型別的name，任何有效dtype型別的type，還有一個可選的title。
#從字典建立是這樣的格式： {'names': ..., 'formats': ..., 'offsets': ..., 'titles': ..., 'itemsize': ...}
dt = np.dtype({'names':('Name','num1','num2','True'), 'formats':((np.str_, 5), np.int32 , int,'U3')})
#b = np.genfromtxt('structured.txt', delimiter=',',dtype = dt)
#新建立一個結構化陣列，方式跟建立陣列非常類似。
#下例使用 zeros() 初始化陣列，並指定 dtype。
c = np.zeros(3, dtype = dt)
c = np.array([('',0,0,''),('',0,0,''),('',0,0,'')],
    dtype = [('Name', '<U5'),('num1','<i4'),('num2','<i8'),('True','<U3')])
name = ['Chloe', 'Charlotte','Clara']
num1 = [11,12,13]
num2 = [14,15,16]
check = ['Y','Y','N']

c['Name'] = name
c['num1'] = num1
c['num2' ] = num2 
c['True'] =check
print(c)

#NumPy 結構化陣列：RecordArray
#RecordArray 與 Structured Array 非常類似，但是提供更多的屬性可以用來存取結構化陣列。不過 RecordArray 雖然方便但是在效能上會比原來的陣列差。使用方法如下：
import numpy as np
#Python 中的 list 與 NumPy 中 array 的區别 及相互轉換
a = ([3.234, 34, 3.777, 6.33])
#a為list型別

#將a轉化為numpy中的array:
np.array(a)
print(np.array(a))
