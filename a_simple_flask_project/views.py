# coding:utf8
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8') # python3 默认为 unicode 编码
import os
from flask import Flask, render_template, redirect, flash, session, Response, url_for, request
from forms import LoginForm, RegisterFrom, PublishForm
from models import db, User, Article
from werkzeug.security import generate_password_hash
from datetime import datetime
from functools import wraps
from werkzeug.utils import secure_filename
import uuid

app = Flask(__name__)
app.config["SECRET_KEY"] = "111111"  # A secret key is required to use CSRF.
app.config["UP"] = os.path.join(os.path.dirname(__file__), "static/uploads")


# 登陆装饰器!!
def user_login_req(f):
    @wraps(f)
    def login_req(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)

    return login_req


# 登陆
@app.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        session["user"] = data["name"]
        flash(u"登陆成功！", "ok")
        return redirect("/art/list/1/")
    else:
        pass
    return render_template("login.html", title=u"登陆", form=form)  # 渲染模板


# 注册
@app.route("/register/", methods=["GET", "POST"])
def register():
    form = RegisterFrom()
    if form.validate_on_submit():  # 提交并验证通过
        data = form.data
        # 保存数据
        user = User(
            name=data["name"],
            pwd=generate_password_hash(data["pwd"]),
            addtime=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        db.session.add(user)
        db.session.commit()
        # 定义一个会话闪现
        flash(u"注册成功，请登陆！", "ok")
        return redirect("/login/")
    else:
        flash(u"输入正确信息注册！", "err")
    return render_template("register.html", title=u"注册", form=form)


# 退出 (302跳转到登陆页面)
@app.route("/logout/", methods=["GET"])
@user_login_req
def logout():
    session.pop("user", None)
    return redirect("/login/")


# 修改文件名称
def change_name(name):
    info = os.path.splitext(name)
    # 文件名： 时间格式字符串+唯一字符串+后缀名
    name = datetime.now().strftime("%Y%m%d%H%M%S") + str(uuid.uuid4().hex) + info[-1]
    return name


# 发布文章
@app.route("/art/add/", methods=["GET", "POST"])
@user_login_req
def art_add():
    form = PublishForm()
    if form.validate_on_submit():
        data = form.data
        # 上传LOGO
        file = secure_filename(form.logo.data.filename)
        logo = change_name(file)
        if not os.path.exists(app.config["UP"]):
            os.makedirs(app.config["UP"])
        form.logo.data.save(app.config["UP"] + "/" + logo)
        # 获取用户ID
        user = User.query.filter_by(name=session["user"]).first()
        user_id = user.id
        # 保存数据
        art = Article(
            title=data["title"],
            cate=data["cate"],
            user_id=user_id,
            logo=logo,
            content=data["content"],
            addtime=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        db.session.add(art)
        db.session.commit()
        flash(u"发布文章成功！", "ok")
    else:
        pass
    return render_template("art_add.html", title=u"发布文章", form=form)


# 编辑文章
@app.route("/art/edit/<int:id>/", methods=["GET", "POST"])
@user_login_req
def art_edit(id):
    return render_template("art_edit.html")


# 删除文章
@app.route("/art/del/<int:id>/", methods=["GET"])
@user_login_req
def art_del(id):
    return redirect("/art/list/")


# 文章列表
@app.route("/art/list/<int:page>/", methods=["GET"])
@user_login_req
def art_list(page=None):
    if page is None:
        page = 1
    # 获取当前用户信息
    user = User.query.filter_by(name=session["user"]).first()
    # 数据查询并分页获取
    page_data = Article.query.filter_by(
        user_id=user.id
    ).order_by(
        Article.addtime.desc()
    ).paginate(page=page, per_page=2)
    cate = [(1, u"汽车"), (2, u"旅游"), (3, u"美食"), (4, u"其它")]
    return render_template("art_list.html", title=u"文章列表", page_data=page_data, cate=cate)


# 验证码
@app.route("/code/", methods=["GET"])
def code():
    from code import Code
    c = Code()
    info = c.create_code()
    image = os.path.join(os.path.dirname(__file__), "static/code" + "/" + info["img_name"])
    with open(image, 'rb') as f:
        image = f.read()
    session["code"] = info["code"]
    return Response(image, mimetype="jpeg")


if __name__ == "__main__":
    app.run()
