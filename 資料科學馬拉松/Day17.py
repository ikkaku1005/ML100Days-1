# #D17：Pandas 時間序列資料處理
# #時間序列資料處理
# 所有資料中只要有時間關係就需要使用到時間序列的資料型態，因為資料之間是有時間關係的，資料之間的時間距離也不盡相同
#時間序列的資料非常注重間的間隔

# 既然時間間隔重要，那首先必須介紹控制時間長度的函數.to_period(freq = "")，參數 freq 代表時間頻率(Y：年、M：月、D：日、H：小時)

#可以運用 resample 函數將年轉成季，如沒有值的填上 nan。
import pandas as pd
df = pd.Series([1, 2, 3, 4, 5], index=pd.period_range('2021-01-01', freq='Y', periods=5)) #Y:年
print(df)
# 2021    1
# 2022    2
# 2023    3
# 2024    4
# 2025    5
# Freq: A-DEC, dtype: int64
print(df.resample('Q', convention='start').asfreq())  #年轉成季
# 2021Q1    1.0
# 2021Q2    NaN
# 2021Q3    NaN
# 2021Q4    NaN
# 2022Q1    2.0
# 2022Q2    NaN
# 2022Q3    NaN
# 2022Q4    NaN
# 2023Q1    3.0
# 2023Q2    NaN
# 2023Q3    NaN
# 2023Q4    NaN
# 2024Q1    4.0
# 2024Q2    NaN
# 2024Q3    NaN
# 2024Q4    NaN
# 2025Q1    5.0
# 2025Q2    NaN
# 2025Q3    NaN
# 2025Q4    NaN
# Freq: Q-DEC, dtype: float64

#可以用先前學到的索引操作找到特定時間點的資料。
print(df['2021':'2023']) #取出'2021'列到'2023'列
# 2021    1
# 2022    2
# 2023    3
# Freq: A-DEC, dtype: int64

# 移動（shifting）指的是沿著時間軸將資料前移或後移。Series 和 DataFrame 都有一個 .shift() 方法用於執行單純的移動操作。
#

# 分時間資料以及字串差別，時間需要使用 pd.Timestamp() 做設定，並不是只使用字串就可以代表時間。
str_date = '2021-01-01'
date = pd.Timestamp(2021,1,1) #字串轉時間型態
print(str_date) 
#2021-01-01
print(type(str_date))
#<class 'str'>
print(date, type(date))
#2021-01-01 00:00:00 <class 'pandas._libs.tslibs.timestamps.Timestamp'>

#時間跟字串可以互相轉換
# 時間轉字串
# 字串轉時間
date_to_str = date.strftime('%Y-%m_%d') #時間轉字串
str_to_date = pd.to_datetime(str_date)  #字串轉時間
print((date_to_str, type(date_to_str)), (str_to_date, type(str_to_date)))
#('2021-01_01', <class 'str'>) (Timestamp('2021-01-01 00:00:00'), <class 'pandas._libs.tslibs.timestamps.Timestamp'>)

# 日期時間處理
# 接下來介紹 timestamps 的常用函數
# 直接呼叫出年月日，在 timestamps 後面加上回傳的 year, month, day 即可
print(date)
#2021-01-01 00:00:00
print(date.year, date.month, date.day) 
# 2021 1 1

#也可以呼叫星期與周數
# pandas.Series.dt.day_name
print(date.day_name())  #乎叫星期
#Friday 
print(date.weekofyear) #呼叫週數
#53  第53周
#為甚麼是第 53 周 ? 同學可以去查查台灣的月曆。

# Timestamps 可以直接加時間或是計算時間差距
date2 = pd.Timestamp(2021, 1 ,11)
print(date, date2)
# 021-01-01 00:00:00 2021-01-11 00:00:00
print(date2 - date)  #計算天數差距
#10 days 00:00:00
print(date + pd.Timedelta(days=10) == date2)  #date +10天是否等於day2
#True

#也可以加工作日天數
# 注意 : 因為 pd.offsets.BDay() 是工作日，所以在六、日套上這個函數不能直接往後算我們所指定的天數，以下面為例，原本日期為星期六，但後兩個工作日是星期二不是星期一 (加上一天)。
date += pd.Timedelta(days=1)    
some_b_day = 2 * pd.offsets.BDay()  # 設定兩天工作日
print(some_b_day)
#<2 * BusinessDays>
add_some_b_date = date + some_b_day # 把某日加上兩天工作日
print(date.day_name(), add_some_b_date.day_name())
# Saturday Tuesday

#時間序列的資料非常注重時間的間隔
# 時間序列的資料可以使用索引操作
# 時間資料可以加時間或是計算相差時間
# 時間資料可以呼叫年、月、日、第幾周、星期幾




#補充 : 轉各種期間的函數
import pandas as pd
import numpy as np
#pd.date_range():
date_rng = pd.date_range('2021-01-01', freq='M', periods=12)
print(f'month date_range()：\n{date_rng}')
# Saturday Tuesday
# month date_range()：
# DatetimeIndex(['2021-01-31', '2021-02-28', '2021-03-31', '2021-04-30',               '2021-05-31', '2021-06-30', '2021-07-31', '2021-08-31',               '2021-09-30', '2021-10-31', '2021-11-30', '2021-12-31'],
#               dtype='datetime64[ns]', freq='M')
date_rng = pd.date_range('2021-01-01', freq='W-SUN', periods=12)
print(f'week date_range()：\n{date_rng}')
# week date_range()：
# DatetimeIndex(['2021-01-03', '2021-01-10', '2021-01-17', '2021-01-24',
#                '2021-01-31', '2021-02-07', '2021-02-14', '2021-02-21',
#                '2021-02-28', '2021-03-07', '2021-03-14', '2021-03-21'],
#               dtype='datetime64[ns]', freq='W-SUN')
date_rng = pd.date_range('2021-01-01 00:00:00', freq='H', periods=12)
print(f'hour date_range()：\n{date_rng}')
# hour date_range()：
# DatetimeIndex(['2021-01-01 00:00:00', '2021-01-01 01:00:00',
#                '2021-01-01 02:00:00', '2021-01-01 03:00:00',
#                '2021-01-01 04:00:00', '2021-01-01 05:00:00',
#                '2021-01-01 06:00:00', '2021-01-01 07:00:00',
#                '2021-01-01 08:00:00', '2021-01-01 09:00:00',
#                '2021-01-01 10:00:00', '2021-01-01 11:00:00'],
#               dtype='datetime64[ns]', freq='H')

#pd.period_range()
period_rng = pd.period_range('2021/01/01', freq='M', periods=12)
print(f'month period_range()：\n{period_rng}')
# month period_range()：
# PeriodIndex(['2021-01', '2021-02', '2021-03', '2021-04', '2021-05', '2021-06',
#              '2021-07', '2021-08', '2021-09', '2021-10', '2021-11', '2021-12'],
#             dtype='period[M]', freq='M')
period_rng=pd.period_range('2021-01-01',freq='W-SUN',periods=12)
print(f'week period_range()：\n{period_rng}')
# week period_range()：
# PeriodIndex(['2020-12-28/2021-01-03', '2021-01-04/2021-01-10',
#              '2021-01-11/2021-01-17', '2021-01-18/2021-01-24',
#              '2021-01-25/2021-01-31', '2021-02-01/2021-02-07',
#              '2021-02-08/2021-02-14', '2021-02-15/2021-02-21',
#              '2021-02-22/2021-02-28', '2021-03-01/2021-03-07',
#              '2021-03-08/2021-03-14', '2021-03-15/2021-03-21'],
#             dtype='period[W-SUN]', freq='W-SUN') 
period_rng=pd.period_range('2021-01-01 00:00:00',freq='H',periods=12)
print(f'hour period_range()：\n{period_rng}')
# hour period_range()：
# PeriodIndex(['2021-01-01 00:00', '2021-01-01 01:00', '2021-01-01 02:00',
#              '2021-01-01 03:00', '2021-01-01 04:00', '2021-01-01 05:00',
#              '2021-01-01 06:00', '2021-01-01 07:00', '2021-01-01 08:00',
#              '2021-01-01 09:00', '2021-01-01 10:00', '2021-01-01 11:00'],
#             dtype='period[H]', freq='H')


print(pd.Timedelta(days=5, minutes=50, seconds=20, milliseconds=10, microseconds=10, nanoseconds=10))
# 5 days 00:50:20.010010010

now=pd.datetime.now()
dt=now+pd.Timedelta(days=50)
print(f'当前时间是{now}, 50天后时间是{dt}')
#当前时间是2019-06-08 17:59:31.726065, 50天后时间是2019-07-28 17:59:31.726065
#只显示年月日
print(dt.strftime('%Y-%m-%d')) #2019-07-28
# 当前时间是2021-04-22 12:59:58.061558, 50天后时间是2021-06-11 12:59:58.061558
# 2021-06-11


#定义timestamp
t1=pd.Timestamp('2019-01-10')
t2=pd.Timestamp('2018-12-10')
print(f't1= {t1}')
print(f't2= {t2}')
print(f't1与t2时间间隔：{(t1-t2).days}天')
# t1= 2019-01-10 00:00:00
# t2= 2018-12-10 00:00:00
# # t1与t2时间间隔：31天

per=pd.Period('2019')
print(f'pd.Period()：{per}')
# pd.Period()：2019
per_del=pd.Period('2019')-pd.Period('2018')
print(f'2019和2018间隔{per_del}年')#可以直接+、-整数（代表年）
#2019和2018间隔1年

#时期转换为时间戳
print(per.to_timestamp(how='end'))#2019-12-31 00:00:00
print(per.to_timestamp(how='start'))#2019-01-01 00:00:00
# pd.Period()：2019
# 2019和2018间隔<YearEnd: month=12>年
# 2019-12-31 23:59:59.999999999
# 2019-01-01 00:00:00

date=pd.date_range('1/1/2018', periods=20, freq='D')
tsdat_series=pd.Series(range(20),index=date)
tsp_series=tsdat_series.to_period('D')
print(tsp_series.index.asfreq('Q'))
# PeriodIndex(['2018Q1', '2018Q1', '2018Q1', '2018Q1', '2018Q1', '2018Q1',
#              '2018Q1', '2018Q1', '2018Q1', '2018Q1', '2018Q1', '2018Q1',
#              '2018Q1', '2018Q1', '2018Q1', '2018Q1', '2018Q1', '2018Q1',
#              '2018Q1', '2018Q1'],
#             dtype='period[Q-DEC]', freq='Q-DEC')

date=pd.date_range('1/1/2018', periods=20, freq='M')
tsdat_series=pd.Series(range(20),index=date)
tsp_series=tsdat_series.to_period('M')
print(tsp_series.index.asfreq('Q'))
# PeriodIndex(['2018Q1', '2018Q1', '2018Q1', '2018Q2', '2018Q2', '2018Q2',
#              '2018Q3', '2018Q3', '2018Q3', '2018Q4', '2018Q4', '2018Q4',
#              '2019Q1', '2019Q1', '2019Q1', '2019Q2', '2019Q2', '2019Q2',
#              '2019Q3', '2019Q3'],
#             dtype='period[Q-DEC]', freq='Q-DEC')

date=pd.period_range('1/1/2018', periods=20, freq='D')
tsper_series=pd.Series(range(20),index=date)
print(tsper_series.index.asfreq('Q'))
# PeriodIndex(['2018Q1', '2018Q1', '2018Q1', '2018Q1', '2018Q1', '2018Q1',
#              '2018Q1', '2018Q1', '2018Q1', '2018Q1', '2018Q1', '2018Q1',
#              '2018Q1', '2018Q1', '2018Q1', '2018Q1', '2018Q1', '2018Q1',
#              '2018Q1', '2018Q1'],
#             dtype='period[Q-DEC]', freq='Q-DEC')