#1. 產生一個 1-11 的一維陣列，並且把 3-6 由正數變成負數
import numpy as np
A = np.arange(11) + 1 
print(A)
A[(3 <= A) & (A < 7)] *= -1 # a *= 5 意思為 a = a*5
print(A)