# 機器學習 - D5 如何新建一個 dataframe? 如何讀取其他資料? (非 csv 的資料)



## 範例





### 1. Day_005-1

檔案: Day_005-1_build_dataframe_from_scratch.ipynb



#### 創建DataFrame的方法一

Step1: 定義一個Python字典，將對應的數據填入

Step2: 使用pd.DataFrame()來將剛剛的字典轉換成DataFrame



#### 創建DataFrame的方法二

Step1: 創建各種數據(以串列的形式創建)

Step2: 創建標籤串列

Step3: 創建列的數據(將Step1中的變數填入)

Step4: 將標籤和列數據使用zip()來壓縮在一起，並轉成串列

Step5: 將壓縮好的串列(list)轉成dictinary格式，然後使用pd.DataFrame()轉換成DataFrame





#### 資料操作: groupby

這邊會使用一個DataFrame常用的操作 - groupby()



Step1: 我們要以weekday來分組，所以使用groupby(by='weekday')

Step2: 我們要知道以weekday當分組下，visitor的平均數量



**補充:  ** GroupBy可以想像是一種拆分、應用、組合的過程

可以使用的一些聚合操作

| Aggregation          | Description                     |
| :------------------- | :------------------------------ |
| `count()`            | Total number of items           |
| `first()`, `last()`  | First and last item             |
| `mean()`, `median()` | Mean and median                 |
| `min()`, `max()`     | Minimum and maximum             |
| `std()`, `var()`     | Standard deviation and variance |
| `mad()`              | Mean absolute deviation         |
| `prod()`             | Product of all items            |
| `sum()`              | Sum of all items                |



### 2. Day_005-2

**檔案:** Day_005-2_read_and_write_files.ipynb



#### 讀取txt檔

**Step1:** 使用with open()來讀取我們local端data資料夾裡面的txt檔

**Step2:**接著使用readlines將檔案一行一行讀出來





#### 將txt 轉成 pandas dataframe

Step1: 創建一個空的串列 (用來裝後面的分割好的數據)

Step2: 使用with open()來讀取我們local端data資料夾裡面的txt檔

Step3: 將字符串中的"\n"取代成空的，並以","來分割數據成串列

Step4: 將分割好的數據一個一個塞入我們創建的新串列 - data

Step5: 將第一筆以外的數據轉成DataFrame

Step6: 將第一筆數據當作是DataFrame的列



#### 將資料轉成json檔後輸出

將 json 讀回來後，是否與我們原本想要存入的方式一樣? (以 id 為 key)



**存入json**

Step1: 導入json套件

Step2: 把前面建立好的df(DataFrame)轉成json檔，並指定存在data資料夾底下

**載入json**

1.

Step1: 使用讀取文件的方式with open來讀取剛剛存好的json檔

2.

Step1: 把df中的'id'欄位設成索引列

Step2: 將df存成json檔

Step3: 載入存好的json檔



參考: https://matters.news/@CHWang/%E5%AF%AB%E7%B5%A6%E8%87%AA%E5%B7%B1%E7%9A%84%E6%8A%80%E8%A1%93%E7%AD%86%E8%A8%98-%E4%BD%9C%E7%82%BA%E7%A8%8B%E5%BC%8F%E9%96%8B%E7%99%BC%E8%80%85%E6%88%91%E5%80%91%E7%B5%95%E5%B0%8D%E4%B8%8D%E8%83%BD%E5%BF%BD%E7%95%A5%E7%9A%84json-python-%E5%A6%82%E4%BD%95%E8%99%95%E7%90%86json%E6%96%87%E4%BB%B6-bafyreibegh77qc2xaejwbbbv5xdoodgqyaznesq5uhety5von3rpqzdaoa





**補充:**

**使用方法**

| 函數       | 說明                                       |
| ---------- | ------------------------------------------ |
| json.dumps | 將Python對象(Object)編碼成JSON格式的字符串 |
| json.dump  | 將Python字典轉成JSON後，寫入JSON文件       |
| json.loads | 將JSON字符串解碼成為Python對象(Object)     |
| json.load  | 直接讀取JSON文件，並轉成Python字典         |



#### 將檔案存為npy檔

一個專門儲存 numpy array 的檔案格式 使用 npy 通常可以讓你更快讀取資料喔!

Step1: 導入numpy套件

Step2:將前面創立的data串列轉成NumPy數組

Step3: 保存成npy檔(使用np.save)

Step4: 載入npy檔(np.load)



經驗: 我自己的經驗上，公司常使用這個方法來保存數據集，為了之後的載入可以更快更有效率



#### 將檔案存成Pickle檔

Step1: 導入pickle套件

Step2: 使用with open來新建一個檔案，並使用pickle .dump()寫入檔案

Step3: 使用with open打開檔案，並使用pickle.load()來載入檔案



### 3. Day_005-3

檔案: Day_005-3_read_and_write_files.ipynb



#### 環境設定

+ 我們要先導入matplotlib套件(繪圖用)和numpy套件

+ 使用%matplotlib inline可以使圖像直接嵌入到notebook中喔



#### skimage.io

可以參考: https://www.itread01.com/content/1549068846.html

Step1:使用imread來讀取圖片

Step2: 使用plt.imshow來顯示圖像



#### PIL(pillow)

Pillow庫為Python的第三方庫

Python2中PIL(Python Imaging Library)是一個非常好用的圖像處理套件，但其不支援Python3，所以有了Pillow庫的誕生

Step1: 導入PIL中的Image套件

Step2: 讀取圖片(使用Image.open)

Step3: 讀取回來的會是一個PIL object，所以要轉成NumPy數組

Step4: 顯示圖像



#### cv2

**安裝套件:** pip install opencv-python

Step1: 使用讀取圖片

Step3: 使用plt.imshow來顯示圖像

Step4: 將原本為BGR格式的圖像轉為RGB格式

Step5: 使用plt.imshow來顯示圖像



**補充:** 能指定轉換的格式

+ cv2.IMREAD_COLOR: 讀取RGB的三個CHANNELS的彩色圖片，忽略透明度的CHANNELS

+ cv2.IMREAD_GRAYSCALE: 灰階

+ cv2.IMREAD_UNCHANGED: 讀取圖片的所有CHANNELSS，包含透明度的CHANNELS





**補充: skimage.io.imread 和 cv2.imread 比較**

紅綠藍(RGB)

藍綠紅(BGR)

+ skimage.io讀出圖像的格式為uint8(unsigned int)，value為NumPy數組，而圖像是以RGB的格式來儲存的，通道值預設為0~255
+ cv2.imread讀出圖像的格式為int8，value為NumPy數組，而圖像是以BGR的格式來儲存的，BGR格式需要將存儲類型改成RGB的格式才會正常顯示遠使徒的顏色



#### 比較三者讀取圖像的速度

+ 使用%%timeit這個魔法函數來計算程式執行時間

+ 可以發現cv2比較快一點(而且它還做了格式轉換還是比較快)



#### 將圖像存成mat檔

補充: mat是一個類，兩個部分構成: 矩陣頭(矩陣尺寸、存儲方法、儲存地址等等)與一個指向儲存所有像素值的矩陣指針



Step1: 導入scipy.io套件，用來讀寫mat檔

Step2: 先將前面的圖img1保存為mat檔(指定在字典中的'img'欄位)

Step3: 載入mat檔，並印出mat字典中所以得鍵值

Step4: 查看一下圖像的shape(第一個為水平像素，第二個為垂直像素，第三個為channel，3表示RGB彩色圖，1是灰階圖片)

Step5: 顯示圖像













## 作業



### 1 . Day5-1作業 - Day_005_HW.Ipynb解說



**檔案:** Day_005_HW.Ipynb



**題目:** 在小量的資料上，我們用眼睛就可以看得出來程式碼是否有跑出我們理想中的結果。請嘗試想像一個你需要的資料結構 (裡面的值是隨機的)，然後用程式碼範例的方法把它變成 DataFrame



**作業範例:** 在作業的範例中我們可以看到，這個DataFrame具有兩列，分別為國家和人口，然後這個DataFrame擁有三個數據，分別為台灣、美國和泰國的人口數據



**解法步驟:**



**創立一個隨機的DataFrame**

Step1: 創建一個Python字典，用來將我們的數據填入

Step2: 填入我們指定的國家，像是台灣、美國和泰國

Step3: 隨機地產生這三個國家的人口數據

(因為人口不會有小數，而且每個國家也應該至少會有一定的人口，所以我這邊採用在一個區間內隨機產值的方法)

(我這邊採用的區間在100~10000，國家的人口當然不會那麼少xd，當然大家可以自己決定這個區間)

Step4: 建立DataFrame，將剛剛建立好的Python字典放入

Step5: 顯示DataFrame



**找尋最大人口的國家**

Step1: 先找到"人口"數據中最大的那個值

Step2: 並透過Mask的方法來搜尋整個DataFrame中符合這個值的國家數據





### 2. Day 5-2 作業



#### 1

##### 1.1 讀取 txt 檔, 請讀取 text file

Step1: 自行將txt檔存在電腦中，或複製連結: https://raw.githubusercontent.com/vashineyu/slides_and_others/master/tutorial/examples/imagenet_urls_examples.txt

Step2: 使用request來取得資料 並建立一個try-except的機制來判斷給定的這個url，可以使用request來取得資料嗎

Step3: 印出取的的資料長度

Step4: 顯示資料前100個字符 





##### 1.2: 將所提供的 txt 轉成 pandas dataframe

Step1: 確定我們要找的資料(url)

Step2: 利用特定的分隔符\n來split出我們要的資料

Step3: 資料裡面還存有一組編號和一組url，我們要再將其分隔

Step4: 將url和編號資料分裝在兩個我們創建的串列中，並合成一個字典

Step5: 將Python字典轉為DataFrame

Step6: 顯示前五筆資料



#### 2



從所提供的 txt 中的連結讀取圖片，請讀取上面 data frame 中的前 5 張圖片



##### **1. 先讀取第一張圖片試試**

Step1: 導入所需的套件

Step2: 取得第一組連結

Step3: 使用request獲取資料

Step4: 讀取圖片(二進制)

Step5: 轉換成NumPy數組

Step6: 顯示圖片



**補充說明: BytesIO**

+ 再很多的狀況下，數據的讀寫不一定要經過文件街口這個方法，它可以直接在內存中去進行讀寫，這樣的優點就是快，而這個方法分成StringIO和BytesIO，StringIO只能操作str，但如果要操作二進制的資料，就需要用到BytesIO

+ 在題目中 由於傳入Image.open的需要是二進制的形式，所以我們使用BytesIO轉



##### **2. 一次讀取前五張照片**



Step1: 撰寫一個img2arr_fromURL函式，來將傳入的URLs串列，照著前面讀取圖片的方法來轉換好格式，最後轉成NumPy數組並傳回

Step2: 使用例外處理檢查這前五個圖片檔都能讀取嗎

Step3: 我們會發現第五張圖沒辦法讀取

Step4: 將前四張圖，透過img2arr_fromURLs函數轉換成NumPy數組後，一一顯示其圖像









