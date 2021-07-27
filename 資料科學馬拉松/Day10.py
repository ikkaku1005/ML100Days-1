#D10：Pandas DataFrame 的資料選取
#從 DataFrame 選取資料
#資料選取是 DataFrame 最重要的操作之一，仰賴於內部的 index 結構，讓我們得以高效的資料選取。在 DataFrame 當中選取資料有幾種方式：
#1.利用欄位名稱選取單行資料
#2.利用欄位名稱選取多行資料
#3.利用列索引位置選取單列/多列資料
#4.用 loc, iloc, ix 取得行與列
#5.用 iat, at 取得資料
#6.根據條件篩選資料（遮罩）


############  見講義  ###################
#資料過濾、選擇
#資料讀取進來後時常需要過濾要觀察的資料集，與刪除列資料或刪除欄位不同，過濾資料式不會影響到原資料的，只選擇需觀察的資料出來。
#利用[]和.loc[]做布林邏輯選擇資料，回傳為 True 的資料，此方法可以針對欄位的值做過濾，其中.iloc[]可以一併選擇欄位，則[]不行選擇欄位。
#2. 利用.iloc[]針對索引做過濾，也可以一併選擇欄位，不過在這裡不是用欄位名稱選擇而是用欄位
#的位子做選擇。

#合併資料
#串連(concat)
#pandas 的可以將多個物件的資料合成一個新物件。DataFrame 的串連(concat)可以在任何指定的欄位進行結合，如資料對其後出現遺漏值將會填入 NaN。
#以下使用 ETF 元大台灣 50 的資料做為範例，stock_data1 欄位有[date,open,close]，stock_data2 欄位有[date,open,high]，使用 concat 串聯參數 axis=0 縱向結合後發現 stock_data1 不存在 high 欄位，stock_data2 不存在 close 欄位，那麼該位子會被填入 NaN。
#使用concat串聯參數axis=1橫向結合，會以列索引標籤對齊。
#串連(concat)在合併資料時，連結類型預設是外連結(outer join)連集的操作，連結類型可以用 join 參數調整，如 join=’inner’ 表示連結型態為內連結(inner join)交集的操作

#合併(merge)
#合併是藉由找出一或多個行或列索引的吻合值，然後將兩資料結合。
#以下為針對合併欄位 (key)date 做合併，合併方式為 how=’outer’ 外連結，如除了合併欄位 date 之外還有相同欄位名稱，pandas 將會自動把重複欄位名稱加上 '_x' 代表左邊 DataFrame stock_data1 的重複欄位open，加上 '_y' 代表右邊 DataFrame stock_data2 的重複欄位 open。


#pd.merge() 預設連結類型為內連結(inner join)，參數 how 可以更改連結類型，
#inner : 兩資料集的交集
#outer: 兩資料集的聯集
#left   : 只使用左資料的合併欄位(key)
#right : 只使用右資料的合併欄位(key)
#合併的另一種方法.join()，利用兩個 DataFrame 的索引標籤(index)進行連結操作，在這裡要注意，除了 date 是索引標籤(index)以外兩資料還有一個 open 欄位名稱重複，因為 join 不像 merge 會自動對於重複欄位產生字尾，所以需要參數 lsuffix、rsuffix 加上指定字尾。


#利用欄位名稱選取單行資料
#可以使用類似於列表跟字串的索引選取方法，直接使用 [...] 的方式挑選出欄位： 
import pandas as pd
import numpy as np
df = pd.DataFrame([[1,2,3],[4,5,6]], index = ['a','b'], columns = ['A', 'B', 'C'])
print(df['A']) 
print(df['B'])
df = pd.DataFrame(np.random.random(size=(5, 3)))
print(df[0])  #若欄位的名稱非字串，可用數字替代選取第0欄

#利用欄位名稱選取多行資料
#如果被挑選的欄位有多個的話，可以用兩層的方式做選取：
import pandas as pd
df = pd.DataFrame([[1, 2, 3], [4, 5, 6]], index=['a', 'b'], columns=['A', 'B', 'C'])
print(df[['A', 'B']])
print(df[['A', 'C']])
df = pd.DataFrame(np.random.random(size=(5, 3)))
print(df[[0,1,2]])  #若欄位的名稱非字串，可用數字替代，選取第0，1，2欄

#利用列索引位置選取單列/多列資料
#除了利用索引的方式之外，在列表也可以用切片取出部分的元素。在 DataFrame 則可以使用切片的方式選出以列為單位的資料：
df = pd.DataFrame([[1, 2, 3], [4, 5, 6]], index=['a', 'b'], columns=['A', 'B', 'C'])
print(df[0:1]) #選出第一列
#   A  B  C
#a  1  2  3
print(df[0:2]) #選出1、二列
#   A  B  C
#a  1  2  3
#b  4  5  6

#用 loc, iloc, ix 取得行與列
#前面兩種方法可以利用行或列的角度來選取資料，不過一次僅能做一個維度的篩選。為了有效的使用 DataFrame 二維的特性，在 Pandas 當中提供了一種座標選取的方法 .loc[...]：
df = pd.DataFrame([[1, 2, 3], [4, 5, 6]], index=['a', 'b'], columns=['A', 'B', 'C'])
print(df.loc['a','A']) # .loc[列,行]
#1
print(df.loc['a',['A','B']])
#A    1
#B    2
#Name: a, dtype: int64
print(df.loc[['a','b'],'A'])
#a    1
#b    4
#Name: A, dtype: int64
print(df.loc[['a','b'],['A','B']])
#   A  B
#a  1  2
#b  4  5

#類似的方法還有 iloc[...] ，可以索引位置的方法來選出資料：
print(df.iloc[0,0])
#1
print(df.iloc[0,[0,1]])
#A    1
#B    2
#Name: a, dtype: int64
print(df.iloc[[0,1],0])
#a    1
#b    4
#Name: A, dtype: int64
print(df.iloc[[0,1],[0,1]])
#   A  B
#a  1  2
#b  4  5

#
#這邊需要補充一下 .loc[...] 的用法並不是一個函式，.loc 本身其實是一個特殊的物件，搭配 [...] 方式做座標選取。
print(df.loc['a', 'A'])
#print(df.loc)
# <pandas.core.indexing._LocIndexer object at 0x7f236192f770>
print(type(df.loc))
# <class 'pandas.core.indexing._LocIndexer'>

#df.loc('a', 'A')
#Traceback (most recent call last):
#  ...
#TypeError: __call__() takes from 1 to 2 positional arguments but 3 were given


#用 iat, at 取得資料
#如果只是想要選出「數值」資料的話，可以直接用 iat 跟 at 設定座標：
print(df.loc['a','A'])
#1
print(df.iloc[0,1])
#2
print(df.at['a', 'A']) # 1  只選出數值
print(df.iat[0, 1]) #  2  只選出數值

#根據條件篩選資料（遮罩）
#在 DataFrame 當中，也有沿用 NumPy 陣列重要的遮罩用法，可以用它來進行條件的篩選。
print(df > 2)
#       A      B     C
#a  False  False  True
#b   True   True  True
print(df[df > 2])
#      A    B  C
# a  NaN  NaN  3
# b  4.0  5.0  6
print(df['A'] > 2 )  #判斷A欄是否大於二
# a    False
# b     True
# Name: A, dtype: bool
print(df[df['A'] > 2])  #df['A'] > 2 A大於二，把A欄大於二的DataFrame找出

