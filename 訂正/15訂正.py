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
                         [15,89,67,77,'girl',3]],
                        columns=['student_id','math_score','english_score','chinese_score','sex','class'])
print(score_df )
#    student_id  math_score  english_score  chinese_score   sex  class
#0            1          50             80             70   boy      1
#1            2          60             45             50   boy      2
#2            3          98             43             55   boy      1
#3            4          70             69             89   boy      2
#4            5          56             79             60  girl      1
#5            6          60             68             55  girl      2   
#6            7          45             70             77  girl      1   
#7            8          55             77             76  girl      2   
#8            9          25             57             60  girl      1   
#9           10          88             40             43  girl      3   
#10          11          25             60             45   boy      3   
#11          12          80             60             23   boy      3   
#12          13          20             90             66  girl      3   
#13          14          50             50             50  girl      3   
#14          15          89             67             77  girl      3  

#將索引(index)依序改為sex、class、student_id，欄位依序改成chinese_score、english_score、math_score
df = score_df.melt(id_vars = ['sex','class','student_id'])  #將sex、class、student_id 三欄固定不動，其他改為variable、value，欄位改為欄位值
#     sex  class  student_id       variable  value
#0    boy      1           1     math_score     50
#1    boy      2           2     math_score     60
#2    boy      1           3     math_score     98
#3    boy      2           4     math_score     70
#4   girl      1           5     math_score     56
#5   girl      2           6     math_score     60
#6   girl      1           7     math_score     45
#7   girl      2           8     math_score     55
#8   girl      1           9     math_score     25
#9   girl      3          10     math_score     88
#10   boy      3          11     math_score     25
#11   boy      3          12     math_score     80
#12  girl      3          13     math_score     20
#13  girl      3          14     math_score     50
#14  girl      3          15     math_score     89
#15   boy      1           1  english_score     80
#16   boy      2           2  english_score     45
#17   boy      1           3  english_score     43
#18   boy      2           4  english_score     69
#19  girl      1           5  english_score     79
#20  girl      2           6  english_score     68
#21  girl      1           7  english_score     70
#22  girl      2           8  english_score     77
#23  girl      1           9  english_score     57
#24  girl      3          10  english_score     40
#25   boy      3          11  english_score     60
#26   boy      3          12  english_score     60
#27  girl      3          13  english_score     90
#28  girl      3          14  english_score     50
#29  girl      3          15  english_score     67
#30   boy      1           1  chinese_score     70
#31   boy      2           2  chinese_score     50
#32   boy      1           3  chinese_score     55
#33   boy      2           4  chinese_score     89
#34  girl      1           5  chinese_score     60
#35  girl      2           6  chinese_score     55
#36  girl      1           7  chinese_score     77
#37  girl      2           8  chinese_score     76
#38  girl      1           9  chinese_score     60
#39  girl      3          10  chinese_score     43
#40   boy      3          11  chinese_score     45
#41   boy      3          12  chinese_score     23
#42  girl      3          13  chinese_score     66
#43  girl      3          14  chinese_score     50
print(df.pivot_table(index = ['sex','class','student_id'], columns = 'variable', values = 'value'))
#variable                    chinese_score   english_score  math_score
#sex class  student_id
#boy  1     1                      70             80          50       
#           3                      55             43          98       
#     2     2                      50             45          60       
#           4                      89             69          70
#     3     11                     45             60          25
#           12                     23             60          80
#girl 1     5                      60             79          56
#           7                      77             70          45
#           9                      60             57          25
#     2     6                      55             68          60
#           8                      76             77          55
#     3     10                     43             40          88
#           13                     66             90          20
#           14                     50             50          50
#           15                     77             67          89
