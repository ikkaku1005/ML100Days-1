#D18：Pandas 大型資料處理與效能調校
#效能調校
#大型資料集處理

#效能調校
#大家如果熟悉 pandas 了之後，邏輯都可以做出來的情況下，接下來老闆就會要求你速度要快，也就是快狠準才是 coding 的王道。
#接下來有三個方法帶給大家，可以大幅減少程式的執行時間
#
# 1.讀取資料型態選最快速的
# 2.多使用內建函數
# 3.向量化的資料處理

#資料型態非常多種，在大數據的情況第一關往往都是資料讀取，以下四種資料型態進行實測，可以發現讀取速度以 pkl 檔為最快，是平常讀 csv 的 6 倍速，當然不同環境與不同資料會有所差距，不過資料越多改善會越明顯。
#之後如果遇到讀取資料慢時，不妨使用 pkl 檔讀取看看。

#在使用 agg 和 transform 進行操作時，儘量使用 Python 的內建函式，能夠提高執行效率
#如果非得需要用到自己的函式，那盡量使用 agg 會比 transform 來的快速

#下圖可以看到，採用 isin() 篩選出對應資料室最快的，速度快是因為它採用了向量化的資料處理方式（這裡的 isin() 是其中一種方式，還有其他方式，大家可以嘗試一下） 


##大型資料集處理
# 遇到大資料集時，常有記憶體不足的問題，還有速度上變慢，此時我們可以將欄位的型態降級，不需要存太多元素在一個數字中
# 首先先生成大資料，因為改善部分不同所以分成浮點數 float 與整數 int 的資料集，可以看到不管浮點數還是整數都佔了 800128bytes

# 將整數型態 int 改成 uint 減少記憶體正用空間，使用前 800128bytes，使用後剩下 200128bytes，原因是因為原本有 100 個欄位是 int64，經過 downcast 變成了 100 個欄位的 uint16，因此只用了 1/4 倍左右的空間(int64 uint16 差了 4 倍)

# 將浮點數型態 float64 改成 float32 減少記憶體正用空間，使用前 800128bytes，使用後剩下 400128bytes，原因是因為原本有 100 個欄位是 float64，經過 downcast 變成了 100 個欄位的 float32，因此只用了 1/2 倍左右的空間(float62 🡪 float32 差了 2 倍)


#在這裡介紹3種加速方法針對 Pandas ，在 Python 中還有很多方式可以提升效能
#欄位的型態降級有助於減少記憶體佔用空間
import pandas as pd
import numpy as np 
import time
score_df = pd.DataFrame([[1,50,80,70,'boy',1], 
              [2,60,45,50,'boy',2],
              [3,98,43,55,'boy',1],
              [4,70,69,89,'boy',2],
              [5,56,79,60,'girl',1],
              [6,60,68,55,'girl',2],
              [7,45,70,77,'girl',1],
              [8,55,77,76,'girl',2],
              [9,25,57,60,'girl',1],
              [10,88,40,43,'girl',3],
              [11,25,60,45,'boy',3],
              [12,80,60,23,'boy',3],
              [13,20,90,66,'girl',3],
              [14,50,50,50,'girl',3],
              [15,89,67,77,'girl',3]],columns=['student_id','math_score','english_score','chinese_score','sex','class'])
print(score_df)
#  student_id  math_score  english_score  chinese_score   sex  class
# 0            1          50             80             70   boy      1
# 1            2          60             45             50   boy      2
# 2            3          98             43             55   boy      1
# 3            4          70             69             89   boy      2
# 4            5          56             79             60  girl      1
# 5            6          60             68             55  girl      2
# 6            7          45             70             77  girl      1
# 7            8          55             77             76  girl      2
# 8            9          25             57             60  girl      1
# 9           10          88             40             43  girl      3
# 10          11          25             60             45   boy      3
# 11          12          80             60             23   boy      3
# 12          13          20             90             66  girl      3
# 13          14          50             50             50  girl      3
# 14          15          89             67             77  girl      3
start_time = time.time()
score_df.groupby('class').agg('mean') #agg使用Python的內建函式
end_time = time.time()
print(end_time -start_time)
#0.010003805160522461

start_time = time.time()
score_df.groupby('class').agg(lambda x: x.mean()) ##agg使用自定義函式
end_time = time.time()
print(end_time -start_time)
#0.01590394973754882

star_time = time.time()
score_df.groupby('class').transform('mean') #transform使用Python的內建函式
end_time = time.time()
print(end_time - star_time)
#0.016013383865356445

star_time = time.time() 
score_df.groupby('class').transform(lambda x: x.mean())  ##transform使用自定義函式
end_time = time.time()
print(end_time - star_time)
#0.011001110076904297

# 做到這邊可以看出在使用agg和transform進行操作時，儘量使用Python的內建函式，能夠提高執行效率





#範例
#篩選出對應資料
score_df1 = score_df.copy()
star_time = time.time()
score_df1['Pass_math'] = [i>=60 for i in score_df1.math_score]
end_time = time.time()
print(end_time - star_time)

#用DataFrame column方式搜索
score_df1 = score_df.copy()
star_time = time.time()
score_df1['Pass_math'] = score_df1.math_score>=60
end_time = time.time()
print(end_time - star_time)

# 用自定義式搜索
score_df2 = score_df.copy()
star_time = time.time()
score_df2['Pass_math'] = score_df2.math_score.apply(lambda x : x>=60)
end_time = time.time()
print(end_time - star_time)

#用isin()
score_df3 = score_df.copy()
star_time = time.time()
score_df3['Pass_math'] = score_df3.math_score.isin(range(60, 100))
end_time = time.time()
print(end_time - star_time)


#遇到大資料集時，常有記憶體不足的問題
#首先先生成大資料，因為改善部分不同所以分成浮點數float與整數int的資料集
np.random.randint(3,9,10)

float_data = pd.DataFrame(np.random.uniform(0,5,100000).reshape(1000,100))
int_data = pd.DataFrame(np.random.randint(0,1000,100000).reshape(1000,100))
int_data.memory_usage(deep=True).sum(), float_data.memory_usage(deep=True).sum()

#整數型態int改成uint減少記憶體正用空間，使用前400128bytes，使用後剩下200128bytes
downcast_int = int_data.apply(pd.to_numeric,downcast='unsigned')
int_data.memory_usage(deep=True).sum(),downcast_int.memory_usage(deep=True).sum()


#原本有100個欄位是int32，經過downcast變成了100個欄位的uint16
compare_int = pd.concat([int_data.dtypes,downcast_int.dtypes],axis=1)
compare_int.columns = ['before','after']
compare_int.apply(pd.value_counts)


#浮點數型態float64改成float32減少記憶體正用空間，使用前800128bytes，使用後剩下400128bytes
downcast_float = float_data.apply(pd.to_numeric,downcast='float')
float_data.memory_usage(deep=True).sum(),downcast_float.memory_usage(deep=True).sum()