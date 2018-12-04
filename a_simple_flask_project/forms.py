# coding:utf8
from flask import session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, FileField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from models import User

"""
登陆表单
1.账号
2.密码
3.登陆按钮
"""


class LoginForm(FlaskForm):
    name = StringField(
        label=u"账号",
        validators=[
            DataRequired(u"账号不能为空！")
        ],
        description=u"账号",
        render_kw={
            "class": "form-control",
            "placeholder": u"请输入账号！"
        }
    )
    pwd = PasswordField(
        label=u"密码",
        validators=[
            DataRequired(u"密码不能为空！")
        ],
        description=u"密码",
        render_kw={
            "class": "form-control",
            "placeholder": u"请输入密码！"
        }
    )

    submit = SubmitField(
        u"登陆",
        render_kw={
            "class": "btn btn-primary"
        }
    )

    # 自定义字段验证规则： validate_字段名
    def validate_pwd(self, field):
        pwd = field.data
        user = User.query.filter_by(name=self.name.data).first()
        if not user or not user.check_pwd(pwd):
            raise ValidationError(u"账号或密码错误！")


"""
注册表单
1.账号
2.密码
3.确认密码
4.验证码
5.注册按钮
"""


class RegisterFrom(FlaskForm):
    name = StringField(
        label=u"账号",
        validators=[
            DataRequired(u"账号不能为空！")
        ],
        description=u"账号",
        render_kw={
            "class": "form-control",
            "placeholder": u"请输入账号！"
        }
    )
    pwd = PasswordField(
        label=u"密码",
        validators=[
            DataRequired(u"密码不能为空！")
        ],
        description=u"密码",
        render_kw={
            "class": "form-control",
            "placeholder": u"请输入密码！"
        }
    )
    repwd = PasswordField(
        label=u"确认密码",
        validators=[
            DataRequired(u"确认密码不能为空！"),
            EqualTo('pwd', message=u"两次输入密码不一致！")
        ],
        description=u"确认密码",
        render_kw={
            "class": "form-control",
            "placeholder": u"请输入确认密码！"
        }
    )
    code = StringField(
        label=u"验证码",
        validators=[
            DataRequired(u"验证码不能为空！")
        ],
        description=u"验证码",
        render_kw={
            "class": "form-control",
            "placeholder": u"请输入验证码！"
        }
    )
    submit = SubmitField(
        u"注册",
        render_kw={
            "class": "btn btn-success"
        }
    )

    # 自定义字段验证规则： validate_字段名
    def validate_name(self, field):
        name = field.data
        user = User.query.filter_by(name=name).count()
        if user > 0:
            raise ValidationError(u"账号已存在，不能重复注册！")

    # 自定义验证码验证功能
    def validate_code(self, field):
        code = field.data
        # if not session.has_key("code"):
        #     raise ValidationError(u"请输入验证码！")
        # if session.has_key("code") and session["code"].lower() != code.lower():
        #     raise ValidationError(u"验证码不正确！")
        if session["code"].lower() != code.lower():
            raise ValidationError(u"验证码不正确！")


"""
发布文章表单
1.标题
2.分类
3.封面
4.内容
5.发布文章按钮
"""


class PublishForm(FlaskForm):
    title = StringField(
        label=u"标题",
        validators=[],
        description=u"标题",
        render_kw={
            "class": "form-control",
            "placeholder": u"请输入标题！"
        }
    )
    cate = SelectField(
        label=u"分类",
        validators=[],
        description=u"分类",
        choices=[(1, u"汽车"), (2, u"旅游"), (3, u"美食")],
        default=1,
        coerce=int,
        render_kw={
            "class": "form-control"
        }
    )
    logo = FileField(
        label=u"封面",
        validators=[],
        description=u"封面",
        render_kw={
            "class": "form-control-file"
        }
    )
    content = TextAreaField(
        label=u"内容",
        validators=[],
        description=u"内容",
        render_kw={
            "style": "height: 11em;",
            "id": "content"
        }
    )
    submit = SubmitField(
        u"发布",
        render_kw={
            "class": "btn btn-primary"
        }
    )
