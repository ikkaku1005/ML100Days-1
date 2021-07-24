#D8：Pandas 物件的定義與屬性 (3/19更新)
#函式與函式庫
#函式庫是由一堆函式所組成的集合，又稱為是模組、套件或是大陸用語包、模塊等詞。而函式是指一段程式碼的片段封裝而成的函式，可以用於重複呼叫。
#Pandas 的發展史
#Pandas 是一個開源的（BSD 協議許可的函式庫），為 Python 提供高性能的數據結構和數據分析工具。 Pandas 是由 NumFOCUS 組織所贊助，確保其在開源界的地位。
#andas 的重要特性
#提供了快速高效的 DataFrame 結構（底層使用 Cython 或 C 的實作對效能進行高度優化）
#廣泛地在學術傑與商業領域中使用，包括金融，神經科學，經濟學，統計學，廣告，Web分析等。
#對於資料格式有高度的銜接性，包含 CSV、Excel 或資料庫（SQL）皆能提供彈性的讀寫工具
#在程式中載入 Pandas
#不管是在 .py 或是 Jupyter 的環境，都可以利用 import 的方法載入 pandas 函式庫，一般習慣命名成 pd：
import pandas as pd
print(pd)
print(pd.__version__)

#ataFrame and Series
#Pandas 最重要的貢獻是提出了兩種資料結構：「DataFrame」和「Series」。Series 是一種一維的資料結構，用來一定序列型的資料。DataFrame 是二維的資料結構，用表格的形式存放常見的資料內容。
s = pd.Series([1,2,3])
print(s)
print(type(s)) #type() 判斷型別
print("=================================")
df = pd.DataFrame([1,2,3])
print(df)
#     0
# 0  1
# 1  2
# 2  3
print(type(df))

#Series 的常用屬性
#Series 其實就是 NumPy 的 Array 的加工品，所以 Array 有的屬性， Series 絕大部分都可延用：
s = pd.Series([1,2,3])
print(s.shape)  #(3,)
print(s.size)  #3
print(s.dtype)

#DataFrame 的常用屬性
#DataFrame 也是 NumPy 的 Array 的加工品，所以 Array 有的屬性， DataFrame 一樣可以使用用：
df = pd.DataFrame([1, 2, 3])
print(df.shape) # (3, 1)
print(df.size) # 3
print(df.dtypes) 

#Pandas 中的資料型態
#Pandas 大部分沿用 NumPy 定義的型態，只是沒有那麼嚴格。除此之外， Pandas 新增了兩種在資料分析時常用的型態「timedelta」和「category」。
#Seies、DataFrame 與 NdArray 的比較
#DataFrame 代表的是用「資料」的角度去思考程式中的實踐應該長什麼樣子、應該要提供哪些方法，是以資料的觀點出發。
#那你可以會問既然 Seies、DataFrame 都是由陣列所封裝而成的加工品，那為什麼不直接用陣列就好呢？陣列當中所有資料型態必須相同，而 DataFrame 是由  Seies 所組成，也就說同一個欄位形態相同，欄位與欄位間可不相同。
