# coding:utf8
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost:3306/movie"  # 连接movie数据库
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'b26273f62a0d44568360ee8570221c24'  # 随机生成一个随机字符串 uuid.uuid4().hex

# 定义文件上传的保存路径
app.config['UP_DIR'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/uploads/')
app.debug = True
db = SQLAlchemy(app)  # 实例化数据库对象

from app.home import home as home_blueprint  # 导入home蓝图对象
from app.admin import admin as admin_blueprint  # 导入admin蓝图对象

app.register_blueprint(home_blueprint)  # 注册home蓝图
app.register_blueprint(admin_blueprint, url_prefix="/admin")  # 注册admin蓝图，第二个参数是url前缀


# 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"), 404
