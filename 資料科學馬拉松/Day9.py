#D9：使用 Pandas DataFrame 的初始化 
#DataFrame
#DataFrame 是一種二維的資料結構，使用表格的方式儲存資料。我們會把直向的欄位稱為是 Column、橫向的資料稱為是 Row。
#建立 Pandas 物件
#在 NumPy 中有很多種初始化陣列的方法，但是在 Pandas 當中我們都建議「先直接將資料轉換看看」，可以細分成兩種方法：
#1.從原有的物件轉換
#2.從外部資料讀取而來
#Series
#如果資料的樣態是一維的話，例如 ... 。直接採用 pd.Series(...) 進行轉換：
import pandas as pd
s = pd.Series([1,2,3])
print(s)
s = pd.Series([1,2,3],  index=['Amy', 'Bob', 'Tom'])
print(s)

#從 Array 轉換而來
#如果資料的樣態是一維陣列的話，用 pd.DataFrame(...) 進行轉換的話會變成僅有一個欄位的表格：
import pandas as pd
df = pd.DataFrame([1, 2, 3])
print(df)
#    0
# 0  1
# 1  2
# 2  3
df = pd.DataFrame([1, 2, 3], index=['a', 'b', 'c'], columns=['No'])
print(df)
#    No
# a   1
# b   2
# c   3

#如果資料的樣態是二維陣列的話，用 pd.DataFrame(...) 進行轉換的話會變成多個的表格：
df = pd.DataFrame([[1,2,3],[4,5,6]])
print(df)
#    0  1  2
# 0  1  2  3
# 1  4  5  6
df = pd.DataFrame([[1,2,3],[4,5,6]],index = ['a','b'],columns = ['A','B','C'])
print(df)

#其他資料型態來源
#其他資料可能是就建議直接先轉成 DataFrame 再看看：
df = pd.DataFrame({
    'Name':['Alice','Bob'],
    'Age':[18,20]
})
print(df)
df = pd.DataFrame([
  {'Name': 'Alice', 'Age': 18},
  {'Name': 'Bob', 'Age': 20}
])
print(df)
#    Name  Age
#0  Alice   18
#1    Bob   20

#DataFrame 的來源樣態可以很多元
#DataFrame 是由 Series 组成的
#DataFrame 是一種二維的資料結構，其中的欄位是由多個 Series 組成：
df = pd.DataFrame([[1,2,3],[4,5,6]],index = ['a','b'],columns = ['A','B','C'])
print(df)
print(df['B'])
#a    2
#b    5
#Name: B, dtype: int64
print(type(df['B']))


#DataFrame 的常用屬性
#DataFrame 也是 NumPy 的 Array 的加工品，所以 Array 有的屬性， DataFrame 一樣可以使用用：
print(df.size)
print(df.index)
print("欄:",df.columns)
print(df.values)
print(df.head())
print(df.tail())
print(df.describe())
print(df.info())
#特徵工程是事實對應到後續評估分數的轉換
#在程式語法中，特徵工程位於資料彙整之後，以及擬合模型之前
#由於資料包含類別型(文字型)特徵以及數值型特徵，所以最小的特徵工程至少要包含一種類別編碼(範例使用標籤編碼)，以及一種特徵縮放方法(範例使用最小最大化)
