import numpy as np
print(np)  
print(np.__version__) #1.20.1

#建立Numpy array(陣列)
#要用序列數字產生等差一維陣列的話，可以使用 arange()
#與 linspace() 函式，兩者的函式引數很類似，其中結束值為必填，起始值、間隔值非必填。產生的序列數字包含起始值但不包含結束值，也就是 [start, stop) 的表示方式。
#arange()不同於 linspace() 在於對產生的元素可以有更多的控制。
#建立陣列的方式是透過執行 NumPy 函式，依照不同的目的，以下逐一介紹常用來建立陣列的函式。

#NumPy 提供了一個同類型元素的多維容器型態，是一個所有元素（通常是數字）的類型都相同的矩陣類容器，並通過正整數索引。
#NumPy 的數組（陣列）被稱為 NdArray 或簡稱 Array。以下範例提供一個 3x5 的陣列，並且利用 type() 查看其類型。
import numpy as np
a = np.arange(15).reshape(3,5)
print(a)
#array([[0,1,2,3,4],
#       [5,6,7,8,9],
#       [10,11,12,13,14]
# ])
print(type(a)) #<type 'numpy.ndarray'>

#陣列的常用屬性
#NumPy 的數組被稱為 NdArray 或簡稱 Array，提供以下屬性：
#ndarray.ndim: 陣列有多少維度
#ndarray.shape: 每個維度的大小
#ndarray.size:陣列當中有幾個元素
#ndarray.dtype:陣列中的資料型態
#ndarray.itemsize：陣列中每個元素佔用的空間
#ndarray.data:陣列所存在的記憶體位置
print("ndim",a.ndim)
print("shape",a.shape)
print("size",a.size) #陣列當中有幾個元素
print("dtype",a.dtype)
print("itemsize",a.itemsize)
print("data",a.data)

#List 與 Array 的轉換
#NumPy 的陣列與 Python 的 List 轉換可以有下列兩種方法，請思考一下這兩者有什麼差異：
#list(a) 只會把第一層的元素轉換成 List，多層的話只有第一層會轉；
#tolist() 才能達成多層的型態轉換。
list(a)
# [array([0, 1, 2, 3, 4]), array([5, 6, 7, 8, 9]), array([10, 11, 12, 13, 14]
print("list(a)",list(a))
a.tolist()# [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]
print("tolist()",a.tolist())
