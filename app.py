#flaskをインポート
from operator import truediv
from time import time
from flask import Flask, render_template ,request,redirect,session

import sqlite3,datetime

#これからappという名前でFlaskアプリを作っていく
app = Flask(__name__)

#main.htmlにとぶ
@app.route("/")
def main():
    return render_template("main.html")

@app.route("/amakusa_list")
def list1():
    return render_template("amakusa_list.html")
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



if __name__ =="__main__":
    #Flaskが持っているアプリを実行する
    app.run(debug=True)
# app.run(port=8888)