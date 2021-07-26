#陣列中的比較運算
#在 NumPy 陣列中也有比較運算，一樣會符合「對齊」與「廣播」的特性：
import numpy as np
a = np.array([20,30,40,50])
b = np.array(4)
print(a > b )   #[ True  True  True  True]
print(a < b)  #[False False False False]
print( a == b)  #[False False False False]
print(a != b) #[ True  True  True  True]

#陣列中的邏輯運算 : and or not
#需要特別注意的是，在 NumPy 陣列中沒有邏輯運算，可以使用位元運算或是邏輯運算的函式方法取代：
a = np.array([True, True, False, False])
b = np.array([True, False, True, False] )
#print(a and b) 
#Traceback (most recent call last):
#ValueError: The truth value of an array with more than one element is 
#ambiguous. Use a.any() or a.all()

print(a & b)  #[ True False False False]
print(a | b) #[ True  True  True False]
#邏輯運算與比較運算都會產生一組有布林所組成的陣列：
#若要理解這個，必須知道 python 的邏輯是依照數學邏輯 (true false) 處理的，底下舉出最簡單的例子:
#「且」(全都為真才為真，否則為否)的部分:
##false 且 false = false
#flase 且 true = false
#true 且 true = true
#「或」(至少有一個真即真，否則為否)的部分:
#false 或 false = false
#false 或 true = true
#true 或 true = true
#回到上面的問題:
#若 a 與 b 都是邏輯值(true false)，則 &、| 跟 and、or 沒什麼差別 (所以可以看到輸出符合預期，可以用我上面提到的運算規則去對照圖片中的結果)，那本問題基本上就解決，但若要再探討 & 與 | ，就繼續往下看吧。
#若 a 與 b是數值 ，例如 a=2, b=4，則 & 、 | 會把 a 與 b 轉為二進制 (a = 10，b=100)，在二進制中 1 代表 true、0 代表 false，所以
#a&b=0 (從最右邊開始加，0&0=false&false=false=0，再來右邊數來第二個，1&0=true&fasle=false=0，再往左一個位數發現 a 少一個數字那就忽略不動作，算出的二進位數值再轉為十進位制作為回傳值)
#a|b=6 (作為練習)


#利用布林值作為篩選的條件：遮罩
#可以用一組 True/False 做為每一個位置的篩選條件，這種方法稱為遮罩（Mask）：
a = np.array([10,20,30,40])
print(a[[True, True, True, True]])
#[10 20 30 40]
print(a[[True, False, True, False]])
#[10 30]
print(a[[False, False, False, False]])
#[]

#從比較/邏輯運算到遮罩特性
#我們可以把比較/邏輯運算所產生的布林陣列作為遮罩的條件，可以一次從陣列中挑選出滿足條件的元素：
a = np.array([10,20,30,40])
print(a > 20) #a > 20作為遮罩的條件
#[False False  True  True
print(a[[False, False, True, True]])
#[30 40]
print(a[a > 20]) #找出大於20的元素
#[30 40]

#遮罩特性背後的強大之處
#「遮罩」是陣列當中最重要的特性之一，用於篩選出符合條件的元素。以「找出 >3 的元素」這個例子來看，兩種截然不同的做法：
a = np.arange(4)
print(a [ a > 1])
a = np.arange(4)
b = []
for i in a:
    if i > 1:
        b.append(i)
print(b)
#綜合這兩天的介紹，我們可以知道在陣列算符合「對齊」、「廣播」以及「遮罩」三個特性。這三種特性都符合矩陣以整組為單位的運算，而非一個一個元素做比較。這也是陣列和容器最大的差別。

#補充：any() 和 all()
#除了用邏輯跟比較運算產生由 True 或 False 組成布林陣列之外，還有一些常用的方法可以用：
#any:對所有元素做運算，存在True則返回True
print(np.any([True, True, True])) # True
print(np.any([True, False, False])) # True
print(np.any([False, False, False])) # False
#all:對所有元素做運算，所有為True則返回True
print(np.all([True, True, True])) # True
print(np.all([True, False, False])) # False
print(np.all([False, False, False])) # False

#陣列的比較與陣列元素的比較
#陣列的比較指的是兩個變數之間的比較，會是一個布林的結果；而陣列元素的比較是指陣列中的元素兩兩對齊比較，會回傳一組布林的結果
#numpy.nan 與 numpy.NAN 都是 NumPy 常數，代表 Not a Number，不過在官方文件中建議統一使用小寫的 nan。
#判斷無限數的函式有 isinf()、isposinf()、isneginf()，分別用來判斷判斷陣列元素是否為正無限數或負無限數、是否為正無限數、是否為負無限數。
#isnat() 的 nat (NaT) 是 not a time 的意思，用來判別陣列元素是否為日期時間。若非日期時間 (包括 datetime 或 timedelta) 的話回傳 True，若是的話則回傳 False。

#NumPy 陣列邏輯函式 - 陣列比較
#使用 np.array_equal()、np.array_equiv() 比較 2 個陣列是否相同。
#兩個函式不同之處在於 array_equal() 需要形狀完全一樣且元素值皆相同才為 True。

#NumPy 陣列邏輯函式 - 邏輯操作
#邏輯比較函式都是 element-wise，比較 2 個陣列元素。如果 2 個陣列的形狀不同的話，必須符合廣播 (broadcasting) 規則。

#NumPy 陣列邏輯函式 - Truth值測試
#使用 np.all()  進行 Truth 值測試
print(np.all([-1,4,0]))  #False
#使用 np.any() 進行 Truth 值測試
print(np.any([[True, False],[False, False]], axis = 0))
#[ True False]
#可以依軸 (axis) 進行比較，兩個函式不同的地方在於 np.all() 是 AND 邏輯的比較，而 np.any() 是 OR 邏輯的比較。
#以下的值均認定為非 0，也就是屬於 True：True、NaN、正無限值、負無限值。


