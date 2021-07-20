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
        newlist.append(tolist(obj))
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

