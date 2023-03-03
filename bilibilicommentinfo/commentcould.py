import jieba
import  wordcloud
import pandas as pd

#  打开文件（保存 弹幕的 csv 文件）

df = pd.read_csv('BV1oS4y1i7VA_评论.csv',encoding= 'utf-8',header=None)
df.columns = ['时间','点赞','评论']
col_data_1 = df['评论']
#print(col_data_1)
txt_list = jieba.lcut(str(col_data_1))


# 接下来 理解为  将其这些内容 拼接为  完整的  字符串
string = ' '.join(txt_list)
#print(string)

#  创建对象 填写参数
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='white',  #  背景颜色
                        font_path='msyh.ttc',   #  字体
                        scale=15, # 间隔
                        stopwords={' ','?','!',','},  # 停用词  剔除不需要显示的字符
                        contour_width=5,                #  整个内容显示的宽度
                        contour_color='red',      #  内容显示的颜色 红色边境
)

w.generate(string)  #  传入处理好的字符窜
photo_path = r'G:\pythonProject\bilibili\bilibilicommentinfo\词云图片\BV1oS4y1i7VA.jpg'
w.to_file(photo_path)  #  保存

