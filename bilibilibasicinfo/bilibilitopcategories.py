# -*- coding: utf-8 -*-
import requests as rq, json as js
import csv

datalist = []
for page in range(1,5):
    # 1.获取html文件
    r = rq.get('https://api.bilibili.com/x/web-interface/popular?ps=50&pn={}'.format(page))
    # 2. 设置对于的编码方式
    r.encoding = r.apparent_encoding
    # 3. 将已编码的 JSON 字符串解码为 Python 对象即字典
    data = js.loads(r.content.decode('utf8'))['data']['list']
    #print('hhhh'),用来测试是否进入循环
    # 4. 遍历字符串信息，d为字典型
    #print(data)
    for d in data:
        count = []
        count.append(d['title'])             # 标题
        count.append(d['tname'])             # 类型
        count.append(d['owner']['name'])     # up主名字
        count.append(d['stat']['view'])      # 播放量
        count.append(d['stat']['reply'])     # 评论
        count.append(d['stat']['like'])      # 点赞
        count.append(d['stat']['coin'])      # 投币
        count.append(d['stat']['favorite'])  # 收藏
        count.append(d['stat']['share'])     # 分享
        datalist.append(count)



s = set()                   #set创建一个无序不重复元素集
for i in data:              #遍历循环字典
    s.add(i['tname'])       #这样就能获取到所有不重复的电影类型
    print(i['tname'])
csvfile = open('bilibili热门分类.csv', 'w', newline='',encoding="utf-8-sig")#打开文件，没有则创建

writer = csv.writer(csvfile)
writer.writerow(['分类', '视频', '类型', '点赞', '评论','综合评分'])
list = []
for i in s:
    for d in data:
            t = (i, d["title"], d["tname"],
            d['stat']['like'],
            d['stat']['reply'],(d['stat']['like']*0.3 +d['stat']['reply']*0.7))
            list.append(t)
#这里开始就是对视频类型的排序
    for j in range(len(list) - 1, 0, -1):
        if (list[j - 1][0] != i):
            #print(list[j-1][0])
            break
        if (list[j - 1][4] < list[j][4]):
            # print(list[j - 1][4],list[j][4])
            tmp = list[j - 1]
            list[j - 1] = list[j]
            list[j] = tmp
writer.writerows(list)
csvfile.close()

csvfile = open('bilibili热门分类-1.csv', 'w', newline='',encoding="utf-8")#打开文件，没有则创建
writer = csv.writer(csvfile)
writer.writerow([ '视频', '类型', '点赞', '评论','综合评分'])
list1 = []

for d in data:
        t = ( d["title"], d["tname"],
        d['stat']['like'],
        d['stat']['reply'],(d['stat']['like']*0.3 +d['stat']['reply']*0.7))
        list1.append(t)
# print(list1[0][4])
b=sorted(list1,key=lambda x:x[4],reverse=True)

writer.writerows(b)
csvfile.close()
