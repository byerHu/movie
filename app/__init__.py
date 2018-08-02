# coding:utf8
from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

from app.home import home as home_blueprint  # 导入home蓝图对象
from app.admin import admin as admin_blueprint  # 导入admin蓝图对象

app.register_blueprint(home_blueprint)  # 注册home蓝图
app.register_blueprint(admin_blueprint, url_prefix="/admin")  # 注册admin蓝图，第二个参数是url前缀


# 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"), 404
