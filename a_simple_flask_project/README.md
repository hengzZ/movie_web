# A simple project for flask learning
以项目实战的形式学习flask

## 1. 项目介绍（任务需求）
* 实现用户注册、用户登陆、退出登陆
* 添加文章、文章分页列表、修改文章、删除文章等功能。

## 2. 项目演示
* 登陆页面
* 注册页面
* 文章列表页面
* 添加文章页面

## 3. 开发思路
* 搭建开发环境
* 构建项目目录
* 开发前端模板
* 设计数据模型
* 编写后端逻辑
* 测试部署上线


-------------------------------------------------------------
## 前端设计思路
###### 1. 路由 (routes):
@app.route("/login/", methods=["GET","POST"])  # 用户登陆 <br>
@app.route("/logout/", methods=["GET"])  # 用户退出 <br>
@app.route("/register/", methods=["GET","POST"])  # 用户注册 <br>
@app.route("/art/add/", methods=["GET","POST"])  # 发布文章 <br>
@app.route("/art/edit/\<int:id>/", methods=["GET","POST"])  # 编辑文章 <br>
@app.route("/art/list/", methods=["GET"])  # 文章列表 <br>
@app.route("/art/del/\<int:id>/", methods=["GET"])  # 删除文章 <br>

###### 2. 视图 (views):
login  # 用户登陆 <br>
logout  # 用户退出 <br>
register  # 用户注册 <br>
art_add  # 发布文章 <br>
art_edit  # 编辑文章 <br>
art_list  # 文章列表 <br>
art_del  # 删除文章 <br>

###### 3. 模板 (templates):
login.html  # 用户登陆 <br>
register.html  # 用户注册 <br>
art_add.html  # 发布文章 <br>
art_edit.html  # 编辑文章 <br>
art_list.html  # 文章列表 <br>

###### 4. 静态文件 (static):
css  # 层叠式样表 <br>
js  # javascript脚本 <br>
ue  # 百度 ueditor 富文本编辑器


## Jinja2 语法
1.继承
```html
{% extends "父模板路径" %}
```
2.数据块
```html
{% block 块名 %} ... {% endblock %}
```
3.路由生成
```html
{{ url_for("模块名.视图名") }}
```
4.静态文件加载
```html
{{ url_for('static',filename='静态文件路径') }}
```
5.循环语句
```html
{% for 条件 %} ... {% endfor %}
```
6.条件语句
```html
{% if 条件 %} ... {% endif %}
```

7.注释
```html
{# 注释 #}
```

8.函数
```html
{% macro page(data,url) %}  # 定义
{% endmacro %}
```
```html
{% import "page.html" as pg %}  # 导入
{{ pg.page(page_data,'art_list') }}  # 使用
```


## 前端页面开发
step 1. 前端框架选择 <br>
**Bootstrap**: <http://getbootstrap.com/> <br>
step 2. jQuery 插件库 <br>
**jQuery**: <https://code.jquery.com/jquery-3.3.1.min.js> <br>
step 3: UEditor (HTML 文本编辑器) <br>
**UEditor**: <http://fex.baidu.com/ueditor/> <br>

### UI三要素
1. **html template** (html structure without FORM)
2. **form** (for interaction)
3. **view** (for Rendering, Get or Post)

### 后端二要素
1. **model** (for Table structure and DB Accessor )
2. **form** (perform Data Validation)


# 所用内容
* bootstrap CSS 式样表使用 + jQuery 动态页面功能插件
* flask 模板(html + jinja2)、视图（render_template）+ 路由（app.route,redirect,url_for,登陆装饰器）
* wtforms 定义表单
* 通过 sqlalchemy 访问 MySQL
* 静态文件创建