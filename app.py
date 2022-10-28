#flaskをインポート
# from crypt import methods
from ast import And
from operator import truediv
from ssl import HAS_TLSv1_1
from time import time
from flask import Flask, render_template ,request,redirect,session
import os

import sqlite3,datetime

#これからappという名前でFlaskアプリを作っていく
app = Flask(__name__)

IMG_FOLDER = os.path.join('static', 'IMG')

app.config['UPLOAD_FOLDER'] = IMG_FOLDER


#main.htmlにとぶ
@app.route("/")
def main():
    return render_template("main.html")



#フリーランス追加ページ
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
    seibetu=request.form.get("seibetu")
    Total_time=request.form.get("Total_time")
    sunabaco=request.form.get("sunabaco")
    hitokoto_ten=request.form.get("hitokoto_ten")
    content_ten1=request.form.get("content_ten1")
    content_ten2=request.form.get("content_ten2")
    reward_first=request.form.get("reward_first")
    content_1=request.form.get("content_1")
    content_2=request.form.get("content_2")
    content_3=request.form.get("content_3")
    content_ten3=request.form.get("content_ten3")
    sougyou=request.form.get("sougyou")
    memo_last=request.form.get("memo_last")
    class_00=request.form.get("class_00")

    
    conn=sqlite3.connect("try.db")
    c=conn.cursor()
    c.execute("INSERT INTO users VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);",(display_name,twitter_id,era,place,hitokoto_0,seibetu,Total_time,sunabaco,hitokoto_ten,content_ten1,content_ten2,reward_first,content_1,content_2,content_3,content_ten3,sougyou,memo_last,class_00,))
    conn.commit()
    c.close()
    return redirect("/")



#雇用追加ページ
@app.route("/add_ten",methods =["GET"])
def add_ten_get():
    return render_template("add_ten.html")


# @app.route("/add_ten",methods = ["POST"])
# def add_post():
#     display_name=request.form.get("display_name")
#     twitter_id=request.form.get("twitter_id")
#     era=request.form.get("era")
#     place=request.form.get("place")
#     hitokoto_0=request.form.get("hitokoto_0")
#     seibetu=request.form.get("seibetu")
#     Total_time=request.form.get("Total_time")
#     sunabaco=request.form.get("sunabaco")
#     hitokoto_ten=request.form.get("hitokoto_ten")
#     content_ten1=request.form.get("content_ten1")
#     content_ten2=request.form.get("content_ten2")
#     reward_first=request.form.get("reward_first")
#     content_1=request.form.get("content_1")
#     content_2=request.form.get("content_2")
#     content_3=request.form.get("content_3")
#     content_ten3=request.form.get("content_ten3")
#     sougyou=request.form.get("sougyou")
#     memo_last=request.form.get("memo_last")
#     class_00=request.form.get("class_00")

    
#     conn=sqlite3.connect("try.db")
#     c=conn.cursor()
#     c.execute("INSERT INTO users VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);",(display_name,twitter_id,era,place,hitokoto_0,seibetu,Total_time,sunabaco,hitokoto_ten,content_ten1,content_ten2,reward_first,content_1,content_2,content_3,content_ten3,sougyou,memo_last,class_00,))
#     conn.commit()
#     c.close()
#     return redirect("/")


# #表示機能(amakusa)
# @app.route("/amakusa_list")
# def amakusa_list():
#     #「sqlite3でcolor.dbに接続してね」ということをconnに代入
#     conn = sqlite3.connect("try.db")
#     #「sqlite3で接続したものを操作してね」ということをcに代入
#     c = conn.cursor()
#     #()内のSQL文を実行
#     c.execute("SELECT id,display_name,era,hitokoto_0,seibetu,place FROM users where place = 'AMAKUSA';")
#     #タスクリストを入れる配列を定義
#     task_list = []
#     #繰り返し分
#     for row in c.fetchall():
#         task_list.append({"id":row[0],"display_name":row[1],"era":row[2],"hitokoto_0":row[3],"seibetu":row[4],"place":row[5]})
#     #color.dbとの接続を終了
#     c.close()
#     #データの中身を確認
#     print(task_list)
#     return render_template("amakusa_list.html", task_list = task_list)



#  #taskの作成----------追加したところーーーーーー
#         c.execute("SELECT seibetu,era FROM users WHERE class_00 = '在宅';")
#         seibetu_list = []
#         era_list=[]
#         for row in c.fetchall():
#             seibetu_list.append({"seibetu":row[0]})
#             era_list.append({"era":row[0]})
#             seibetu=seibetu_list
#             if "男性"==seibetu: 
#                 Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'yung_man.png')
#             else:
#                 Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'yung_woman.png')

#表示機能(在宅)
@app.route("/zaitaku_list")
def zaitaku_list():
    #「sqlite3でcolor.dbに接続してね」ということをconnに代入
    conn = sqlite3.connect("try.db")
    #「sqlite3で接続したものを操作してね」ということをcに代入
    c = conn.cursor()
    #()内のSQL文を実行
    #task_listの作成
    c.execute("SELECT id,display_name,era,hitokoto_0,seibetu,place FROM users where class_00 = '在宅';")
    # c.execute("SELECT seibetu,era FROM users WHERE class_00 = '在宅';")
    task_list = []
    seibetu = ""
    era=""
    # era_list=[]
    for row in c.fetchall():
        
        seibetu=row[4]
        era=row[2]
        #taskの作成----------追加したところーーーーーー
        
        # seibetu_list.append({"seibetu":row[0]})
        # era_list.append({"era":row[0]})
        # seibetu=seibetu_list

        if "男性"==seibetu:  
            if "10代〜20代"==era:
                Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'yung_man.png')
            elif "30代〜40代"==era:
                Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'man.png')
            else:
                Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'old_man.png')

        else:
            if "10代〜20代"==era:
                Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'yung_woman.png')
            elif "30代〜40代"==era:
                Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'woman.png')
            else:
                Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'old_woman.png')
            

        task_list.append({"id":row[0],"display_name":row[1],"era":row[2],"hitokoto_0":row[3],"seibetu":row[4],"place":row[5],"Flask_Logo":Flask_Logo})

    #color.dbとの接続を終了
    c.close()
    print("-------------------------------------")
    print(Flask_Logo)
    return render_template("zaitaku_list.html", task_list = task_list)






#表示機能(就職・転職)
@app.route("/ten_list")
def ten_list():
    #「sqlite3でcolor.dbに接続してね」ということをconnに代入
    conn = sqlite3.connect("try.db")
    #「sqlite3で接続したものを操作してね」ということをcに代入
    c = conn.cursor()
    #()内のSQL文を実行
    c.execute("SELECT id,display_name,era,hitokoto_ten,seibetu,place FROM users where class_00 = '就職・転職';")
    #タスクリストを入れる配列を定義
    task_list = []
    seibetu = ""
    era=""
    # era_list=[]
    for row in c.fetchall():
        
        seibetu=row[4]
        era=row[2]
        #taskの作成----------追加したところーーーーーー
        
        # seibetu_list.append({"seibetu":row[0]})
        # era_list.append({"era":row[0]})
        # seibetu=seibetu_list

        if "男性"==seibetu:  
            if "10代〜20代"==era:
                Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'yung_man.png')
            elif "30代〜40代"==era:
                Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'man.png')
            else:
                Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'old_man.png')

        else:
            if "10代〜20代"==era:
                Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'yung_woman.png')
            elif "30代〜40代"==era:
                Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'woman.png')
            else:
                Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'old_woman.png')
            

        task_list.append({"id":row[0],"display_name":row[1],"era":row[2],"hitokoto_ten":row[3],"seibetu":row[4],"place":row[5],"Flask_Logo":Flask_Logo})
    

    c.close()

    return render_template("ten_list.html", task_list = task_list)



# @app.route("/del_check/<int:id>",methods=["POST"])
# def del_check(id):

#     num=(id)
#     print(num)
#     return render_template("del_check.html",num=num)





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
    return redirect("/")


#個人情報表示機能(在宅)
@app.route("/zaitaku_task/<int:id>",methods = ["POST"])
def zaitaku_task(id):
     #「sqlite3でcolor.dbに接続してね」ということをconnに代入
    conn = sqlite3.connect("try.db")
    #「sqlite3で接続したものを操作してね」ということをcに代入
    c = conn.cursor()
    #()内のSQL文を実行
    c.execute("SELECT id,display_name,twitter_id,era,place,hitokoto_0,seibetu,Total_time,sunabaco,reward_first,content_1,content_2,content_3,memo_last FROM users where class_00 = '在宅' AND id =?;",(id,))
    #タスクリストを入れる配列を定義
    zaitaku_task = []
    seibetu=""
    era=""
    #繰り返し分
    for row in c.fetchall():

        seibetu=row[6]
        era=row[3]


        if "男性"==seibetu:  
            if "10代〜20代"==era:
                Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'yung_man.png')
            elif "30代〜40代"==era:
                Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'man.png')
            else:
                Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'old_man.png')

        else:
            if "10代〜20代"==era:
                Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'yung_woman.png')
            elif "30代〜40代"==era:
                Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'woman.png')
            else:
                Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'old_woman.png')

        zaitaku_task.append({"id":row[0],"display_name":row[1],"twitter_id":row[2],"era":row[3],"place":row[4],"hitokoto_0":row[5],"seibetu":row[6],"Total_time":row[7],"sunabaco":row[8],"reward_first":row[9],"content_1":row[10],"content_2":row[11],"content_3":row[12],"memo_last":row[13],"Flask_Logo":Flask_Logo})
    #color.dbとの接続を終了
    c.close()
    #データの中身を確認
    print("-------------------------------------")
    print(Flask_Logo)

    return render_template("zaitaku_task.html", zaitaku_task = zaitaku_task)



#個人情報表示機能(就職・転職)
@app.route("/ten_task/<int:id>",methods = ["POST"])
def ten_task(id):
     #「sqlite3でcolor.dbに接続してね」ということをconnに代入
    conn = sqlite3.connect("try.db")
    #「sqlite3で接続したものを操作してね」ということをcに代入
    c = conn.cursor()
    #()内のSQL文を実行
    c.execute("SELECT id,display_name,twitter_id,era,place,seibetu,sunabaco,hitokoto_ten,content_ten1,content_ten2,content_ten3,memo_last FROM users where class_00 = '就職・転職' AND id = ?;",(id,))
    #タスクリストを入れる配列を定義
    ten_task = []
    seibetu=""
    era=""
    #繰り返し分
    for row in c.fetchall():

        seibetu=row[5]
        era=row[3]


        if "男性"==seibetu:  
            if "10代〜20代"==era:
                Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'yung_man.png')
            elif "30代〜40代"==era:
                Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'man.png')
            else:
                Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'old_man.png')

        else:
            if "10代〜20代"==era:
                Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'yung_woman.png')
            elif "30代〜40代"==era:
                Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'woman.png')
            else:
                Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'old_woman.png')

        ten_task.append({"id":row[0],"display_name":row[1],"twitter_id":row[2],"era":row[3],"place":row[4],"seibetu":row[5],"sunabaco":row[6],"hitokoto_ten":row[7],"content_ten1":row[8],"content_ten2":row[9],"content_ten3":row[10],"memo_last":row[11],"Flask_Logo":Flask_Logo})
    #color.dbとの接続を終了
    c.close()
    #データの中身を確認
    return render_template("ten_task.html", ten_task = ten_task)






















#表示機能(詳細検索)
@app.route("/zaitaku_detail",methods = ["POST"])
def zaitaku_detail():

    place=request.form.get("place")
    # sunabaco=request.form.get("sunabaco")

    #「sqlite3でcolor.dbに接続してね」ということをconnに代入
    conn = sqlite3.connect("try.db")
    #「sqlite3で接続したものを操作してね」ということをcに代入
    c = conn.cursor()
    #()内のSQL文を実行

    if "全部" ==place:
         c.execute("SELECT id,display_name,era,hitokoto_0,seibetu,place FROM users where class_00 = '在宅';")
    
    else:
        c.execute("SELECT id,display_name,era,hitokoto_0,seibetu,place FROM users where class_00 = '在宅' AND place =?;",(place,))


    # c.execute("SELECT seibetu,era FROM users WHERE class_00 = '在宅';")
    task_list = []
    seibetu = ""
    era=""
    # era_list=[]
    for row in c.fetchall():
        
        seibetu=row[4]
        era=row[2]
        #taskの作成----------追加したところーーーーーー
        
        # seibetu_list.append({"seibetu":row[0]})
        # era_list.append({"era":row[0]})
        # seibetu=seibetu_list

        if "男性"==seibetu:  
            if "10代〜20代"==era:
                Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'yung_man.png')
            elif "30代〜40代"==era:
                Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'man.png')
            else:
                Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'old_man.png')

        else:
            if "10代〜20代"==era:
                Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'yung_woman.png')
            elif "30代〜40代"==era:
                Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'woman.png')
            else:
                Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'old_woman.png')
            

        task_list.append({"id":row[0],"display_name":row[1],"era":row[2],"hitokoto_0":row[3],"seibetu":row[4],"place":row[5],"Flask_Logo":Flask_Logo})

    #color.dbとの接続を終了
    c.close()
    # print("-------------------------------------")
    # print(Flask_Logo)
    return render_template("zaitaku_list.html", task_list = task_list)







#表示機能(就職・転職)
@app.route("/ten_detail",methods = ["POST"])
def ten_detail():

    place=request.form.get("place")
    #「sqlite3でcolor.dbに接続してね」ということをconnに代入
    conn = sqlite3.connect("try.db")
    #「sqlite3で接続したものを操作してね」ということをcに代入
    c = conn.cursor()

    
    #()内のSQL文を実行
    c.execute("SELECT id,display_name,era,hitokoto_ten,seibetu,place FROM users where class_00 = '就職・転職' AND place = ?;",(place,))
    #タスクリストを入れる配列を定義
    task_list = []
    seibetu = ""
    era=""
    # era_list=[]
    for row in c.fetchall():
        
        seibetu=row[4]
        era=row[2]
        #taskの作成----------追加したところーーーーーー
        
        # seibetu_list.append({"seibetu":row[0]})
        # era_list.append({"era":row[0]})
        # seibetu=seibetu_list

        if "男性"==seibetu:  
            if "10代〜20代"==era:
                Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'yung_man.png')
            elif "30代〜40代"==era:
                Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'man.png')
            else:
                Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'old_man.png')

        else:
            if "10代〜20代"==era:
                Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'yung_woman.png')
            elif "30代〜40代"==era:
                Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'woman.png')
            else:
                Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'old_woman.png')
            

        task_list.append({"id":row[0],"display_name":row[1],"era":row[2],"hitokoto_ten":row[3],"seibetu":row[4],"place":row[5],"Flask_Logo":Flask_Logo})
    

    c.close()

    return render_template("ten_list.html", task_list = task_list)





#目的ページにとぶ
@app.route("/mokuteki")
def mokuteki():
    return render_template("mokuteki.html")











if __name__ =="__main__":
    #Flaskが持っているアプリを実行する
    app.run(debug=True)

# app.run(port=8888)