# Flask Web 开发实战笔记
## 1. 基础篇
1. 开发环境：`Ubuntu+python3.6+pipenv+MS code`

2. 安装`pipenv`:
   1. `pip3 install pipenv`
   2. 全局安装`sudo pip3 install pipenv`
   3. 用户安装`pip install --user pipenv`
   4. 检查安装`pipenv --version`

3. 创建虚拟环境：
   1. 切换至项目根目录
   2. 执行`pipenv install`

4. 虚拟环境目录：
   1. Windows:`C:\Users\Administrator\.virtualenvs`
   2. Linux:`~/.local/share/virtualenvs/`

5. 虚拟环境目录名称：`当前项目目录名+随机字符串`
6. 显式激活虚拟环境：
   1. 切换至项目目录
   2. `pipenv shell`
7. 退出虚拟环境：`exit`
8. 隐式激活虚拟环境：`pipenv run python app.py`
9. 安装`Flask`：`pipenv install flask`
10. 更新`Flask`：`pipenv update flask`
11. 创建程序实例;
    1.  导入类：
    ```python
    from flask import Flask
    # 实例化类
    app = Flask(__name__)
    ```
12. 注册路由：
在一个web应用里，客户端
    1.


