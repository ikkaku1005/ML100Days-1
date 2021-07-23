#D6：Numpy 中常見的陣列方法與函式
#NumPy 最主要提供了陣列的資料結構，我們會把定義在陣列上可用的方法稱為是通用函式（universal function，ufunc）。ufunc 與一般的函式的差別在於，他是一種特別適合用於陣列元素級別的操作（以整組為單位的元素運算）。也就是說，ufunc 滿足矩陣運算的特性，例如廣播、對齊這樣的特性。所以，我們也會稱 ufunc 是一種用於向量化（vectorized）運算的封裝函式。
#陣列中的統計方法
#NumPy 提供了很多統計函數，用於從陣列中查找最小元素，最大元素，百分位標準差和方差：
import numpy as np
a = np.arange(6)
print(a)
print(a.sum())
print(a.min())
print(a.max())

#一種功能，三種函式
#對一個 NumPy 的陣列進行操作，可能有三種層級的函式（都可以得到相同的結果）：
print(a.sum())
print(np.sum(a))
print(sum(a))

#NumPy 陣列統計函式 - 順序統計量
#numpy.fmax(), numpy.fmin()
#以 element-wise 比較 2 個陣列並回傳各元素的最大值或最小值。與 maximum() / minimum() 不同的是，如果比較的元素中只有一個是 nan 的話，回傳非 nan 的值，如果兩個元素都是 nan 則回傳 nan。
#同樣在進行比較時，若有需要會利用到廣播 (bradcasting)。

#numpy.nanmax(), numpy.nanmin()
#回傳陣列中有非 nan 元素值的最大值或最小值。
#可以指定要比較的軸(axis)，以及回傳值是否要保留維度。
#百分位數：percentile(), nanpercentile()
#計算百分位數，percentile() 與 nanpercentile() 不同的地方在於後者會忽略 nan。
#欲取得的百分位數引數，可以傳入純量或是陣列的值 (介於0 - 100 之間)，也可以指定要比較的軸，以及回傳值是否要保留維度。
#分位數：quantile(), nanquantile()
#計算分位數，quantile() 與 nan quantile() 不同的地方在於後者會忽略 nan。如果元素中包含 nan 的話，則 quantile() 會回傳 nan。
#欲取得的分位數引數，可以傳入純量或是陣列的值 (介於0 - 1 之間)，也可以指定要比較的軸，以及回傳值是否要保留維度。


#NumPy 陣列統計函式 - 平均數與變異數
#平均值：mean(), nanmean()
#mean() 和 nanmean() 不同的地方在於後者會忽略 nan。如果元素中包含 nan 的話，則 mean() 會回傳 nan。下面的例子使用 np.isnan() 判斷陣列中是否包含 nan，如果無 nan 的話就呼叫 mean() 計算平均值，反之則呼叫 nanmean() 進行計算。
#可以指定要計算平均數的軸，以及回傳值是否要保留維度。dtype 引數是計算使用的型別，若輸入陣列是整數的話，則會用 float64 型別計算，若輸入的是浮點數的話，則是依輸入陣列的型別做為 dtype。
#平均值：average()
#使用 average() 計算平均值的話，可以輸入權重值做為引數。
#須注意權重的總和不能為 0，否則會產生錯誤。
#計算中位數：median(), nanmedian()
#median() 和 nanmedian() 不同的地方在於後者會忽略 nan。如果元素中包含 nan 的話，則 median() 會回傳 nan。
#可以指定要計算中位數的軸，以及回傳值是否要保留維度。要留意的是，如果軸或是陣列總數不是單數的話，中位數的值會是中間 2 個元素值相加除以 2。
#計算標準差：std(), nanstd()
#std() 和 nanstd() 不同的地方在於後者會忽略 nan。如果元素中包含 nan 的話，則 std() 會回傳 nan。
#可以指定要計算標準差的軸，以及回傳值是否要保留維度。若是對於精度可能造成的誤差影響，可以改變 dtype 提高精度。
#如果要計算樣本標準差的話，可將 ddof (自由度) 引數傳入 1，在計算平均方差 (mean squared deviation) 時分母就會以 N - ddof 做計算。
#計算變異數：var(), nanvar()
#var() 和 nanvar() 不同的地方在於後者會忽略 nan。如果元素中包含 nan 的話，則 var() 會回傳 nan。
#可以指定要計算變異數的軸，以及回傳值是否要保留維度。若是對於精度可能造成的誤差影響，可以改變 dtype 提高精度。
#如果要計算樣本變異數的話，可將 ddof (自由度) 引數傳入 1，在計算平均方差 (mean squared deviation) 時分母就會以 N - ddof 做計算。


#NumPy 陣列統計函式 - 相關性
#相關係數：corrcoef()
#orrcoef() 計算 Pearson 積差相關係數。引數 rowvar 預設值為 True，代表將每一個 row 當做是一筆變數。
#
#互相關 (Cross-correlation)：correlate()
#計算 2 個一維序列的互相關。
#共變異數：cov()
#NumPy 陣列統計函式 – 直方圖 (Histogram)
#NumPy 提供 np.histogram() 函式來計算 histogram，基本語法及引數說明如下：
#numpy.histogram(a, bins=10, range=None, normed=None, weights=None, density=None)
#引數	  說明
#a	      輸入陣列
#bins	  bins的定義，可傳入純量、序列、或是不同的方法（例如：auto）
#range	  bins的範圍，預設是 a.min() 與 a.max() 之間，或是依照傳入的範圍
#weights  權重值，陣列形狀須與 a 相同
#density  False：回傳各bin的count
#         True：回傳各bins的probability density


#陣列中的軸參數
#對多維的陣列進行操作，可以設定軸（Axis）的參數：
import numpy as np
b = np.arange(12).reshape(3,4)
# array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]])
print(b.sum())
print(b.sum(axis = 0)) #axis = 0 行
print(b.sum(axis = 1)) #axis = 1 列  
#Axis 其實指的是陣列的層級，
#當 axis = i 就是要從沿著第 i 個方向進行操作。
#軸 (axis) 在 NumPy 多維陣列中是很重要觀念，但是在應用上容易混淆。軸的數目也就是 NumPy 陣列的維度 (dimension) 數，軸的順序編號從 0 開始。
#如果是要增加軸數的話，可以使用 np.newaxis 物件。將 np.newaxis 加到要增加的軸的位置即可。


#搜尋與排序方法
#在陣列中也常常會用到搜尋和排序的方法，以排序來說也會有兩種實現方法：
a = np.array([1,3,2,5,4])
print(a.sort())  
#none
print(np.sort(a)) #排序
print(a)

#numpy.sort(...) 更多用法
#來看一下關於 np.sort(...) 參數比較細節的用法：
#numpy.sort(a, axis=-1, kind=None, …)
#a：必填，任何需要被排序的 array_like 物件
#axis：預設 = -1，指的是排序的方向
#kind：有四種排序算法可以選（quicksort, mergesort, heapsort, stable），預設為 quicksort 演算法
#補充：排序演算法
#不管是 np.sort(a) 或是 a.sort() 的排序方法，都有一個參數叫 kind，可以用來指定排序算法，可以從選 quicksort, mergesort, heapsort, stable 選擇一種（預設為 quicksort 演算法）。

#搜尋與排序方法
#搜尋的話可以使用 searchsorted() 的函式：
print(np.searchsorted([1,2,3,4,5],3))
print(np.searchsorted(
    [1,2,3,4,5],
    [-10,10,3,5]
))

#NumPy 陣列搜尋與排序 – argmax() 與 argmin()
#argmax() / argmin() 和上述不同的地方在於，argmax() / argmin() 回傳的是最大值和最小值的索引，也可以依照軸找出各軸最大值和最小值的索引。
#有 2 種不同的使用方式：
#np.argmax(array,axis = none)
#np.argmin(array, axis = none)

#NumPy 陣列搜尋與排序 – where()
#傳入條件式，回傳值為符合條件的元素索引。
#若是多維陣列的話，會回傳多個陣列的索引值，要合在一起看。以二維陣列為例：
#上面的回傳值代表 a[0, 0], a[0, 1], a[1, 3], a[2, 2] 均為符合條件的元素索引值。

#NumPy 陣列搜尋與排序 – nonzero()
#nonzero 等同於 np.where(array != 0) 的語法，同樣的也是回傳符合非 0 條件的元素索引值。
#有 2 種不同的使用方式：
#np.nonzero(array)


#NumPy 陣列搜尋與排序 – sort() 與 argsort()
#要對陣列進行排序可以使用 sort() 與 argsort()，兩者的差異是在 sort() 回傳的是排序後的陣列，而 argsort() 回傳的是排序後的陣列索引值。
#有 2 種不同的使用方式：
#np.sort()
#np.argsort()
#與 np.sort() 不同的是，陣列物件.sort() 的語法會進行 in-place 排序，也就是原本的陣列內容會跟著改變。
#多維陣列在排序時可以指定要依據的軸。
#排序支援多種不同的排序算法，包括 quicksort (預設)、heapsort、mergesort、timesort，在 kind 引數指定即可。依照官網文件指出排序速度是以 quicksort 最快，mergesort / timesort 其次，之後是 heapsort。


#陣列中的形狀方法
#另一種常見的情境是，我們會去改變陣列的形狀與大小。跟形狀有關的方法可以分成兩種類型：
#reshape、 resize
#三種陣列攤平用法
#reshape 和 resize
#reshape(...) 和 resize(...) 都可以將陣列的形狀改變，你看得出他們的差異嗎？
a = np.arange(6)
print(a.reshape(3,2))  #3x2
#[[0 1]
# [2 3]
# [4 5]]
print(a)
#[0 1 2 3 4 5]
print(a.resize((3,2)))  #給定一個數組，和特定維度，將會返回一個給定維度形式的新陣列。
                        #如果新陣列比原陣列大，則將會copy原陣列中的值對新陣列進行填充
## None


#三種陣列攤平用法
#有的時候我們會想要將多維形狀的陣列轉換成一維的，這個方法我們稱為「攤平」，常見有三種方法：
a = np.arange(6).reshape((3,2))
print(a.ravel())
print(a.flatten())

#NumPy 陣列重塑 - flatten() 與 ravel()
#透過 flatten() 與 ravel() 均可將多維陣列轉形為一維陣列，flatten() 與 ravel() 的使用透過下列兩種方法，得到的結果都是完全一樣的。
#不同的是，ravel() 建立的是原來陣列的 view，所以在 ravel() 回傳物件中做的元素值變更，將會影響原陣列的元素值。
#預設展開的順序是 C-style，展開時是以 row 為主的順序展開。

#NumPy 陣列重塑 - reshape()
#呼叫 reshape() 時指定新的形狀 (shape)，可將陣列重塑為該形狀，但如果新的總數與原先 shape 總數不一致的話，則會產生錯誤。
#Reshape 時，新的形狀可以採用模糊指定為 -1，讓 NumPy 自動計算，例如：a.reshape((5, -1))。
#若 reshape 後的陣列元素值改變，會影響原陣列對應的元素值也跟著改變。
#NumPy 陣列重塑 - resize()
#與 reshape() 不同的地方在於，如果 resize 的大小超過總元素值，則會在後面的元素值的指定為 0。
#如果 resize 的大小小於總元素值，則會依照 C-style 的順序，取得 resize 後的陣列元素。

#NumPy 陣列的合併 - concatenate()
#使用 concatenate() 進行陣列的合併時，須留意除了指定的軸之外 (預設為 axis 0)，其他軸的形狀必須完全相同，合併才不會發生錯誤。

#NumPy 陣列的合併 - stack(), hstack(), vstack()
#stack(), hstack(), vstack() 的觀念及用法類似，不同點在於 stack() 回傳的陣列維度會是合併前的維度 +1，而 hstack() 與 vstack() 回傳的陣列維度則是依合併的陣列而定。
#至於是否可以合併，stack() 必須要所有陣列的形狀都一樣；而 hstack() 與 vstack() 則跟上述的規則一樣，除了指定的軸之外，其他軸的形狀必須完全相同才可以合併。

#NumPy 陣列的分割 – split()、hsplit()、vsplit()
#呼叫 split() 時 indices_or_sections 引數如果給定單一整數的話，那就會按照軸把陣列等分；如果給定一個 List 的整數值的話，就會按照區段去分割。
#hsplit() 與 vsplit()，分別是依照水平軸和垂直軸去做分割。
