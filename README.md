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

前台布局的搭建<br>

    1 静态文件的引入:{{ url_for('static',filename='文件路径') }}
    2 定义路由:{{ url_for('模块名.视图名',变量=参数) }}
    3 定义数据块: {% block 数剧块名称 %} ... {% endblock %}

会员登录页面的搭建<br>

    # 登录
    @home.route("/login/")
    def login():
        return render_template("home/login.html")
    # 退出登录
    @home.route("/logout/")
    def logout():
        return redirect(url_for('home.login'))  # 此处要导入redirect和url_for模块：redirect方法可以重定向，url_for是路由生成器

会员注册页面搭建<br>

    # 注册
    @home.route("/register/")
    def register():
        return render_template("home/register.html")

会员中心页面的搭建<br>


    # 会员中心
    @home.route('/user/')
    # 修改密码
    @home.route('/pwd/')
    # 评论记录
    @home.route('/comments/')
    # 登录日志
    @home.route('/loginlog/')
    # 收藏日志
    @home.route('/moviecol/')

电影列表页面的搭建<br>


    # 列表
    @home.route("/")
    def index():
        return render_template("home/index.html")
    # 动画
    @home.route("/animation/")
    def animation():
        return render_template("home/animation.html")


电影搜索页面的搭建<br>

    #搜索
    @home.route("/search/")
    def search():
        return render_template('home/search.html')


电影详情页面的搭建

    # 详情
    @home.route("/play/")
    def play():
        return render_template('home/play.html')


404页面的搭建

    # 404
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("common/404.html",404)
    # 404页面是要放置在初始化文件中的

搭建后台页面

    管理员登录页面的搭建
    # 登录
    @admin.route('/login/')
    def login():
        return render_template("admin/login.html")
    # 退出
    @admin.route('/logout/')
    def logout():
        return redirect(url_for("admin.login"))


    # 后台布局搭建
    # admin.html
    {% block css %}...{% endblock %}
    {% include "grid.html" %}
    {% block content %}...{% endblock %}
    {% block js %}...{% endblock %}

    # 其他页面继承父模板
    {% extends "admin/admin.html" %}
    {% block css %}...{% endblock %}
    {% include "grid.html" %}
    {% block content %}...{% endblock %}
    {% block js %}...{% endblock %}

    # 修改密码
    @admin.route('/pwd/')
    def pwd():
        return render_template("admin/pwd.html")

    # 控制面板 系统管理
    @admin.route('/index/')
    def index():
        return render_template('admin/index.html')

    # 标签管理页面的搭建
    # 编辑标签
    @admin.route("/tag/add/")
    def tag_add():
        return render_template('admin/tag_add.html')
    # 标签列表
    @admin.route('/tag/list/')
    def tag_list():
        return render_template('admin/tag_list.html')

    # 电影管理页面的搭建
    # 编辑电影
    @admin.route('/movie/add/')
    def movie_add():
        return render_template('admin/movie_add.html')
    # 电影列表
    @admin.route('/movie/list')
    def movie_list():
        return render_template('admin/movie_list.html')

    # 上映预告管理页面的搭建
    # 编辑上映预告
    @admin.route('/preview/add/')
    def preview_add():
        return render_template('admin/preview_add.html')
    # 上映预告列表
    @admin.route('/preview/list/')
    def preview_list():
        return render_template('admin/preview_list.html')

    # 会员管理页面的搭建
    # 会员列表
    @admin.route('/user/list/')
    def user_list():
        return render_template('admin/user_list.html')
    # 查看会员
    @admin.route('/user/view/')
    def user_view():
        return render_template('admin/user_view.html')

    # 评论管理页面的搭建
    # 评论列表
    @admin.route('/comment/list')
    def comment_list():
        return render_template("admin/comment_list.html")

    # 收藏管理页面的搭建
    # 收藏列表
    @admin.route('/moviecol/list')
    def moviecol_list():
        return render_template('admin/moviecol_list.html')

    # 操作日志管理页面的搭建
    # 操作日志列表
    @admin.route('/oplog/list/')
    def oplog_list():
        return render_template('admin/oplog_list.html')
    # 管理员日志列表
    @admin.route('/adminloginlog/list/')
    def adminloginlog_list():
        return render_template('admin/adminloginlog_list.html')
    # 会员日志列表
    @admin.route('/userloginlog/list/')
    def userloginlog_list():
        return render_template('admin/userloginlog_list.html')

    # 角色管理页面的搭建
    # 添加角色
    @admin.route('/role/add')
    def role_add():
        return render_template('admin/role_add.html')
    # 角色列表
    @admin.route('/role/list/')
    def role_list():
        return render_template('admin/role_list.html')
    # 权限管理页面的搭建
    @admin.route('/auth/add/')
    def auth_add():
        return render_template('admin/auth_add.html')
    @admin.route('/auth/list/')
    def auth_list():
        return render_template('admin/auth_list.html')

    # 管理员管理页面搭建
    # 添加管理员
    @admin.route('/admin/add/')
    def admin_add():
        return render_template('admin/admin_add.html')
    # 管理员列表
    @admin.route('/admin/list/')
    def admin_list():
        return render_template('admin/admin_list.html')



# 后台管理模块

    # 管理员登录
    1 app/__init__.py 中创建db对象
    2 app/models.py 中导入db对象
    3 app/admin/forms.py 中定义表单验证
    4 app/templates/admin/login.html 中使用表单字段，信息验证，消息闪现
    5 app/admin/views.py 中处理登录请求，保存会话
    6 app/admin/views.py 定义登录装饰器，访问控制
    # 管理员登录
    1 模型：Admin
    2 表单：LoginForm
    3 请求方法：GET,POST
    4 访问控制：无

# 标签管理
1 模型：Tag
2 表单：TagForm
3 请求方法：GET,POST
4 访问控制：@admin_login_req
