#D11：Pandas 中的算術運算特性
#算術運算
#算術運算是指一般數字間的加、減、乘、除或次方等等的運算，
#NumPy 陣列的運算有「對齊」、「廣播」和「遮罩」三種向量的運算特性。
#算術運算
#算術運算是指一般數字間的加、減、乘、除或次方等等的運算， NumPy 陣列的運算有「對齊」、「廣播」和「遮罩」三種向量的運算特性。
import pandas as pd
import numpy as np
df1 = pd.DataFrame([[1,2,3]])
df2 = pd.DataFrame([[1,1,1]])
print(df1 + df2)
#   0  1  2
#0  2  3  4
#當 list 是一維型態時，
#裏頭的每個 element 會代表資料表的每筆資料，
#所以資料表會顯示多個 row 但只會有一個 column；
#而二維型態時，
#內層的 [] 中的每個 element 代表資料表中的每個 column，
#外層的 [] 中的每個 element 代表資料表中的每筆資料（row）

#不同欄位的算術運算
#在 DataFrame 的「對齊」的特性很嚴格，欄位對不上會產生錯誤的結果：
df1 = pd.DataFrame([[1, 2, 3]], columns=['a', 'b', 'c'])
df2 = pd.DataFrame([[1, 1, 1]], columns=['c', 'd', 'e'])
print(df1 + df2)
#    a   b   c  d   e
# 0 NaN NaN  4 NaN NaN   #補充：NaN 是 Not a Number 的縮寫，在程式中泛指無法定義的數值。

#DataFrame 也有廣播的特性
#在 DataFrame 的算術運算也有「廣播」的特性：
#df1 = pd.DataFrame([[1, 2, 3]])
print(df1 + 1)
#    a  b  c
# 0  2  3  4

#DataFrame 和 Array 有點不一樣
#在 DataFrame 的「廣播」的特性也比較嚴格，只有支援常數的廣播：
df = pd.DataFrame([[1, 2, 3]])
print(df)
print(df + 1)
#    0  1  2
# 0  2  3  4
print(df + pd.DataFrame([1]))
#    0   1   2   pandas 對其不到會顯示nan
# 0  2 NaN NaN
a = np.array([[1, 2, 3]])
print(a + 1)
# [[2 3 4]]
print(a + np.array([1]))
# [[2 3 4]]       #numpy 會自動對齊

#比較和邏輯運算
#比較運算是用來判斷數值之間的比較關係，邏輯運算適用於布林值的組合。在 NumPy 當中，我們會利用比較/邏輯運算所產生的布林陣列作為遮罩的條件，從陣列中篩選出滿足條件的元素。

#DataFrame 也有遮罩運算
#DataFrame 也有沿用遮罩的特性，也可以用來做資料篩選：
df = pd.DataFrame([[1, 2, 3],[4,5,6]],index = ["a", "b"] ,columns=["A", "B","C"])
print(df  > 2 )
#        A      B     C
# a  False  False  True
# b   True   True  True
print(df[df > 2 ])
#      A    B  C
# a  NaN  NaN  3
# b  4.0  5.0  6
print(df['A'] > 2)
# a    False
# b     True
# Name: A, dtype: bool
print(df[df['A'] > 2]) #篩選出 True 的 DataFrame 
#    A  B  C
# b  4  5  6

#DataFrame 中的排序
#除了常見的運算之外，在 DataFrame 當中更多了一些資料的操作方法。第一種我們常用的是排序方法：
df = pd.DataFrame({
    'col1': ['A', 'a', 'B', 'b'],
    'col2': [2, 1, 9, 8]
})
print(df)
#  col1  col2
#0    A     2
#1    a     1
#2    B     9
#3    b     8
print(df.sort_values(by = ['col1'])) #df.sort_values() 排序函數 
                                     # by = ['col1] 依據第一列作排序
#  col1  col2
#0    A     2
#2    B     9
#1    a     1
#3    b     8

#、sort_values()函數的具體參數
#用法：
#參數說明
#參數	                    說明
#by	            指定列名(axis=0或'index')或索引值(axis=1或'columns')
#axis	        若axis=0或'index'，則按照指定列中數據大小排序；若axis=1或'columns'，則按照指定索引中數據大小排序，默認axis=0
#ascending	    是否按指定列的數組升序排列，默認為True，即升序排列
#inplace	    是否用排序後的數據集替換原來的數據，默認為False，即不替換
#na_position	{'first','last'}，設定缺失值的顯示位置



#除了常見的運算之外，在 DataFrame 當中更多了一些資料的操作方法。第一種我們常用的是排序方法：
df = pd.DataFrame({
    'col1': ['A', 'a', 'B', 'b'],
    'col2': [2, 1, 9, 8]
})
print(df.sort_values(by = 'col2' , ascending = False))  
#  col1  col2
#2    B     9
#3    b     8
#0    A     2
#1    a     1

#DataFrame 的統計方法 : 見 cupoy 講義

#DataFrame 的字串方法:
#df.str.findall() ：對所有欄位的文字進行 re.findall()
#df.str.replace() ：對所有欄位的文字進行取代
#df.str.contains() ：對所有欄位的文字進行包含子字串的檢查
#df.str.count() ：對所有欄位的文字進行計數操作
#df.str.split() ：對所有欄位的文字進行分割操作

#統計函式 平均值mean() : 見cupoy講義
#今天都以班上學生國文、英文、數學分數的資料(右表)為例子介紹各個統計函數。
#首先是最常使用到的平均值 mean()，pandas 可針對指定欄位算平均值，如果沒指定會對全部欄位算平均值

#統計函式 加總sum() 、個數count()
#加總 : 計算總和，時常用在計算家庭開銷
#個數 : 計算個數，時常用在出遊時的點名
#score_df.count()

#統計函式：中位數median()
#中位數通常使用在有否贏過 50% 的數據，假如薪資中為數為 4 萬，超過 4 萬即為贏過 50% 的人，反之亦然。
#中位數：通過把所有觀察值高低排序後找出正中間的一個作為中位數。 如果觀察值有偶數個，則中位數不唯一，通常取最中間的兩個數值的平均數作爲中位數。
#以利用中位數算出各科中位數，如果今天數學考了 60 分超過了中位數的 58 分，我就可以說我數學贏過了全班一半的同學。

#統計函式：百分位數quantile()
#百分位數使用在觀察數據百分比，最常運用到的是升學分數的百分位數。
#百分位數：將一組數據從小到大排序，並計算相應的累計百分位，則某一百分位所對應數據的值就稱為這一百分位的百分位數。如果百分位數設定在 50% 即為中位數。
#以下計算 75% 的百分位數，如果我今天國文分數為 75分，我可以說我的國文贏過班上 75% 的同學

#統計函式：最大值max()、最小值min()
#最大最小值時常拿觀察極端值，也可以檢視資料的資料最小與最大分佈。
#其中最小值常常拿來當通過門檻，例如：大學入取分數最低幾分。


#統計函式：標準差std()，變異數var()
#標準差：在機率統計中最常使用作為測量一組數值的離散程度之用。一個較大的標準差，代表大部分的數值和其平均值之間差異較大；一個較小的標準差，代表這些數值較接近平均值。
#變異數：為標準差平方
#統計函式：相關係數corr()
#相關係數 : 皮爾遜積矩相關係數（Pearson product-moment correlation coefficient）用於度量兩個變數X和Y之間的相關程度（線性相依）。在自然科學領域中，該係數廣泛用於度量兩個變數之間的線性相依程度。相關係數的值介於 –1 與 +1 之間，即 –1≤r≤+1。其性質如下：
#當 r>0 時，表示兩變數正相關，r<0 時，兩變數為負相關，r=0 時，表示兩變數間無線性相關關係。
#一般可按三級劃分：|r|<0.4 為低度線性相關；0.4≤|r|<0.7 為顯著性相關；0.7≤|r|<1為高度線性相關。

#自訂義的行或列函式應用 apply()
#你有時候可能儲覺得說前面的統計函式不足以表達資料的特性，此時你可以使用 apply 做自定義的函式。
#像是學校最常使用的加分方式為開根號乘以十，例如：我考 49 分加分過後 √49 × 10 ＝ 70，這種方程式沒辦法在統計函式中算出來，需要藉由 apply 中 lambda 的函式達成。
#其中 lambda x 相當於數學式中的 f(x) ＝√x × 10
#df.apply(lambda x : x**(0.5)*10)  ##(lambda x : x**(0.5)*10)  表示f(x) = x^(1/2) * 10
