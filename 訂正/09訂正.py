# 參考解答：方法二
import pandas as pd
d = [
    ['Austin', 139, 'Sun'],
    ['Dallas', 237, 'Sun'],
    ['Austin', 139, 'Mon'],
    ['Dallas', 456, 'Mon'],
]

df = pd.DataFrame(d, columns=['city', 'visitor', 'weekday'])
print(df)
#     city  visitor weekday
#0  Austin      139     Sun
#1  Dallas      237     Sun
#2  Austin      139     Mon
#3  Dallas      456     Mon

#訂正
#3. 承上題，假設你想知道每個 weekday 的平均 visitor 數量，可以怎麼做？
for day in set(df["weekday"]):
    print(day, df[df["weekday"] == day ]["visitor"].mean() )


#這邊是要透過for迴圈，計算並顯示每個不同的weekday--包含星期一(Mon)、星期日(Sun)--的visiter平均。
#所以在for 迴圈下 day會依序等於"Mon","Sun"
#print用逗號隔開，可以分別顯示出不同的變數，
#比如x=1 y=2 print(x,y) 會顯示出1,2。
#在這邊，前面就是印出當個迴圈的day等於什麼字串("Mon"或"Sun")，逗號後面就是印出平均的結果。
#df["weekday"]==day 這段是條件判斷式，用於判斷資料的weekday欄位是否屬於指定的weekday(Mon or Sun)，這段程式輸出是包含了 true 和 false的Series(類似一個true false 串列)。
#比如當day等於"Mon"時
#df["weekday"]==day 出來的結果是[false false true true]的series

#而當有了這樣的series，即可以用於做資料的篩選。
#當day等於"Mon"時df[df["weekday"]==day]即相當於df[[false false true true]]。
#df[df["weekday"]==day]的輸出會是weekday等於"Mon"的兩筆資料。

#df[df["weekday"] == day]["visitor"].mean()就是將這兩筆資料的visitor進行平均的意思
