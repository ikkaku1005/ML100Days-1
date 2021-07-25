import numpy as np
#如何利用 list(...) 實現 a.tolist() 的效果？試著用程式實作。
#method1 簡單版
a = np.random.randint(10, size=6) 
print(a)
b = np.random.randint(10, size=(3,4)) 
c = np.random.randint(10, size=(2,3,2)) 
d = (989)
def tolist(iterable):
    if type(iterable) != np.ndarray:
        return iterable
    newlist = []
    for obj in iterable:
        newlist.append(tolist(obj))    #取出 iterable 的每個 element， iterable 為一維 array，則 append(obj) 與 append(tolist(obj)) 會是相同結果；    
                         #然而若為二維矩陣，obj 就會是一維向量，這時若使用 append(obj)，每個加入 newlist 的 element 會是一個個一維向量，
                         #而 append(tolist(obj)) 會是增加一個 list，
                         #兩者輸入至 newlist 的資料型態會不一樣。
    return list(newlist)
# tolist(d) #可省
#tolist(a) 可省
print(tolist(d))
print(tolist(a)) 
print(tolist(b))
print(tolist(c))

## method2進階版
def tolist(iterable):
    if type(iterable) != np.ndarray:  
        return iterable
    return [tolist(obj) for obj in iterable]

print(tolist(a))
print(tolist(b))
print(tolist(c))

