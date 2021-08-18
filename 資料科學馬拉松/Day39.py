# library
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import math
import statistics
import seaborn as sns
from IPython.display import display
import sklearn
print(sklearn.__version__)
#如果只有 0.19 記得要更新至 最新版本


#用字典產生一組資料
data={'sex': ['Male','Male','Male','Male','Male','Female','Female','Female','Female','Female','Male','Male','Male','Male','Male','Female','Female','Female','Female','Female'],
      'insomnia':['Y','N','N','N','N','N','Y','Y','Y','N','Y','N','N','N','N','N','Y','Y','Y','N'],
     'age':[23,40,5,30,1,40,16,27,43,8,23,39,5,29,1,42,13,29,41,10],
     'height':[180,170,100,176,70,160,170,166,155,35,170,168,101,175,72,163,169,163,151,40],
     'weight':[100,68,20,70,10,45,50,58,58,17,101,65,22,79,12,40,53,52,56,14]}
#轉成 dataframe格式 
data=pd.DataFrame(data)
display(data)

print(data.info())

cat_features = []
for dtype, feature in zip(data.dtypes, data.columns):
    if dtype == 'object':
        cat_features.append(feature)
print(f'{len(cat_features)} category Features : {cat_features}\n')

# 連續 vs 連續
# 本範例透過 Pearson相關係數，看身高和體重相關性
# 由於 pearsonr 有兩個回傳結果，我們只需取第一個回傳值為相關係數
corr, _=stats.pearsonr(data['height'], data['weight'])
print(corr)
#代表身高和體重有高度線性相關
g = sns.regplot(x="height", y="weight", color="g",data=data)
#年齡和身高有關連
plt.show()

# 離散 vs 離散
# 本範例透過 Cramér's V ，看失眠的狀態和性別相關性
#如果沒有安裝過，先把下一行程式碼打開，先安裝套件 
#!pip install researchpy
import researchpy  
contTable = pd.crosstab(data['sex'], data['insomnia'])
print(contTable)
# step1: 用交叉列連表(contingency table)，來整理兩個類別型的資料
contTable = pd.crosstab(data['sex'], data['insomnia'])
print(contTable)

#Step2:計算資料自由度 df*
df = min(contTable.shape[0], contTable.shape[1]) - 1
print(df)

# Step3:運用 researchpy 套件，計算出 Cramer’s V 係數
crosstab, res = researchpy.crosstab(data['sex'], data['insomnia'], test='chi-square')
#print(res)
print("Cramer's value is",res.loc[2,'results'])
## 寫一個副程式判斷相關性的強度
def judgment_CramerV(df,V):
    if df == 1:
        if V < 0.10:
            qual = 'negligible'
        elif V < 0.30:
            qual = 'small'
        elif V < 0.50:
            qual = 'medium'
        else:
            qual = 'large'
    elif df == 2:
        if V < 0.07:
            qual = 'negligible'
        elif V < 0.21:
            qual = 'small'
        elif V < 0.35:
            qual = 'medium'
        else:
            qual = 'large'
    elif df == 3:
        if V < 0.06:
            qual = 'negligible'
        elif V < 0.17:
            qual = 'small'
        elif V < 0.29:
            qual = 'medium'
        else:
            qual = 'large'
    elif df == 4:
        if V < 0.05:
            qual = 'negligible'
        elif V < 0.15:
            qual = 'small'
        elif V < 0.25:
            qual = 'medium'
        else:
            qual = 'large'
    else:
        if V < 0.05:
            qual = 'negligible'
        elif V < 0.13:
            qual = 'small'
        elif V < 0.22:
            qual = 'medium'
        else:
            qual = 'large'
    return(qual)

judgment_CramerV(df,res.loc[2,'results'])
print(judgment_CramerV(df,res.loc[2,'results']))

# 此案例的失眠狀態和性別這兩個變數，呈現中度相關
# 搭配圖形觀察
g= sns.countplot(x="sex", hue="insomnia", data=data)
plt.show()

# 離散 vs 連續 Eta Squared(η2)
# 本範例透過 Eta Squared ，看失眠的狀態和體重相關性
import pingouin as pg
# Step1: 取出失眠和體重資料
# Step2:運用 pg.anova 計算三種變異數
aov = pg.anova(dv='weight', between='insomnia', data=data, detailed=True)
print(aov)
# Step3:變異數換算得到 Eta Squared (𝜼^𝟐)
etaSq = aov.SS[0] / (aov.SS[0] + aov.SS[1])
print(etaSq )
def judgment_etaSq(etaSq):
    if etaSq < .01:
        qual = 'Negligible'
    elif etaSq < .06:
        qual = 'Small'
    elif etaSq < .14:
        qual = 'Medium'
    else:
        qual = 'Large'
    return(qual)
judgment_etaSq(etaSq)
print(judgment_etaSq(etaSq))
# 搭配圖形來檢視
# 這邊使用小提琴圖示法
g = sns.catplot(x="insomnia", y="weight", hue="insomnia",
               data=data, kind="violin")
plt.show()