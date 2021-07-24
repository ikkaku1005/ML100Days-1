#1. 請比較對一個 100 x 100 x 100 的陣列，使用不同方法對每一個元素 +1 的時間比較。
import numpy as np
Z = np.random.randint(0,100,1000000).reshape(100,100,100)
%timeit -n 10 a = 2
for i in Z:
    for j in i:
        for k in j:
            i = i + 1

%timeit -n 10 a = 2
for i in Z.flat:
    i = i+1

%timeit -n 10 a = 2
for i in np.nditer(Z): #迭帶
    i = i + 1
    