import requests as rq, json as js
import xlwt
import sqlite3  # 进行SQLite数据库操作

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

#print(datalist)
#print("-----------------------------------------------")
b=sorted(datalist,key=lambda x:x[3],reverse=True)
print((b))




