# coding:utf8
from . import home  # 从当前目录导入home蓝图对象


@home.route("/")
def index():
    return "<h1 style='color:green'>this is home</h1>"
