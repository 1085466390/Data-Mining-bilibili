from flask import Flask,render_template
import sqlite3

app = Flask(__name__)


@app.route('/')#路由解析

def index():
    return render_template("index.html")

@app.route('/index')
def home():
    return render_template("index.html")

@app.route('/movie')#路由解析
def movie():
    datalist = []
    con = sqlite3.connect("bilibili.db")
    cur = con.cursor()
    sql = "select * from bilibili200"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    return render_template("movie.html",movies = datalist)

@app.route('/score')#路由解析
def score():
    score = []#评分
    number = []#每个评分统计出的电影数量
    con = sqlite3.connect("bilibili.db")
    cur = con.cursor()
    sql = "select views,coin from bilibili200 group by coin, views"
    data = cur.execute(sql)
    for item in data:
        score.append(item[0])
        number.append(item[1])

    cur.close()
    con.close()
    return render_template("score.html",score=score,num=number )

@app.route('/team')#路由解析
def team():
    return render_template("team.html")

@app.route('/word')#路由解析
def word():
    return render_template("word.html")

@app.route('/test')#路由解析
def test():
    return render_template("test.html")



if __name__ == '__main__':
    app.run()
