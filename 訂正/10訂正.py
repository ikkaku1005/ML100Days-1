#2. 請根據提供的資料，選擇出下列的要求：
# - select the first 3 rows.
# - select the odd rows. (index = 1, 3, 5)
# - select the last 2 columns.
# - select the even columns. (index = 0, 2, 4)
# 參考解答
# - select the first 3 rows.
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
print(df[0:3])
print(df.iloc[0:3,:]) #列，行 
print(df.iloc[0:3])

# - select the odd rows. (index = 1, 3, 5)
print(df[1::2]) #df[起始::間隔] 選列
print(df.iloc[1::2, :])
print(df.iloc[[1,3,5], :])

# - select the last 2 columns.
print(df.iloc[:, -2:])

# - select the even columns. (index = 0, 2)
print(df.iloc[:, 0::2])
print(df.iloc[:, [0, 2]])


print("==============================================")

#3. 請根據提供的資料，選擇出下列的要求：
# - 1. filtered by first column > 20?
# - 2. filtered by first column + second column > 50
# - 3. filtered by first column < 30 or second column > 30
# - 4. filtered by total sum of row > 100
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
# - 1. filtered by first column > 20?
print(df.loc[df[0]>20])
print(df[df[0] > 20])
# 參考解答

# - 1. filtered by first column > 20?

print(df.loc[df[0] > 20])
print(df[df[0] > 20])

# - 2. filtered by first column + second column > 50

print(df[df[0] + df[1] > 50])
print(df.loc[df[0] + df[1] > 50])

# - 3. filtered by first column < 30 or second column > 30
print(df[np.logical_or(df[0] < 30, df[1] > 30)])
print(df[(df[0] < 30) | (df[1] > 30)]) #| :or 

# - 4. filtered by total sum of row > 100
print(df[df[0] + df[1] + df[2] + df[3] > 100])
print(df[df.sum(axis=1) > 100])  #axis = 1 : row