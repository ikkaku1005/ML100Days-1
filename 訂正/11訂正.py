import pandas as pd
import numpy as np
data = {
    'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
    'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
    'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data, index=labels)
print(df)
#  animal  age  visits priority
#a    cat  2.5       1      yes
#b    cat  3.0       3      yes
#c  snake  0.5       2       no
#d    dog  NaN       3      yes
#e    dog  5.0       2       no
#f    cat  2.0       3       no
#g  snake  4.5       1       no
#h    cat  NaN       1      yes
#i    dog  7.0       2       no
#j    dog  3.0       1       no

#2.將資料依照 Age 欄位由小到大排序，再依照 visits 欄位由大到小排序
print(df.sort_values(by = ["age"], ascending = True, axis = 0))
a = df.sort_values(by = ["age"], ascending = True, axis = 0)
print(a.sort_values(by = ["visits"], ascending = False, axis = 0))
#  animal  age  visits priority
#c  snake  0.5       2       no
#f    cat  2.0       3       no
#a    cat  2.5       1      yes
#b    cat  3.0       3      yes
#j    dog  3.0       1       no
#g  snake  4.5       1       no
#e    dog  5.0       2       no
#i    dog  7.0       2       no
#d    dog  NaN       3      yes
#h    cat  NaN       1      yes

#  animal  age  visits priority
#f    cat  2.0       3       no
#b    cat  3.0       3      yes
#d    dog  NaN       3      yes
#c  snake  0.5       2       no
#e    dog  5.0       2       no
#i    dog  7.0       2       no
#a    cat  2.5       1      yes
#j    dog  3.0       1       no
#g  snake  4.5       1       no
#h    cat  NaN       1      yes

#2. 一個包含兩個欄位的 DataFrame，將每個數字減去
#1) 該欄位的平均數
#2) 該筆資料平均數
df = pd.DataFrame(np.random.random(size=(5, 3)))
print(df)
#1) 該欄位的平均數
print(df.mean())  #沒有標記就是指對每一欄(axis = 0)做平均數 
print(df - df.mean()) 
#2) 該筆資料平均數  
print(df.sub(df.mean(axis=1) ,axis=0))   #df.sub()代表相減的意思，

print("===========================")
#範例
data = pd.DataFrame([[1,2,3],[4,5,6]])
print(data.mean()) #沒有特別寫就是對每一欄做平均
# 0    1    2 
#2.5  3.5  4.5
print(data.mean(axis = 1)) 
#0    2.0
#1    5.0
print(data.sum().argmax()) #data.sum().argmax()  取得最大值的那一欄
#2  #第二欄總和最大

#3. 承上題，請問：
#1) 哪一比的資料總合最小 2) 哪一欄位的資料總合最小

