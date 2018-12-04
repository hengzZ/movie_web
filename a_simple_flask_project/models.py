# coding:utf8
import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost/flask_study"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

"""
用户表
1.编号
2.账号
3.密码
4.注册时间
"""


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(20), nullable=False)  # 账号
    pwd = db.Column(db.String(100), nullable=False)  # 密码
    addtime = db.Column(db.DateTime, nullable=False, index=True, default=datetime.now)  # 注册时间
    articles = db.relationship('Article', backref='user')  # 文章外键关系关联

    # email = db.Column(db.String(100), unique=True)  # 邮箱
    # phone = db.Column(db.String(11), unique=True)  # 手机号码
    # info = db.Column(db.Text)  # 个性简介
    # face = db.Column(db.String(255), unique=True)  # 头像
    # uuid = db.Column(db.String(255), unique=True)  # 唯一标志符

    def __repr__(self):
        return "<User %r>" % self.name

    def check_pwd(self, pwd):
        return check_password_hash(self.pwd, pwd)


"""
文章表
1.编号
2.标题
3.分类
4.作者
5.封面
6.内容
7.发布时间
"""


class Article(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    title = db.Column(db.String(255), nullable=False, unique=True)  # 标题
    cate = db.Column(db.Integer, nullable=False)  # 分类
    logo = db.Column(db.String(255), nullable=False)  # 封面
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 作者
    content = db.Column(db.Text, nullable=False)  # 内容
    addtime = db.Column(db.DateTime, nullable=False, index=True, default=datetime.now)  # 添加时间

    def __repr__(self):
        return "<Article %r>" % self.title


if __name__ == "__main__":
    db.create_all()  # create tables
    # user = User(  # create a record to test saving
    #     name="root",
    #     pwd=generate_password_hash("root"),
    #     addtime=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # )
    # db.session.add(user)
    # db.session.commit()
