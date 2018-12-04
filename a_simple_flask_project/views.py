# coding:utf8
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8') # python3 默认为 unicode 编码
import os
from flask import Flask, render_template, redirect, flash, session, Response, url_for, request
from forms import LoginForm, RegisterFrom, PublishForm
from models import db, User
from werkzeug.security import generate_password_hash
from datetime import datetime
from functools import wraps

app = Flask(__name__)
app.config["SECRET_KEY"] = "111111"  # A secret key is required to use CSRF.


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
        return redirect("/art/list/")
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


# 发布文章
@app.route("/art/add/", methods=["GET", "POST"])
@user_login_req
def art_add():
    form = PublishForm()
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
@app.route("/art/list/", methods=["GET"])
@user_login_req
def art_list():
    return render_template("art_list.html", title=u"文章列表")


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
