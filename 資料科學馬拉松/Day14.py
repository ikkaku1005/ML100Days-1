#D14：Pandas 的外部資料存取
#DataFrame
#DataFrame 是一種二維的資料結構，使用表格的方式儲存資料。我們會把直向的欄位稱為是 Column、橫向的資料稱為是 Row。
#建立 Pandas 物件
#在 NumPy 中有很多種初始化陣列的方法，但是在 Pandas 當中我們都建議「先直接將資料轉換看看」，可以細分成兩種方法：
#從原有的物件轉換
#從外部資料讀取而來
#各種外部資料來源
#Pandas 支援常見的幾種外部資料來源

#讀寫csv
#CSV 的資料由很多文本資料組成，資料之間以逗點隔開。
#首先我們使用 Pandas 的套件中 pd.read_csv 讀取一個 CSV 檔案夾中的 iris.csv，讀取之後即為 DataFrame 的資料型態。有時候資料太多不想一次讀取這麼多行可以使用 usercols 參數指定讀取的行名稱。

#iris_data= pd.read_csv("iris.csv")
#iris_data
#有時候資料太多不想一次讀取這麼多行可以使用 usercols 參數指定讀取的行名稱。
##iris_data= pd.read_csv("iris.csv",usecils = ['petal length','petal width','target'])

#可以再資料圖取中利用 names 參數指定行的名稱，因為有指定行名稱所以必須以 hearder=0 參數跳過檔案裡放置行名稱的列。
##iris_data= pd.read_csv("iris.csv",headers = 0 ,namess = ['featrue1','featrue2','featrue3','featrue4','target'])

#輸出 csv 檔案使用 .to_csv() 的方法就可以將資料存到指定路徑下。
#iris_data.to_csv("my_iris.csv")

#讀寫excel
#Pandas 利用 pd.read_excel() 函數支援讀取 Excel 2003 之後的格式資料，此方法內部是使用 XLRD 或 OpenPyXL 套件，所以使用前確認至少安裝其中一項
#data = pd.read_excel('data.xls')

#pd.read_excel() 只會讀第一個工作簿，如今天 excel 工作簿不只一個，我們可以使用 sheetname 參數傳入要讀取頁面的名稱。
#boston_data = pd.read_excel('data.xls',sheet_name = 'boston')

#pd.read_excel 和 pd.read_csv 一樣有 usecols、header、names 可以使用。
#boston_data = pd.read_excel('data.xls',sheet_name = 'boston',header = 0 \,usecols = ['Tax','piratio','b'])

#輸出 excel 檔案使用 .to_excel() 的方法就可以將資料存到指定路徑下，也可以使用 sheet_name 更改工作簿名稱。
#boston_data.to_excel('my_boston.xlsx',sheet_name = 'boston')

#讀寫json
#利用 pd.read_json() 函數支援讀取 JavaScript 物件表示法(JSON)格式資料，json 具有跨平台與程式語言的可攜性。
#boston_data = pd.read_json('boston.json')
#輸出 json 檔案使用 .to_json() 的方法就可以將資料存到指定路徑下。
#boston_data.to_json('boston.json')

#讀寫SQL資料庫
#任何 SQL 資料庫如果支援遵守 Python DB-API 都可以被 Pandas 讀取。以下先用 boston.csv 的資料寫入 SQLite3 資料庫中並且命名 boston，由 if_exists 參數判斷是否存在資料庫，如果檔案不存在會立即被建立，如果存在 if_exists='replace' 將會取代掉原本資料，if_exists='append'將會繼續寫在原有資料下。
#import sqlite3
#. . .  見講義
#讀取 SQLite3 資料庫可以使用 pd.io.sql.read_sql，可以直接下 SQL 指令對 sql_db 中的 boston 做搜尋。

#認識類別資料
#變數的特徵屬於非數值型態。需利用一組的標記、類別、性質或名稱以區別每個基本單位的特徵、屬性。無法以數值表示的統計資料，如航班編號、性別、學歷、旅遊同伴、頭髮顏色、宗教等。類別資料中可以分為兩類順序性與一般性兩種
#順序性 : 類別之間存在順序性，例如:衣服尺寸[XL,L,M]、長度[短,中,長]
#一般性 : 類別之間沒有順序關係，例如 : 顏色[黃,綠,藍]、性別[男,女]
#大部分的模型都是基於數學運算，字串無法套入數學模型進行運算，在此先對其進行 encoding編碼(將類別資料轉成數字)才能進一步對其做分析。
#對於順序性的類別資料，需要有順序性的 encoding 方法，可以使用 sklearn 中的 LabelEncoder()。
#對於一般性的類別資料，則不需要有順序的編碼，可以使用 pandas 中的 get_dummies()


#認識類別資料 順序性 LabelEncoder()
#順序性類別資料，編碼也需要有順序性，將類別資料依序編碼由 0 到 n-1，其中 n 為類別總數，因此類別之間會有順序關係 0<1<2<….，排序依照 python 內建順序，可以藉由 ord() 查看內建順序。
import pandas as pd
df = pd.DataFrame([['green','M','male','short'],
                    ['red','L','female','normal'],
                    ['blue','XL','male','long']
                                                ])
df.columns = ['color','size','sex','lenght']
print(df)

from sklearn.preprocessing import LabelEncoder
df['size_label'] = LabelEncoder().fit_transform(df['size'].values)
print(df)

#認識類別資料 一般性 get_dummies()
#get_dummies() 把資料表中的每個類別 對應的欄位，經過 One-hot Encoding(一位有效編碼)，增加資料表的欄位代表所屬的類別，如下欄位 color 中有 green、red、blue 將他們一一編入欄位中 color_blue、color_green、color_red 這個一對一的關係通常稱為 One-hot Encoding(一位有效編碼) 是沒有順序性的編碼。
pf = pd.get_dummies(df[['color']])
df = pd.concat([df,pf], axis = 1)
print(df)

#認識缺值處理方法與應用函式
#資料缺失時常發生在問卷資料上，填寫人時常會漏寫或不願意填寫，導致資料上有缺失值，只要缺失值將會填上 nan 代替缺失值，大部分的模型不能處理缺失值的問題，一般來說會將有缺失值的資料整筆直接刪除，但是這樣會損失其它欄位的資料，所以如果缺失情況不嚴重，傾向於將缺失值補上數值，以下最常見兩種補值方式。
#1.定值補值 : 將缺失值都補上一個定值
#2.前(後)補值 : 補前(後)一列的值

#認識缺值處理方法與應用函式:定值補值
#函式 fillna() 可以將所有缺失值填補上固定的數值
temp_data = pd.DataFrame([['2020-11-01', 24.8],
             ['2020-11-02', 24.8],
             ['2020-11-03', None],
             ['2020-11-04', 25]],columns=['date','current_temp'])
print(temp_data)
#         date  current_temp
#0  2020-11-01          24.8
#1  2020-11-02          24.8
#2  2020-11-03           NaN
#3  2020-11-04          25.0
print(temp_data.fillna(0)) #以0填補
#         date  current_temp
#0  2020-11-01          24.8
#1  2020-11-02          24.8
#2  2020-11-03           0.0
#3  2020-11-04          25.0

#也可以補上平均值、中位數、….等的數值
print(temp_data.fillna(temp_data.current_temp.median())) #以current_temp該欄的中位數做填補

#認識缺值處理方法與應用函式 前(後)補值
#前(後)補值最常使用在金融上，有時候因為颱風天導致沒有開盤，這時沒開盤那天的數值空了通常都會補前一天的價錢。
#函式一樣使用 fillna()，我們只需要進一步運用參數method=‘ffill’即可填補前一列數值， method=‘bfill’ 填補後一列數值
print(temp_data.fillna(method = "ffill")) #填補前一列的數值
#         date  current_temp
#0  2020-11-01          24.8
#1  2020-11-02          24.8
#2  2020-11-03          24.8
#3  2020-11-04          25.0
print(temp_data.fillna(method = "bfill")) #前補後一列的數值
#         date  current_temp
#0  2020-11-01          24.8
#1  2020-11-02          24.8
#2  2020-11-03          25.0
#3  2020-11-04          25.0

#Missing Value 是什麼？
#很常在讀寫資料的過程中，產出 NaN 的型態，那這個東西到底是什麼呢？
#NaN 是一種被定義在 NumPy 中的特殊型態，全名為 Not a Number，通常被當成是「空值/缺失值」使用。

#缺值資料的處理
#缺值是程式或模型中無法正確計算的資料，必須先處理乾淨後才可以進行後面的操作。常見的處理策略如下：
#直接刪除含有缺失值的資料或欄位
#利用人工填補遺失值
#利用常數或通用值填補遺失值
#利用類似資料/全部資料的統計值值填補遺失值
#利用統計方法進行補值（內差/回歸）
#利用機器學習方法進行補值（預測）
