#Numpy 中的資料類型
#NumPy 提供了一個同類型元素的多維容器型態，稱為是數組或陣列。陣列的全名是 N-dimensional Array，習慣簡寫為 NdArray 或 Array。Numpy 的類型系統中，提供以下幾種型態：
#NumPy 的型態與 Python 內建的型態比起來更多細緻（尤其是數字型態），其目的是為了「更好的操作」與「更佳的儲存」。
#dtype 與 itemsize
#ndarray.dtype： 陣列中的資料型態
#ndarray.itemsize： 陣列中每個元素佔用的空間
import numpy as np
a = np.arange(15).reshape(3,5)
print(a)
print(a.dtype) # int32:代表的是 32 個位元長度的 int
print(a.itemsize) # 4:每個元素佔用 4 Bytes。

#numpy 中的型態判斷
#在陣列中如果想要判斷其元素的型態，可能會這麼寫：
print(a.dtype == 'int64') #回傳 a 陣列的型態是否等於 int64 的布林結果

#numpy 中的屬性判斷
# 也可能會想用 is 的方式來做比較：
print(a.dtype is 'int64') 
#或使用 np.int64 表示 int64 型態：
print(a.dtype is np.int64) 

#嘗試過了前兩頁的比較之後，你可能會發現有一些「不如你預期」的結果出現，那究竟背後的邏輯是什麼呢？
#在 NumPy 中有幾種表示型態的方法：
#'int' 字串
#'int64' 字串
#np.int64 物件
#np.dtype('float64') 物件
#實際上，NumPy 型態的定義是一個 np.dtype 的物件，包含「型態名稱」、「表示範圍」及「儲存空間」等等的資訊。而「is」跟「==」的差異在於 is 是強比較，必須要所有規格都相同，包含是哪一種物件；而 == 的比較只會考慮自定義的規則，例如只需要物件的表現形式。
#NumPy 的型態定義成用型態名稱的字串作為表示，因此在使用 == 比較的時候，會可以接受的字串或物件的形式；但使用 is 的話就必須要跟 np.dtype 物件來相比。
print(a.dtype == 'int32') # True
print(a.dtype == np.int32) # True
print(a.dtype is np.dtype('int32')) # True

#另外， int 代表「執行電腦中最大可表示的範圍」，會取決於電腦不同而產生不同的結果：
print(a.dtype == 'int') 
print(a.dtype == np.dtype('int')) 

#NumPy 的型態有些可以縮寫寫成這樣：
dt = np.dtype('i4') # int32
print(dt)


