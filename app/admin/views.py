# coding：utf8
from . import admin
from flask import render_template, redirect, url_for


# 主页-控制面板
@admin.route("/")
def index():
    return render_template("admin/index.html")


# 登陆、退出
@admin.route("/login/")
def login():
    return render_template("admin/login.html")


@admin.route("/logout/")
def logout():
    return redirect(url_for("admin.login"))


# 密码管理
@admin.route("/pwd/")
def pwd():
    return render_template("admin/pwd.html")


# 标签管理
@admin.route("/tag/add/")
def tag_add():
    return render_template("admin/tag_add.html")


@admin.route("/tag/list/")
def tag_list():
    return render_template("admin/tag_list.html")


# 电影管理
@admin.route("/movie/add/")
def movie_add():
    return render_template("admin/movie_add.html")


@admin.route("/movie/list/")
def movie_list():
    return render_template("admin/movie_list.html")


# 预告管理
@admin.route("/preview/add/")
def preview_add():
    return render_template("admin/preview_add.html")


@admin.route("/preview/list/")
def preview_list():
    return render_template("admin/preview_list.html")


# 会员列表
@admin.route("/user/list/")
def user_list():
    return render_template("admin/user_list.html")


# 查看会员
@admin.route("/user/view/")
def user_view():
    return render_template("admin/user_view.html")


# 评论列表
@admin.route("/comment/list/")
def comment_list():
    return render_template("admin/comment_list.html")


# 电影收藏列表
@admin.route("/moviecol/list/")
def moviecol_list():
    return render_template("admin/moviecol_list.html")


# 日志（操作、管理员登陆、会员登陆）
@admin.route("/oplog/list/")
def oplog_list():
    return render_template("admin/oplog_list.html")


@admin.route("/adminloginlog/list/")
def adminloginlog_list():
    return render_template("admin/adminloginlog_list.html")


@admin.route("/userloginlog/list/")
def userloginlog_list():
    return render_template("admin/userloginlog_list.html")


# 角色（添加、列表）
@admin.route("/role/add/")
def role_add():
    return render_template("admin/role_add.html")


@admin.route("/role/list/")
def role_list():
    return render_template("admin/role_list.html")


# 权限 （添加、列表）
@admin.route("/auth/add/")
def auth_add():
    return render_template("admin/auth_add.html")


@admin.route("/auth/list/")
def auth_list():
    return render_template("admin/auth_list.html")


# 管理员（添加、列表）
@admin.route("/admin/add/")
def admin_add():
    return render_template("admin/admin_add.html")

@admin.route("/admin/list/")
def admin_list():
    return render_template("admin/admin_list.html")