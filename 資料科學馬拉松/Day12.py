#D12：Pandas 迭代與重複操作
#DataFrame 當中的 For Loop
#當你對一個 DataFrame 進行迴圈（Loop）操作，你預期結果會是什麼嗎？
import pandas as pd
df = pd.DataFrame({
    "name":["Alice","Bob"],
    "age":[20,32]
})
print(df)
#    name  age
#0  Alice   20
#1    Bob   32
for c in df:
    print(c) #依序print出key
print("==============")
#橫向的資料迭代
#如果我們想要對以「筆」為單位的資料迭代的話，最暴力的方法可以這樣做：
import pandas as pd

df = pd.DataFrame({
  'name': ['Alice', 'Bob'],
  'age': [20, 32]
})
for i in range(len(df)):
    print(i)
    print(df.iloc[i])  #是用index位置來取我們要的資料。
#0
#name    Alice
#age        20
#Name: 0, dtype: object
#1
#name    Bob
#age      32
#Name: 1, dtype: object

#iteritems()、iterrows()、itertuples()
#第二種方法可以直接用 DataFrame 內建的 iterative 方法：
for d in df.iteritems():
    print(d)
#('name', 0  Alice 1 Bob Name: name, dtype: object)
#('age', 0  20 1  32 Name: age, dtype: int64)0
for d in df.iterrows():
    print(d)
#(0, name Alice age 20 Name: 0, dtype: object)
#(1, name Bob age  32 Name: 1, dtype: object)
for d in df.itertuples():
    print(d)
#Pandas(Index=0, name='Alice', age=20)
#Pandas(Index=1, name='Bob', age=32)

#apply
#第三種方法是使用 Pandas 當中的 apply 方法，apply 是一種用於逐行或逐列的循環處理方法，常搭配 lambda 匿名函式一起使用：
import numpy as np
import pandas as pd
df = pd.DataFrame({
  'score': [98, 67, 85],
  'age': [20, 32, 28]
})
print(df.apply(np.max)) # 逐列挑出最大值
#score    98
#age      32
#dtype: int64
print(df.apply(np.min)) #逐列挑出最小值
#score    67
#age      20
#dtype: int64
print(df.apply(lambda x: x.max() - x.min()))
# score    31
# age      12
# dtype: int64

#map
#另外一種跟 apply 很像的方法叫做 map：
import numpy as np
import pandas as pd

df = pd.DataFrame({
  'score': [98, 67, 85],
  'age': [20, 32, 28]
})
print(df)
#   score  age
#0     98   20
#1     67   32
#2     85   28
print(df["age"].map(lambda x:-x))
#0   -20
#1   -32
#2   -28
#Name: age, dtype: int64

#applymap
#在 Pandas 當中，有一種同時 apply 和 map 方法稱為 applymap：
import numpy as np
import pandas as pd

df = pd.DataFrame({
  'score': [98, 67, 85],
  'age': [20, 32, 28]
})
print(df.applymap(lambda x: -x))
#   score  age
#0    -98  -20
#1    -67  -32
#2    -85  -28

#Map、 Apply、Applymap
#接著，我們總結一下這三種類似的方法本質上有何差異：
#map：對 series 所有元素作一樣的操作 
#apply：對 series  或 dataframe 逐行或逐列做一樣的操作
#applymap：對 dataframe 所有元素作一樣的操作

#補充：lambda 匿名函式
#Map、 Apply、Applymap 很常搭配 lambda 匿名函式 一起使用，但其實裡面也可以放函式名稱，我們來比較看看：
print(df.apply(lambda x: x.max() - x.min()))
# score    31
# age      12
# dtype: int64
def f(x):
    return x.max() - x.min()
print(df.apply(f))
# score    31
# age      12
# dtype: int64
#補充：lambda 匿名函式是對於 Python 入門者來說比較難的一個坎，很多人會覺得這是一種「炫技」的手法。
