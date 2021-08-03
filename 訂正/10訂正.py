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
df = pd.DataFrame(np.random.randint(10, 40, 60))
print(df)
#      0
# 0   30
# 1   10
# 2   27
# 3   38
# 4   14
# 5   33
# 6   14
# 7   23
# 8   19
# 9   39
# 10  10
# 11  33
# 12  35
# 13  14
# 14  27
# 15  23
# 16  38
# 17  32
# 18  29
# 19  16
# 20  25
# 21  22
# 22  14
# 23  33
# 24  37
# 25  36
# 26  29
# 27  12
# 28  15
# 29  29
# 30  26
# 31  16
# 32  21
# 33  36
# 34  21
# 35  15
# 36  16
# 37  35
# 38  19
# 39  10
# 40  22
# 41  31
# 42  30
# 43  18
# 44  16
# 45  32
# 46  36
# 47  29
# 48  30
# 49  12
# 50  16
# 51  14
# 52  23
# 53  36
# 54  25
# 55  16
# 56  18
# 57  30
# 58  21
# 59  17
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
print(df)       #np.random.randint(10, 40, 60) 10~40中挑60個 size = 60
#     0   1   2   3
# 0   35  14  10  36
# 1   37  39  11  29
# 2   23  16  22  20
# 3   10  31  38  32
# 4   27  28  24  12
# 5   33  16  16  36
# 6   17  13  33  30
# 7   29  38  19  25
# 8   33  24  31  13
# 9   16  38  25  25
# 10  39  12  21  39
# 11  26  29  26  24
# 12  36  32  39  11
# 13  25  18  29  11
# 14  38  13  21  15
#reshape
#當我們使用reshape(1,-1)時數據就會變成一列，使用reshape(-1,1)時數據就話變成一行，
# -1的部分，則是unsepcified value也就是未指定
# 換句話說今天我若是指定reshape(-1,4)的話，那麼就會數據就會變成四行，而列則未指定
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