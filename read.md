# 电影网站开发
### 前后台项目目录分析

微电影网站：<br>

    1 前台模块（home）
        数据模型:models.py
        表单处理:home/forms.py
        模板目录:templates/home
        静态目录:static
        
    2 后台模块（admin）
        数据模型:models.py
        表单处理:admin/forms.py
        模板目录:templates/admin
        静态目录:static
        
    manage.py           入口启动脚本
    app                 项目APP   
        __init__.py     初始化文件
        models.py       数据模型文件
        static          静态目录
        home/admin      前后台模块
            __init__.py 初始化脚本
            views.py    视图处理文件
            forms.py    表单处理文件
        templates       模板目录
            home/admin  前台/后台模板
    

蓝图构建项目目录:<br>

    1 什么是蓝图?
        一个应用中或跨应用制作应用组件和支持通用的模式
    
    2 蓝图的作用？
        - 将不同的功能模块化
        - 构建大型应用
        - 优化项目结构
        - 增强可读性，易于维护
    
    3 定义蓝图（app/admin/__init__.py）
        from flask import Blueprint
        admin = Blueprint("admin",__name__)
        import views
    4 注册蓝图（app/__init__.py）
        from admin import admin as admin_blueprint
        app.register_blueprint(admin_blueprint,url_prefix="/admin")
    5 调用蓝图（app/admin/views.py）
        from . import admin
        @admin.route("/")
        
        
会员及会员登录日志数据模型设计:<br>

    1 安装数据库链接依赖包
        pip install flask-sqlalchemy
        
    2 定义mysql数据库连接
        from flask_sqlalchemy import SQLAlchemy
        from flask import Flask
        
        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:root@localhost/movie"
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
        db = SQLAlchemy(app)
        
    3 定义会员数据模型
        class User(db.Model):
            __tablename__="user"
            id = db.Column(db.Integer,primary_key=True)
            name = db.Column(db.String)
            pwd = db.Column(db.String)
            email = db.Column(db.String)
            phone = db.Column(db.String)
            info = db.Column(db.Text)
            face = db.Column(db.String)
            addtime = db.Column(db.DateTime,index=True,default=datetime.utcnow)
            uuid = db.Column(db.String)
        
        id:编号、name:账号、pwd:密码、email:邮箱、phone:手机号、info:简介、
        face:头像、addtime:注册时间、uuid:唯一标识符
        comments:评论外键关联、userlogs:会员登录日志外键关联、moviecols:电影收藏外键关联
        
    4 定义会员登录日志数据模型
        id:编号
        user_id:所属会员编号
        ip:最近登录IP地址
        addtime:最近登录时间
        