# -*- coding= utf-8 -*-
import jieba#分词
from matplotlib import pyplot as plt#绘图，数据可视化
from wordcloud import WordCloud
from PIL import Image #处理图像，python自带
import numpy as np#矩阵运算
import sqlite3#数据库


#准备词云所需文字
con = sqlite3.connect('bilibili.db')
#con = sqlite3.connect('bilibili.db')
cur = con.cursor()
sql  = 'select title from bilibili200'
data = cur.execute(sql)
text = ""
for item in data:
    #print(item[0])
    text = text + item[0]
#print(text)
cur.close()
con.close()
#分词

cut = jieba.cut(text)
string = ' '.join(cut)
print(len(string))
#
# #
img = Image.open(r'G:\pythonProject\bilibili\bilibilibasicinfo\static\assets\img\tree.jpg')#打开遮罩图片
img_array = np.array(img)#将图片转为数组
wc = WordCloud(
    background_color='white',
    mask = img_array,
    font_path='msjhbd.ttc'
)
wc.generate_from_text(string)



#绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')#是否显示坐标轴



plt.savefig(r'G:\pythonProject\bilibili\bilibilibasicinfo\static\assets\img\bilibili.jpg',dpi=500)