#flaskをインポート
from crypt import methods
from operator import truediv
from ssl import HAS_TLSv1_1
from time import time
from flask import Flask, render_template ,request,redirect,session

import sqlite3,datetime

#これからappという名前でFlaskアプリを作っていく
app = Flask(__name__)

#main.htmlにとぶ
@app.route("/")
def main():
    return render_template("main.html")

# @app.route("/amakusa_list")
# def list1():
#     return render_template("amakusa_list.html")
@app.route("/yatushiro_list")
def list2():
    return render_template("yatushiro_list.html")
@app.route("/fukuoka_list")
def list3():
    return render_template("fukuoka_list.html")
@app.route("/takamatsu_list")
def list4():
    return render_template("takamatsu_list.html")
@app.route("/idoba_list")
def list5():
    return render_template("idaba_list.html")
@app.route("/ebetsu_list")
def list6():
    return render_template("ebetsu_list.html")
@app.route("/koza_list")
def list7():
    return render_template("koza_list.html")




@app.route("/add",methods =["GET"])
def add_get():
    return render_template("add.html")


@app.route("/add",methods = ["POST"])
def add_post():
    display_name=request.form.get("display_name")
    twitter_id=request.form.get("twitter_id")
    era=request.form.get("era")
    place=request.form.get("place")
    hitokoto_0=request.form.get("hitokoto_0")
    users_type=request.form.get("users_type")
    Total_time=request.form.get("Total_time")
    effort_time=request.form.get("effort_time")
    important_lang=request.form.get("important_lang")
    originally_level=request.form.get("originally_level")
    cost_first=request.form.get("cost_first")
    reward_first=request.form.get("reward_first")
    content_1=request.form.get("content_1")
    content_2=request.form.get("content_2")
    content_3=request.form.get("content_3")
    content_4=request.form.get("content_4")
    kansou=request.form.get("kansou")
    memo_last=request.form.get("memo_last")
    
    conn=sqlite3.connect("try.db")
    c=conn.cursor()
    c.execute("INSERT INTO users VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);",(display_name,twitter_id,era,place,hitokoto_0,users_type,Total_time,effort_time,important_lang,originally_level,cost_first,reward_first,content_1,content_2,content_3,content_4,kansou,memo_last,))
    conn.commit()
    c.close()
    return redirect("/amakusa_list")


#表示機能
@app.route("/amakusa_list")
def amakusa_list():
    #「sqlite3でcolor.dbに接続してね」ということをconnに代入
    conn = sqlite3.connect("try.db")
    #「sqlite3で接続したものを操作してね」ということをcに代入
    c = conn.cursor()
    #()内のSQL文を実行
    c.execute("SELECT id,display_name,era,hitokoto_0,users_type FROM users where place = 'AMAKUSA';")
    #タスクリストを入れる配列を定義
    task_list = []
    #繰り返し分
    for row in c.fetchall():
        task_list.append({"id":row[0],"display_name":row[1],"era":row[2],"hitokoto_0":row[3],"users_type":row[4]})
    #color.dbとの接続を終了
    c.close()
    #データの中身を確認
    print(task_list)
    return render_template("amakusa_list.html", task_list = task_list)


#削除機能
@app.route("/del/<int:id>",methods = ["POST"])
def del_task(id):
    #「sqlite3でtry.dbに接続してね」ということをconnに代入
    conn = sqlite3.connect("try.db")
    #「sqlite3で接続したものを操作してね」ということをcに代入
    c = conn.cursor()
    #()内のSQL文を実行
    c.execute("delete from users where id = ?;",(id,))
    #DBに追加するので、変更を保存する
    conn.commit()
    #color.dbとの接続を終了
    c.close()
    return redirect("/amakusa_list")


#個人情報表示機能
@app.route("/task/<int:id>",methods = ["POST"])
def amakusa_task(id):
     #「sqlite3でcolor.dbに接続してね」ということをconnに代入
    conn = sqlite3.connect("try.db")
    #「sqlite3で接続したものを操作してね」ということをcに代入
    c = conn.cursor()
    #()内のSQL文を実行
    c.execute("SELECT * FROM users where place = 'AMAKUSA' AND id = ?;",(id,))
    #タスクリストを入れる配列を定義
    amakusa_list = []
    #繰り返し分
    for row in c.fetchall():
        amakusa_list.append({"id":row[0],"display_name":row[1],"twitter_id":row[2],"era":row[3],"place":row[4],"hitokoto_0":row[5],"users_type":row[6],"Total_time":row[7],"effort_time":row[8],"important_lang":row[9],"originally_level":row[10],"cost_first":row[11],"reward_first":row[12],"content_1":row[13],"content_2":row[14],"content_3":row[15],"content_4":row[16],"kansou":row[17],"memo_last":row[18]})
    #color.dbとの接続を終了
    c.close()
    #データの中身を確認
    print(amakusa_list)
    return render_template("task.html", amakusa_list = amakusa_list)


if __name__ =="__main__":
    #Flaskが持っているアプリを実行する
    app.run(debug=True)
# app.run(port=8888)