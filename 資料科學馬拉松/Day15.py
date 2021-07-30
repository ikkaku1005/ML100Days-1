#D15：用 Pandas 撰寫樞紐分析表
#索引轉欄位、欄位轉索引
#在前天學到畫圖，x 軸為索引(index)，y 軸為欄位(column)，此時 x 軸與 y 軸被索引以及欄位所限制，想畫出各種不同的圖做分析，就必須用到欄位轉索引或是索引轉欄位與資料間更多的轉換。
#參數
#level : 放整數、字串、串列(默認值為-1(最後一欄))，決定哪一欄位轉為索引
#dropna : 放布林值(默認為True)，決定是否要把遺失的值拿掉

#欄位轉索引：將一欄位(column)轉成一索引(index)，使用 df.stack() 即可。
#注意 .stack() 會由最外層的欄位開始轉換。
import pandas as pd
multicol1 = pd.MultiIndex.from_tuples([
    ('weight','kg'),
    ('weight','pounds')
])
df_multi_level_cols1 = pd.DataFrame([
    [1,2],
    [3,4]
],index = ['cat','dog'], columns = multicol1)
print(df_multi_level_cols1 )
#          weight       
#        kg    pounds
#cat      1      2
#dog      3      4
# 使用默認的 .stack()  (也就是讓入最下面的欄位)
print(df_multi_level_cols1.stack())  #.stack() 欄位轉成索引
#            weight
#cat kg           1
#    pounds       2
#dog kg           3
#    pounds       4
print(df_multi_level_cols1.index, df_multi_level_cols1.stack().index)
#Index(['cat', 'dog'], dtype='object') MultiIndex([('cat',     'kg'),  
#            ('cat', 'pounds'),
#            ('dog',     'kg'),
#            ('dog', 'pounds')],
#           )
#補充 :
#欄位位子最上面 (最外層) 為 0 ，往下一列則加一。
#df.stack() 中的參數也能放一個 list (意思為要提出當索引的欄位位子)

#索引轉欄位
#參數 :
#level : 放整數、字串、串列 (默認為 -1)，決定要把哪一索引轉為欄位。
#fill_value : 放整數、字串、字典，決定遺失值要用甚麼代替。
#索引轉欄位：將一索引(index)轉成一欄位(column) ，使用.unstack()即可。
#注意與 .stack() 相同會由最外層開始轉換。
#df_multi_level_cols1.stack()
#            weight
#cat kg           1
#    pounds       2
#dog kg           3
#    pounds       4
#.unstack() 效果
print(df_multi_level_cols1.stack().unstack())
#          weight       
#        kg    pounds
#cat      1      2
#dog      3      4
#補充 .unstack() 可以不斷地做下去。
#df_multi_level_cols1.stack().unstack().unstack().unstack().unstack().unstack().unstack()
##注意 :
#df.stack() : 當欄位沒東西時，會報錯。
#df.unstack() : 當索引都被移到欄位時，會把所有欄位變為索引。


#欄位名稱轉為欄位值
#數據分析的時候經常要規寬數據變成長數據，有點像你們用 excel 做透視跟逆透視的過程。
#例如下表格（紅框），要將欄位轉成欄位值，也就是說將 Name、Course、Age 轉成欄位值，如下圖，使用.melt() 就可以做到。
#參數
#id_vars：不需要被轉換的列名 ，那些colums name不動
#value_vars：需要轉換的列名，如果剩下的列全部都要轉換，就不用寫了。
import pandas as pd 

df = pd.DataFrame({'Name':{0:'Jiao', 1:'John', 2:'Shiela'}, 
                   'course':{0:'python', 1:'ML', 2:'DM'}, 
                   'Age':{0:22, 1:15, 2:50}})
print(df)
#     Name  course  Age
#0    Jiao  python   22
#1    John      ML   15
#2  Shiela      DM   50
print(df.melt()) #將全部欄位名稱轉為欄位值
#  variable   value
#0     Name    Jiao
#1     Name    John
#2     Name  Shiela
#3   course  python
#4   course      ML
#5   course      DM
#6      Age      22
#7      Age      15
#8      Age      50
print(df.melt('Name'))  #Name欄不用動，其餘欄位名稱轉為欄位值
#     Name variable   value
#0    Jiao   course  python
#1    John   course      ML
#2  Shiela   course      DM
#3    Jiao      Age      22
#4    John      Age      15
#5  Shiela      Age      50
print(df.melt(value_vars = 'Name')) #指轉換Name的欄位圍欄位值
#  variable   value
#0     Name    Jiao
#1     Name    John
#2     Name  Shiela

#重新組織資料
#在做資料分析時很常要重新組織資料，在裡面最靈活好用的就是 .pivot() 函數
#.pivot() 函數根據給定的索引/列值重新組織給定的 DataFrame，接下來以右表為例做介紹
#參數
#index：新資料的索引名稱
#columns：新資料的欄位名稱
#values：新資料的值名稱
df = pd.DataFrame({'foo': ['one', 'one', 'one', 'two', 'two',
                           'two'],
                   'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'baz': [1, 2, 3, 4, 5, 6],
                   'zoo': ['x', 'y', 'z', 'q', 'w', 't']})
print(df)
#   foo bar  baz zoo
#0  one   A    1   x
#1  one   B    2   y
#2  one   C    3   z
#3  two   A    4   q
#4  two   B    5   w
#5  two   C    6   t
print(df.pivot(index = 'foo', columns = 'bar', values ='baz'))
#bar  A  B  C
#foo
#one  1  2  3
#two  4  5  6

#索引轉欄位 .unstack()、欄位轉索引 .stack()，注意最外層為 0 ，往內層一格加一。
#欄位名稱轉為欄位值.melt()，其中參數
#id_vars：不需要被轉換的列名
#value_vars：需要轉換的列名，如果剩下的列全部都要轉換，就不用寫了。
#重新組織資料.pivot()，其中參數
#index：新資料的索引名稱 
#columns：新資料的欄位名稱
#values：新資料的值名稱
