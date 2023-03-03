import requests as rq, json as js
import xlwt
import sqlite3  # 进行SQLite数据库操作

datalist = []
for page in range(1,5):#这边的参数是自己测试出来的
    # 1.获取html文件
    r = rq.get('https://api.bilibili.com/x/web-interface/popular?ps=50&pn={}'.format(page))
    # 2. 设置对于的编码方式
    r.encoding = r.apparent_encoding#从内容中分析出的响应内容编码
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
        count.append(d['short_link'])        # 链接
        datalist.append(count)

#print(datalist)#输出测试
b=sorted(datalist,key=lambda x:x[3],reverse=True)
#定义函数存储数据到excel文件中
def saveData(datalist,savepath):
    print("save.......")
    book = xlwt.Workbook(encoding="utf-8",style_compression=0) #创建workbook对象
    sheet = book.add_sheet('哔哩哔哩Top200', cell_overwrite_ok=True) #创建工作表
    col = ("标题","类型","up主","播放量","评论","点赞","投币","收藏","分享","链接")
    for i in range(0,10):
        sheet.write(0,i,col[i])  #列名
    for i in range(0,200):
        # print("第%d条" %(i+1))       #输出语句，用来测试
        data = datalist[i]
        for j in range(0,10):
            sheet.write(i+1,j,data[j])  #数据
    book.save(savepath) #保存

savepath = "bilibili.xls"
saveData(b,savepath)


def saveData2DB(datalist,dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    for data in datalist:
        for index in range(len(data)):
            #data[index] = '"' + data[index] + '"'
            data[index] = str(data[index])
            data[index] = '"' + data[index] + '"'

        sql = '''
                insert into bilibili200(
                title,ttype,up,views,reply,dianzan,coin,favorite,share,link)
                values (%s)'''%",".join(data)
        print(",".join(data))
        print(sql)     #输出查询语句，用来测试
        cur.execute(sql)
        conn.commit()
    cur.close
    conn.close()


def init_db(dbpath):
    sql = '''
        create table bilibili200
        (
        id integer  primary  key autoincrement,
        title varchar,
        ttype varchar,
        up varchar,
        views numeric,
        reply numeric,
        dianzan numeric,
        coin numeric,
        favorite numeric,
        share numeric, 
        link text
        )


    '''  #创建数据表
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

dbpath = "bilibili.db"              #当前目录新建数据库，存储进去
saveData2DB(b,dbpath)