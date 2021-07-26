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
    print(day,df[df["weekday"] == day]["visitor"].mean() )
