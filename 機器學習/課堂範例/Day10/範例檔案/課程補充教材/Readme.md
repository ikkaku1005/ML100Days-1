# D10：數值型特徵 - 去除離群值









## 補充資料

###  **標準化是什麼?**

簡單來說，就是將特徵值縮放成一個特定區間內的值，像是我把班上所有同學的身高與體重的值用0~1區間的值替代，也就是縮放到0~1區間的意思喔

### **為什麼要標準化?**

通常我們的數據包含了許許多多的特徵資料，而這些特徵所代表的數值意義卻是截然不同的，像是體重的25(公斤)，跟身高的180(公分)，如果單以數值來講180大於25，但是它們的特徵意義不同，可以這樣比較嗎?所以我們必須將這些特徵值縮放到一個特定區間內，才能進行比較



#### **Z-Score: 將數據呈現正態分佈（或稱常態	`分佈）與中心化**

- 說明： 進行Z-Score標準化後，數據會呈正態分佈，並且會將數據縮放成平均為0，平方差為1的數據

**Min-Max線性歸一化** 

- 說明： 進行Min-Max標準化後，因為計算公式的關係，當X為最大值時，標準差就為1，最小值轉化為0，所以我們的數據將會縮放到0～1之間喔，這樣的方式使我們的數據分佈型態不會有變化喔





### Machine Learning - 資料預處理- 特徵工程- 標準化(Standard Scaler) 公式教學與Python程式碼實作教學

https://matters.news/@CHWang/machine-learning-%E8%B3%87%E6%96%99%E9%A0%90%E8%99%95%E7%90%86-%E7%89%B9%E5%BE%B5%E5%B7%A5%E7%A8%8B-%E6%A8%99%E6%BA%96%E5%8C%96-standard-scaler-%E5%85%AC%E5%BC%8F%E6%95%99%E5%AD%B8%E8%88%87python%E7%A8%8B%E5%BC%8F%E7%A2%BC%E5%AF%A6%E4%BD%9C%E6%95%99%E5%AD%B8-bafyreihd2uc5clmc7kzzswuhvfd56axliecfzxlk5236o54cvvcphgumzu





###　Machine Learning - 標準化（StandardScaler）- 快速完成數據標準化 - Sklearn 套件教學

https://matters.news/@CHWang/machine-learning-%E6%A8%99%E6%BA%96%E5%8C%96-standard-scaler-%E5%BF%AB%E9%80%9F%E5%AE%8C%E6%88%90%E6%95%B8%E6%93%9A%E6%A8%99%E6%BA%96%E5%8C%96-sklearn-%E5%A5%97%E4%BB%B6%E6%95%99%E5%AD%B8-bafyreibpusofl5b3tt43ovknw2mnjzrmekfldelelyl33luzkfzc4k6loy



