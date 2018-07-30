# coding:urf8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:123456@localhost:3306/movie"  # 连接movie数据库
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)  # 实例化数据库对象


# 会员数据模型
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 昵称
    pwd = db.Column(db.String(100))  # 密码
    email = db.Column(db.String(100), unique=True)  # 邮箱
    phone = db.Column(db.String(11), unique=True)  # 手机号
    info = db.Column(db.Text)  # 个性简介
    face = db.Column(db.String(255), unique=True)  # 头像
    addtime = db.Column(db.DateTime, index=True, default=datetime.uctnow)  # 注册时间
    uuid = db.Column(db.String(255), unique=True)  # 唯一标识符
    userlogs = db.relationship('userlog',backref='user') # 会员日志外键关系关联
    def __repr__(self):
        return "<User %r>" % self.name

# 会员登录日志数据模型
class Userlog(db.Model):
    __tablename__ = "userlog"
    id = db.Column(db.Integer, primary_key=True) # 编号
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # 所属会员
    ip = db.Column(db.String(100)) # 登录ip
    addtime = db.Column(db.DateTime,index=True,default=datetime.utcnow) # 登录时间

    def __repr__(self):
        return "<Userlog %r>" % self.id