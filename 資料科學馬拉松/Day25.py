# 導入開發套件
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

# 新建地圖
map = Basemap()  #Basemap有很多屬性，這里全都使用默認参數

# 畫圖
map.drawcoastlines()

# 顯示结果
plt.show()

# 存储结果
plt.savefig('test.png')

# 導入開發套件
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# 新建地圖
map = Basemap(projection='merc' ,llcrnrlon=-180, urcrnrlon=180, llcrnrlat=-80, urcrnrlat=80)
# 經度 : longitude 、 緯度 : latitude
# llcrnrlon – 左下角的經度。
# urcrnrlon – 右上角的經度。
# llcrnrlat – 左下角的緯度。
# urcrnrlat – 右上角的緯度。
# 畫圖
map.drawcoastlines()

# 顯示结果
plt.show()
# 存储结果
plt.savefig('test.png')


###############################################################

import mpl_toolkits.basemap
print(mpl_toolkits.basemap.supported_projections)

map = Basemap(projection = 'ortho', lat_0 = 0, lon_0 = 0)
#’ortho’指正射投影，後面两個参數是设置中心點

# 给整個地圖上藍色
map.drawmapboundary(fill_color = 'aqua')

# 给陸地塗上珊瑚色，湖泊塗上藍色
map.fillcontinents(color = 'coral', lake_color = 'aqua')

# 畫圖
map.drawcoastlines()

# 顯示结果
plt.show()


#################################################################
# 新建地圖
map = Basemap(projection='merc',urcrnrlat=80, llcrnrlat=-80,llcrnrlon=-180, urcrnrlon=180)  #Basemap有很多屬性，這里全都使用默認参數

# 畫圖
map.drawcoastlines()

map.drawparallels(range(-90,91,30), color='#CCCCCC')
map.drawmeridians(range(-180,181,60), color='#CCCCCC')

#畫出州。
map.drawstates(color='b') 

# 畫出城市
map.drawcountries(color='darkred')

# 劃出海的顏色
map.drawmapboundary(fill_color='aqua')

# 劃出陸地的顏色
map.fillcontinents(color = 'coral')

# 顯示结果
plt.show()
############################################
# 加入經緯度的座標
# 獲得它們的實際座標開始, 坐標需要轉換，其中西經和南緯坐標是負值，北緯和東經坐標是正值。 例如，紐約市是北緯40.7127西經74.0059。我們可以在我們的程序中定義這些座標，如： NYClat, NYClon = 40.7127, -74.0059  

# 將這些轉換為要繪製的x和y座標。 xpt, ypt = m(NYClon, NYClat) 現在已經將座標順序翻轉為lon, lat（緯度，經度）。

# 座標通常以lat, lon順序給出。 然而，在圖形中，lat, long轉換為y, x，我們顯然不需要。在某些時候，必須翻轉它們。

# 最後，我們可以繪製如下的坐標： map.plot(xpt, ypt, 'c*', markersize=15)

def draw_map(m, scale=0.2):
      # 繪製一個陰影浮雕的地理圖像
    m.shadedrelief(scale=scale)

    # 經度與緯度將會以字典的形式返回
    lats = m.drawparallels(np.linspace(-90, 90, 13))
    lons = m.drawmeridians(np.linspace(-180, 180, 13))

    # 運用 plt.Line2D 實例設置經緯線
    lat_lines = chain(*(tup[1][0] for tup in lats.items()))
    lon_lines = chain(*(tup[1][0] for tup in lons.items()))
    all_lines = chain(lat_lines, lon_lines)

    # 通過迴圈設置所有線條的樣式
    for line in all_lines:
        line.set(linestyle='-', alpha=0.3, color='w')
    plt.show()


    #####################

    import numpy as np
from itertools import chain

#運用 "itertools" 庫中的 "chain" 模組，可以繪製更接近於生活中所見世界地圖的圖像
fig = plt.figure(figsize=(8, 6), edgecolor='w')
m = Basemap(projection='cyl', resolution=None,
            llcrnrlat=-90, urcrnrlat=90,
            llcrnrlon=-180, urcrnrlon=180, )
# 繪製一個陰影浮雕的地理圖像
m.shadedrelief(scale=0.2)

# 經度與緯度將會以字典的形式返回
lats = m.drawparallels(np.linspace(-90, 90, 13))
lons = m.drawmeridians(np.linspace(-180, 180, 13))

# 運用 plt.Line2D 實例設置經緯線
lat_lines = chain(*(tup[1][0] for tup in lats.items()))
lon_lines = chain(*(tup[1][0] for tup in lons.items()))
all_lines = chain(lat_lines, lon_lines)

# 通過迴圈設置所有線條的樣式
for line in all_lines:
    print(type(line))
    line.set(linestyle='-', alpha=0.3, color='w')
plt.show()

lats
for i,j in lats.items():
    print(j[0])

        # Basemap 函數的 "projection" 參數值調整為 'moll' ，此時，可以得到一張橢圓形的世界地圖
fig = plt.figure(figsize=(8, 8), edgecolor='w')
m = Basemap(projection='moll', resolution=None,
            lat_0=0, lon_0=0)

# 從 plt.show 改成 draw_map
draw_map(m)