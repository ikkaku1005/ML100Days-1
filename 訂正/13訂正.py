#   fruit  weight  price
#0   apple    high      3
#1  banana  medium      6
#2  orange     low      0
#3   apple    high      5
#4  banana  medium      1
#5  orange     low      2
#6   apple    high     12
#7  banana  medium     11
#8  orange     low      7

##    fruit weight  price
#0   apple   high      3
#1  orange    low      2
#2    pine   high     11
#3   apple    low      3
#4  orange   high     13
#5    pine    low      8

#df1.join(df2)
#columns overlap but no suffix specified: Index(['fruit', 'weight', 'price'], dtype='object')

#2. [簡答題] 承上題，請問為什麼依照 merge 合併後有些資料不見了？
#ANS:因為 merge 有預設的方法是兩邊同時存在才會合併，只存在一邊的資料就不見了。

#3. [簡答題] 承上題，請問為什麼依照 index 合併會發生錯誤？請用程式解決。
##ANS:因為原本的欄位重複，導致無法正確合併。
#df1.join(df2, lsuffix='_df1', rsuffix='_df2')