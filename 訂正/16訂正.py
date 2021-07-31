import pandas as pd
import numpy as np
score_df = pd.DataFrame([[1,50,80,70,'boy',1], 
              [2,60,45,50,'boy',2],
              [3,98,43,55,'boy',1],
              [4,70,69,89,'boy',2],
              [5,56,79,60,'girl',1],
              [6,60,68,55,'girl',2],
              [7,45,70,77,'girl',1],
              [8,55,77,76,'girl',2],
              [9,25,57,60,'girl',1],
              [10,88,40,43,'girl',3],
              [11,25,60,45,'boy',3],
              [12,80,60,23,'boy',3],
              [13,20,90,66,'girl',3],
              [14,50,50,50,'girl',3],
              [15,89,67,77,'girl',3]],columns=['student_id','math_score','english_score','chinese_score','sex','class'])
# 	student_id	math_score	english_score	chinese_score	sex	 class
# 0	     1    	   50	          80	       70	        boy	    1
# 1	     2	       60	          45	       50	        boy	    2
# 2	     3	       98	          43	       55	        boy	    1
# 3	     4	       70	          69	       89	        boy	    2
# 4	     5	       56	          79	       60	        girl	1
# 5	     6	       60	          68	       55	        girl	2
# 6	     7	       45	          70	       77	        girl	1
# 7	     8	       55	          77	       76	        girl	2
# 8	     9	       25	          57	       60	        girl	1
# 9	    10	       88	          40	       43	        girl	3
# 10	11	       25	          60	       45	        boy	    3
# 11	12	       80	          60	       23	        boy	    3
# 12	13	       20	          90	       66	        girl	3
# 13	14	       50	          50	       50	        girl	3
# 14	15	       89	          67	       77	        girl	3
#3.分析全校女生與男生國文平均差幾分?
#原作答
x = score_df.melt(id_vars = 'sex',value_vars = 'chinese_score')  #sex欄的欄位值不動，chinese_score的欄位轉為欄位值
print(x)
#      sex       variable  value
# 0    boy  chinese_score     70
# 1    boy  chinese_score     50
# 2    boy  chinese_score     55
# 3    boy  chinese_score     89
# 4   girl  chinese_score     60
# 5   girl  chinese_score     55
# 6   girl  chinese_score     77
# 7   girl  chinese_score     76
# 8   girl  chinese_score     60
# 9   girl  chinese_score     43
# 10   boy  chinese_score     45
# 11   boy  chinese_score     23
# 12  girl  chinese_score     66
# 13  girl  chinese_score     50
# 14  girl  chinese_score     77
print(x.pivot_table(index = 'sex',columns = 'variable',values = 'value'))
# variable  chinese_score
# sex                    
# boy           55.333333
# girl          62.666667
y = x.pivot_table(index = 'sex',columns = 'variable',values = 'value')
print("全校女生與男生國文平均差",y.iat[1,0]-y.iat[0,0],"分")  #.iat[1,0]取出第一列、第0欄的欄位值:62.666667


#參考解答
#女生平均62.666667分，男生平均55.333333分，相差7.333333999999994分
df = score_df.groupby('sex').apply(lambda x: x.mean())  #f(x) = x.mean
print(df)
#       student_id  math_score  english_score  chinese_score     class
# sex
# boy     5.500000   63.833333      59.500000      55.333333  2.000000  
# girl    9.666667   54.222222      66.444444      62.666667  2.111111
print(df['chinese_score'][1]-df['chinese_score'][0])
