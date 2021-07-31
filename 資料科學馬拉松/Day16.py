#D16：用 Pandas 執行聚合運算(Split-Apply-Combine Strategy)
#認識 groupby
#在數據分析中時常會分析不同族群的資料，例如，學生分數資料(如表 1)，你想分析男生與女生的各科差異，前幾天有教到檢索可以將資料分成男生資料與女生資料，在將各資料算平均值(如圖 2)，在這裡有一個函數 goupby 可以一行指令執行以上的邏輯(下圖 3)。
#你的 dataframe 變數名稱.groupby(['要分析之行的名稱']).運算函數名稱()
import pandas as pd
score_df = pd.DataFrame([[1,50,80,70,'boy'], 
              [2,60,45,50,'boy'],
              [3,98,43,55,'boy'],
              [4,70,69,89,'boy'],
              [5,56,79,60,'girl'],
              [6,60,68,55,'girl'],
              [7,45,70,77,'girl'],
              [8,55,77,76,'girl'],
              [9,25,57,60,'girl'],
              [10,88,40,43,'girl']],columns=['student_id','math_score','english_score','chinese_score','sex'])
score_df = score_df.set_index('student_id')
#             math_score  english_score  chinese_score   sex
# student_id
# 1                   50             80             70   boy
# 2                   60             45             50   boy
# 3                   98             43             55   boy
# 4                   70             69             89   boy
# 5                   56             79             60  girl
# 6                   60             68             55  girl
# 7                   45             70             77  girl
# 8                   55             77             76  girl
# 9                   25             57             60  girl
# 10                  88             40             43  girl
##運用索引將資料分開再取平均
boy_score_df = score_df.loc[score_df.sex=='boy']
girl_score_df = score_df.loc[score_df.sex=='girl']
print(boy_score_df.mean())
# math_score       69.50
# english_score    59.25
# chinese_score    66.00
# dtype: float64
print(girl_score_df.mean())
# math_score       54.833333
# english_score    65.166667
# chinese_score    61.833333
# dtype: float64
print(score_df.groupby('sex').mean())#運用groupby方法值接取平均
#       math_score  english_score  chinese_score
# sex
# boy    69.500000      59.250000      66.000000
# girl   54.833333      65.166667      61.833333
score_df['class'] = [1,2,1,2,1,2,1,2,1,2] #新增欄位class
print(score_df)
#             math_score  english_score  chinese_score   sex  class
# student_id
# 1                   50             80             70   boy      1     
# 2                   60             45             50   boy      2     
# 3                   98             43             55   boy      1     
# 4                   70             69             89   boy      2     
# 5                   56             79             60  girl      1     
# 6                   60             68             55  girl      2     
# 7                   45             70             77  girl      1     
# 8                   55             77             76  girl      2     
# 9                   25             57             60  girl      1     
# 10                  88             40             43  girl      2  

#認識 Split-Apply-Combine 策略
#以剛剛學生資料來分解一下 groupby 的邏輯過程
#Split：將大的數據集拆成可獨立計算的小數據集(拆成男生、女生資料)
#Apply：獨立計算各個小數據集(成績取平均)
#Combine：將小數據集運算結果合併

#將 DataFrame 依照Ａ、B 、C 拆成三個小數據集[split]，各自計算總合[Apply]，合併結果輸出[Combine]
#拆分成 Ａ、B 、C 小數據集的方法為 groupby

#Groupby 針對多個欄位做分析
#Groupby 也可以針對多個欄位做分析，例如，學生成績資料多一欄位 c 班級(class)，想對班級以及性別做分類，在 groupby 中加入兩個欄位名稱即可(如下圖)，此時 groupby 自動會生成多維度索引(multiple index)
#你的 dataframe 變數名稱.groupby(['要分析之行的名稱','可以多個']).運算函數名稱()
print(score_df.groupby(['sex','class']).mean()) #Groupby也可以針對多個欄位做分析
#             math_score  english_score  chinese_score
# sex  class
# boy  1       74.000000      61.500000      62.500000
#      2       65.000000      57.000000      69.500000
# girl 1       42.000000      68.666667      65.666667
#      2       67.666667      61.666667      58.000000

#Groupby 針對欄位做多個分析
#Groupby也可以針對欄位做多個分析，例如，學生成績資料，想針對性別做成績平均以及標準差的計算，在 groupby 後加入 agg() (如下圖)，在 agg 中加入計算的邏輯(mean,std)，此時 groupby 自動會生成多維度欄位(multiple columns)
#注意 agg() 中要給的是函數名稱而非函數，所以在函數名稱後面不用加 ()。
print(score_df.groupby(['sex']).agg(['mean','std'])) #Groupby也可以針對欄位做多個分析
# 	         math_score	           english_score	       chinese_score	        class
#           mean	std	         mean	      std        mean	     std	    mean      std
# sex								
# boy	69.500000	20.680103	59.250000	18.191115	66.000000	17.530925	1.5 	0.577350
# girl	54.833333	20.566153	65.166667	14.579666	61.833333	12.952477	1.5	    0.547723

#Groupby 同時針對多個欄位做多個分析
#Groupby 也可以同時針對多個欄位做多個分析，例如，學生成績資料，想針對性別、班級做成績平均以及最高分的計算
#合併了多欄位以及多分析
#你的 dataframe 變數名稱.groupby(['要分析之行的名稱','可以多個']).agg(['運算函數名稱','可以多個運算函數'])
print(score_df.groupby(['sex','class']).agg(['mean','max']))#Groupby也可以同時針對多個欄位做多個分析
# 	    	  math_score      english_score	   chinese_score
#              mean	    max    mean  	max	   mean	     max
# sex class						
# boy	1	74.000000	98	 61.500000	80	 62.500000	 70
#       2	65.000000	70	 57.000000	69	 69.500000	 89
# girl	1	42.000000	56	 68.666667	79	 65.666667	 77
#       2	67.666667	88	 61.666667	77	 58.000000	 76


#知識點回顧
#Groupby 可以拆成:
#1.Split：將大的數據集拆成可獨立計算的小數據集
#2.Apply：獨立計算各個小數據集
#3.Combine：將小數據集運算結果合併
#Groupby 可以同時針對多個欄位做多個分析
