#D13：Pandas Dataframe 的新增與刪除
#從 DataFrame 中插入或刪除資料
#對於一個 DataFrame 可以進行新增或刪除的操作，又可以分為行或是列的方向：
#1.= 可以用來增加行（欄）
#2.append() 可以用來新增列（資料）
#3.del 或 pop() 可以用來刪除行（欄）
#4.drop() 可以用來刪除列（資料）

#1.= 可以用來增加行（欄）
#可以利用指派運算（=）值些產生新的欄位：
import pandas as pd
df = pd.DataFrame([[1],[2]],columns = ['a'])
print(df)
#   a
#0  1
#1  2
df['b'] = pd.Series([3,4]) #增加b欄 [3,4]
print(df)
#   a  b
#0  1  3
#1  2  4

#2.append() 可以用來新增列（資料）
#利用 append(...) 增加新的資料：
df = pd.DataFrame([[1,2]],columns = ['a','b'])
print(df)
#   a  b
#0  1  2
df = df.append(pd.DataFrame([[3,4]],columns = ['a','b']))
print(df)
#   a  b
#0  1  2
#0  3  4
#但仔細看一下，會發現索引重複了，這邊利用 reset_index() 修正：
df = df.reset_index(drop = True)
print(df)
#   a  b
#0  1  2
#1  3  4

#3.del 或 pop() 可以用來刪除行（欄）
#利用 del 或是 pop() 的方法增加新的欄位：
df = pd.DataFrame([[1,2,3]],columns = ['a','b' ,'c'])
print(df)
#   a  b  c
#0  1  2  3
del df['a']
print(df)
#   b  c
#0  2  3
df.pop('c')
print(df)
#   b
#0  2

#4.drop() 可以用來刪除列（資料）
#可以利用 drop(...) 刪除列的資料：
df = pd.DataFrame([[1], [2]], columns = ['a'])
print(df)
#   a
#0  1
#1  2
df = df.drop(1)  #刪除列
print(df)
#   a
#0  1

#DataFrame 的合併與重組
#除了對於一個 DataFrame 的操作之外，我們也會需要 DataFrame 跟 DataFrame 之間的操作，常見可以分為以下幾種：
#1.聯集（Concat）
#2.合併（merge）
#3.連接（Join）
#4.分組（Group）

#1..聯集（Concat）
#利用聯集（Concat）上下相拼：
one = pd.DataFrame({
    'id':[1,2],
    'Name':['Alex','Amy']
})
two = pd.DataFrame({
    'id':[1, 2],
    'Name': ['Bob', 'Tom']
})
print(pd.concat([one,two]))
#   id  Name
#0   1  Alex
#1   2   Amy
#0   1   Bob
#1   2   Tom
#有時候會有索引重複的現象，請務必要修正：
print(pd.concat([one,two]).reset_index(drop = True))
#   id  Name
#0   1  Alex
#1   2   Amy
#2   1   Bob
#3   2   Tom

#2.合併（merge）
#利用合併（merge）實現欄位左右相拼：
one = pd.DataFrame({
    'id':[1, 2],
    'Name': ['Alex', 'Amy'],
})
two = pd.DataFrame({
    'id':[1, 2],
    'Score': [98, 60]
})
print(pd.merge(one,two,on = 'id')) #指定 id 欄合併 
#   id  Name  Score                #默認為left
#0   1  Alex     98
#1   2   Amy     60

#不同的 merge 規則
#合併除了可以指定欄位之外，也可以設定「拼」的方法：
#pandas.merge(left, right, how='inner', on=None ...)
#left、right：必填，任何 dataFrame 物件
#how：提供四種不同的合併方法（參考下圖） 
#on：用來合併的相依欄位
#見講義圖

#3.連接（Join）
#利用連接（Join）實現索引(index)左右相拼：
one = pd.DataFrame({
    'Name': ['Alex', 'Amy'],
})
two = pd.DataFrame({
    'Score': [98, 60]
})
print(one.join(two))
#   Name  Score
#0  Alex     98
#1   Amy     60

#4.分組（Group）
#另外有一種比較特別的用法稱為是分組（Group），會依照資料內容重新組裝：
df = pd.DataFrame({
  'A' : ['foo', 'bar', 'foo', 'bar'],
  'B' : ['one', 'one', 'two', 'three'],
  'C' : [1,2,3,4],
  'D' : [10, 20, 30, 40]
})
print(df)
#     A      B  C   D
#0  foo    one  1  10
#1  bar    one  2  20
#2  foo    two  3  30
#3  bar  three  4  40
print(df.groupby('A').sum())
#A	    c    D
#bar	6	60
#foo	4	40
print(df.groupby('A').agg(sum))
#A	    C	D
#bar	6	60
#foo	4	40
print(df.groupby(['A','B']).sum())
#A    B	     C	  D
#bar  one	 2	 20
# 	  three	 4	 40
#foo  one	 1   10
# 	  two	 3 	 30
