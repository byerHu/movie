# 微电影网站的搭建
### 前后台项目目录分析

微电影网站：<br>

环境搭建<br>

    1 virtualenv的使用
        （1）创建虚拟环境:virtualenv venv
        （2）激活虚拟环境:source venv/bin/activate   windows下:Script/activate
        （3）退出虚拟环境:deactivate
    2 flask的安装
        （1）安装前检测:pip freeze
        （2）安装flask:pip install flask
        （3）安装后检测:pip freeze

项目模块<br>



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

    5 定义标签数据模型
        id:编号
        name:标题
        movies:电影外键关联
        addtime:创建时间

    6 定义电影数据模型
        id:编号，title:电影标题，url:电影地址
        info:电影简介,logo:电影封面，star:星级
        playnum:电影播放量，commentnum:电影评论量，tag_id:所属标签
        area:地区，release_time:发布时间，length:电影长度
        addtime:添加时间，comments:电影评论外键关联
        moviecols:电影收藏外键关联

    7 定义上映预告数据模型
        id:编号
        title:上映预告标题
        logo:上映预告封面
        addtime:创建时间

    8 定义评论数据模型
        id:编号
        content:评论内容
        movie_id:所属电影
        user_id:所属用户
        addtime:评论时间

    9 定义收藏电影数据模型
        id:编号
        movie_id:所属电影
        user_id:所属用户
        addtime:收藏时间

    10 定义权限数据模型
        id:编号
        name:名称
        url:地址
        addtime:添加时间

    11 定义角色数据模型
        id:编号
        name:名称
        auths:权限列表
        addtime:创建时间
        admins:管理员外键

    12 定义管理员数据模型
        id:编号
        name:管理员名称
        pwd:管理员密码
        is_super:是否超级管理员
        role_id:角色编号
        addtime:创建时间
        adminlogs:管理员登录日志外键关联
        oplogs:操作日志外键关联

    13 定义管理员登录日志数据模型
        id:编号
        admin_id:所属管理员编号
        ip:最近登录IP地址
        addtime:最近登录时间

    14 定义操作日志数据模型
        id:编号
        admin_id:所属管理员编号
        ip:操作IP地址
        reason:操作原因
        addtime:创建时间

