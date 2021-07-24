import numpy as np
#2. 如何從一個陣列中，找出出現頻率最高的數值與位置？
Z = np.random.randint(0,10,50) #(min,max,size)
print(Z)
rint = (np.bincount(Z).argmax())
print(rint)