#資料網址 :https://raw.githubusercontent.com/aniruddhachoudhury/Red-Wine-Quality/master/winequality-red.csv
#1 - 固定酸度 2 - 揮發性酸度 3 - 檸檬酸 4 - 殘糖 5 - 氯化物 6 - 遊離二氧化硫 7 - 總二氧化硫 8 - 密度 9 - pH值 10 - 硫酸鹽 11 - 酒精度 輸出變數（基於感官資料）： 12 - 品質（分數在0到10之間）
#2. 請根據 Kaggle 文件瞭解 winequality-red 資料中所有欄位的定義為何？

#先利用pandas讀取資料
import pandas as pd
import numpy as np
df = pd.read_csv('https://raw.githubusercontent.com/aniruddhachoudhury/Red-Wine-Quality/master/winequality-red.csv')
#再利用pandas的info()函數瞭解資料的欄位定義
df.info()
#3. 請問在該資料的總共有多少欄位？哪一欄位是我們所要的目標欄位？
#資料總共有12個欄位，目標欄位為quality

#4. 請你嘗試觀察每一個「特徵」欄位（除 quality 外）資料的分佈情況，有看出什麼結果嗎？
#利用pandas的describe()函數觀察資料的分佈情況
df.describe()
#print(df.describe())
#可以看出資料的分佈情況，例如：fixed acidity的平均值為8.319637，標準差為1.741096，最小值為4.600000，最大值為15.900000
#幫我分析各個特徵欄位的分佈情況
#fixed acidity的平均值為8.319637，標準差為1.741096，最小值為4.600000，最大值為15.900000
#volatile acidity的平均值為0.527821，標準差為0.179060，最小值為0.120000，最大值為1.580000
#citric acid的平均值為0.270976，標準差為0.194801，最小值為0.000000，最大值為1.000000
#residual sugar的平均值為2.538806，標準差為1.409928，最小值為0.900000，最大值為15.500000
#chlorides的平均值為0.087467，標準差為0.047065，最小值為0.012000，最大值為0.611000
#free sulfur dioxide的平均值為15.874922，標準差為10.460157，最小值為1.000000，最大值為72.000000
#total sulfur dioxide的平均值為46.467792，標準差為32.895324，最小值為6.000000，最大值為289.000000
#density的平均值為0.996747，標準差為0.001887，最小值為0.990070，最大值為1.003690
#pH的平均值為3.311113，標準差為0.154386，最小值為2.740000，最大值為4.010000
#sulphates的平均值為0.658149，標準差為0.169507，最小值為0.330000，最大值為2.000000
#alcohol的平均值為10.422983，標準差為1.065668，最小值為8.400000，最大值為14.900000
#quality的平均值為5.636023，標準差為0.807569，最小值為3.000000，最大值為8.000000
#綜上的標準差與平均值可以如何理解這些分布狀況
#標準差越大，資料的分佈越分散，反之亦然
#這份資料集中，各個特徵欄位的標準差都不大，代表資料的分佈都不是很分散，而是集中在平均值附近


#4. 請你嘗試觀察每一個「標籤」欄位（quality）資料的分佈情況，有看出什麼結果嗎？
#幫我用熱點繪圖
import matplotlib.pyplot as plt
import seaborn as sns
sns.heatmap(df.corr(), annot=True, cmap='RdBu_r')
plt.show()
#幫我分析各個標籤欄位的分佈情況
