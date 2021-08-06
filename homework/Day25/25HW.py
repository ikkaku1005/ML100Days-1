# 更改 Projection 的設定繪製出地球儀圖形

# 當 "projection" 參數為“ortho"時，所得圖位地球儀截面

# 當 "projection" 參數為“Mill"時，所得平展位面

# 查看 resolution / 經緯度座標的繪圖精細度

# 載入套件
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
# 創建基本地圖。
# 當 "projection" 參數為“ortho"時，所得圖位地球儀截面

#由此開始寫code 

#設定圖形大小
plt.figure()

#設定投影型態
m=Basemap(projection = 'ortho', lat_0 = 0, lon_0 = 0)

#設定圖形顏色, 選用NASA 寶石藍輸出 
m.bluemarble()

#秀圖
plt.show()



# 由此開始寫code 

#設置Lambert保形底圖。

# width=12000000,height=9000000
# plt.figure( width= 12000000,height=9000000)
#經緯度lat_1=45.,lat_2=55,lat_0=50,lon_0=-107
#set resolution = None跳過邊界數據集的處理
# projection='lcc'
m = Basemap(projection = 'lcc',lat_1=45.,
           lat_2=55,lat_0=50,lon_0=-107, resolution = None
           ,width= 12000000,height=9000000)

#選用NASA 寶石藍輸出 
m.bluemarble()

#秀圖
plt.show()


#由此開始寫code 
#  "projection" 參數為“Mill"
# 設定經緯座標
# 左下角的緯度 - llcrnrlat = -90,
# 左下角的經度 - llcrnrlon = -180,
# 右上角的緯度 - urcrnrlat = 90,
# 右上角的經度 -urcrnrlon = 180

# 成圖設定resolution


m = Basemap(projection = "mill" ,llcrnrlat = -90,llcrnrlon = -180, urcrnrlat = 90
            ,resolution = None, urcrnrlon = 180) # 成圖設定resolution 

#創建邊線
m.drawcoastlines()
#畫出國家，並使用線寬為2 的線條生成分界線。
m.drawcountries(linewidth= 2)
#畫出州界
m.drawstates(color='b')
#畫出城市
m.drawcounties(color='darkred')

plt.title('Basemap Tutorial')
plt.show()
