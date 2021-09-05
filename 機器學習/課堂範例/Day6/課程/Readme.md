# D6：EDA：欄位的資料類型介紹及處理





補充: EDA介紹 

EDA (Exploratory Data Analysis): 探索式資料分析其實就是運用統計工具或是視覺化，來對我們手邊的資料有初步的了解，以幫助我們後續對資料進行更進一步的分析

https://ithelp.ithome.com.tw/articles/10213384





## 1. 知識地圖



**數據前處理**

在數據前處理中，了解我們數據中的各種不同特徵的資料類型是非常重要的，像是我們有一個班級基本資料的數據集，裡面有班級、學生姓名、身高、體重、排名、個性等等，而這樣的數據集中每個特徵欄位的資料類型可能就非常不同，像是如下圖

![image1](..\images\image1.png)



**格式調整**

+ 了解數據集的資料類型後，我們會做到數據格式的調整，像是我們希望班級可以轉換成用數字表達(Label Encoding)，或我們希望身高都轉為整數類型，這些都是為了能夠在之後使用機器學習演算法進行訓練



## 2. 資料的欄位變數一般可以分



+ 離散變數: 只能夠以整數或自然數為單位進行計算，像是

企業的數量、學生數量、國家等



+ 連續變數: 一定區間內能夠任意取值的變數，像是

身高、體重、規格尺寸等



## 3. Pandas DataFrame中所支援的所有資料類型



- float
- int
- bool
- datetime64[ns]
- datetime64[ns, tz]
- timedelta64[ns]
- timedelta[ns]
- category
- object

| Pandas 類型    | Python 類型  | NumPy 類型                                                   | 說明             |
| -------------- | ------------ | ------------------------------------------------------------ | ---------------- |
| object         | str or mixed | string_, unicode_, mixed types                               | 字符串或混合數字 |
| int64          | int          | int_, int8, int16, int32, int64, uint8, uint16, uint32, uint64 | 整數             |
| float64        | float        | float_, float16, float32, float64                            | 浮點數           |
| bool           | bool         | bool_                                                        | True/False       |
| datetime64[ns] | nan          | datetime64[ns]                                               | 日期時間         |
| timedelta[ns]  | nan          | nan                                                          | 時間差距         |
| category       | nan          | nan                                                          | 分類             |



## 4. 重要知識點複習



- 拿到資料的第一步，通常就是看我們有什麼，觀察有什麼欄位，這些欄位代表什麼意義、以什麼樣的資料類型來儲存
- 資料原來是字串/類別的話，如果要做進一步的分析時（如訓練模型），一般需要轉為數值的資料類型，轉換的方式通常有兩種：
  + Label encoding：使用時機通常是該資料的不同類別是有序的，例如該資料是年齡分組，類別有小孩、年輕人、老人，表示為 0, 1, 2 是合理的，因為年齡上老人 > 年輕人、年輕人 > 小孩
  + One Hot encoding：使用時機通常是該資料的不同類別是無序的，例如國家

**補充:**

Label encoding: 把不同的類別，像是A、B、C，mapping成數字0,1,2

One hot encoding: 將每個類別都當成一個欄位，然後用0/1來表示是或否，由於它不能對字串型資料進行處理，只能對數值型資料進行處理，所以通常會先用Label encoding將資料轉成數值型後，再使用One hot encoding處理

![image2](..\images\image2.png)

![image3](..\images\image3.png)

