# 个人博客

## 部署准备：
系统使用django开发，环境依赖在 requirements.txt 中列出；

方便部署环境隔离，需要先安装 virtualenv >>  pip install virtualenv

创建python环境 >> virtualenv blogEnv

进入目录 >> cd blogEnv

拉取线上代码 >> git clone https://github.com/chnpmy/blog_django.git

启动virtualenv进入python虚拟环境，在不同系统下的不同启动方式
- linux/mac启动方式：blogEnv >> source bin/activate
- windows启动方式：blogEnv\Scripts\activate.bat

在python虚拟环境中安装依赖模块，执行 >> pip install -r blog_django/requirements.txt

## 部署文件：

Nginx + Supervisor + gunicorn部署

在目录 /etc 中有两个文件：

> supervisord.conf 是项目的supervisor 启动配置；
>
> gunicorn.py 是多线程并发配置，最大并发10000