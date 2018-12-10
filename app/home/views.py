# coding:utf8
from . import home
from flask import render_template, redirect, url_for


# 登陆、注册
@home.route("/login/")
def login():
    return render_template("home/login.html")


@home.route("/logout/")
def logout():
    return redirect(url_for("home.login"))


@home.route("/register/")
def register():
    return render_template("home/register.html")


# 用户中心 (用户主界面，修改密码，评论记录，登陆日志，收藏)
@home.route("/user/")
def user():
    return render_template("home/user.html")


@home.route("/pwd/")
def pwd():
    return render_template("home/pwd.html")


@home.route("/comments/")
def comments():
    return render_template("home/comments.html")


@home.route("/loginlog/")
def loginlog():
    return render_template("home/loginlog.html")


@home.route("/collections/")
def collections():
    return render_template("home/collections.html")


# 首页
@home.route("/")
def index():
    return render_template("home/index.html")


@home.route("/animation/")
def animation():
    return render_template("home/animation.html")


# 搜索展示
@home.route("/search/")
def search():
    return render_template("home/search.html")


# 电影详情(播放)
@home.route("/play/")
def play():
    return render_template("home/play.html")
