# INTRODUCTION #

## 环境 ##
* Linux
* python3
* mysql
* html5
* flask
* nginx
* PyCharm Editor

## python web 框架 ##
* flask - 轻量级
* django - 全栈型
* tornado - 高效并发

## Flask 介绍 ##
* WSGI (web server gateway interface) - werkzeug
* 模板引擎 - Jinja2
* 表单功能 - WTForms
* 数据库交互 - SQLAlchemy + PyMySQL

## skills ##
* 使用整型、浮点型、路径型、字符串型、正则表达式路由转换器
* 使用post与get请求、上传文件、cookie获取与响应、session、404处理
* 使用模板自动转义、定义过滤器、定义全局上下文处理器、Jinja2语法、包含、继承、定义宏
* 使用flask-wtf定义表单模型、字段类型、字段验证、视图处理表单、模板使用表单
* 使用flask-sqlachemy定义数据库模型、添加数据、修改数据、查询数据、删除数据、数据库事件、数据迁移
* 使用蓝图优化项目结构，实现微电影网站前台与后台业务逻辑
* centos+python+nginx+mysql的部署以及视频流媒体的配置

## 模块结构 ##
### 前台
* 会员登陆及注册
* 会员中心
* 电影播放
* 电影评论
* 收藏电影
### 后台
* 管理员登陆
* 修改密码
* 标签管理
* 电影管理
* 上映预告管理
* 会员管理
* 评论管理
* 收藏管理
* 角色管理
* 权限管理
* 管理员管理
* 日志管理

## 前后台项目目录分析 ##
* manage.py (入口启动脚本)
* app (项目APP)
    * __init__.py
    * models.py (数据模型文件)
    * static (静态目录)
    * home/admin (前台/后台模块)
        * __init__.py
        * views.py (视图处理文件)
        * forms.py (表单处理文件)
    * templates (模板目录)
        * home/admin (前台/后台模板)

## 蓝图 ##
* 什么是蓝图：
    * 一个应用中或跨应用制作应用组件和支持通用的模式
* 蓝图的作用：
    * -将不同的功能模块化
    * -构建大型应用
    * -优化项目结构
    * -增强可读性，易于维护

## 数据模型关系分析 ##
### 前台模型
* 会员表(user)
* 会员登录日志表(userlog)
* 标签表(tag)
* 电影表(movie)
* 上映预告(preview)
* 评论(comment)
* 电影收藏(moviecol)
### 后台模型
* 权限表(auth)
* 角色表(role)
* 管理员表(admin)
* 管理员登录日志(adminlog)
* 操作日志(oplog)

## 界面
#### 组成
* **导航栏** - nav (navigation)
* **底部** - bottom
* 内容- content
    * **菜单** - menu
    * 对应内容
#### 布局
---------------------------------- <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(横向导航栏) <br>
---------------------------------- <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(内容) <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;菜单 | 对应内容 <br>
---------------------------------- <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(底部导航栏及信息) <br>
---------------------------------- <br>

## 