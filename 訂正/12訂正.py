#2. 請將 dataFrame 所有字串都變成是大寫開頭
#原作答
#x= df[[0,1,2]]
#print(df.str.title())
#dataframe no attribute to title

import pandas as pd
import numpy as np
df = pd.DataFrame([
    ['tom', 'mark', 'mary'],
    ['bob', 'alice', 'john']
])
print(df)
#     0      1     2
#0  tom   mark  mary
#1  bob  alice  john
print(df.applymap(lambda x: x.title()))
#     0      1     2
#0  Tom   Mark  Mary
#1  Bob  Alice  John
