#1. [簡答題] 請問下列這三種方法有什麼不同？
#print(a.sum()) 
#print(np.sum(a))
#print(sum(a)) 
print("sum() 是 python 內建的函式，所有型態皆可以用。np.sum(a) 跟 a.sum() 是陣列專有的函式，差別在於定義在 np 或是 array 底下。")

#2. 請對一個 5x5 的隨機矩陣作正規化的操作。
import numpy as np
A = np.random.random((5,5))
print(A)
A = (A - A.min()) / (A.max()-A.min())

#3. 請建立一個長度等於 10 的正整數向量，並且將其中的最大值改成 -1。
a = np.random.random(10)
print(a)  
a[a.argmax()] = -1
print(a)