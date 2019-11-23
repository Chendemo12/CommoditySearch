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


## 3. 模板template
   + 包含固定内容和动态部分的可重用文件称为模板；
1. 常见的3种定界符：
   1. 语句
   比如`if`判断、`for`循环等:   `{% ... }`
   2. 表达式
   比如字符串、变量、函数调用等：`{{ ... }}`
   3. 注释：`{# ... #}`
   4. 在模板中，Jinja2支持使用`.`获取变量的属性，比如user字典中的username键值通过`.`获取，即`user.username`，效果上等同于`user['username']`。

2. 模板`if`语句语法：
   ```python
    {% if user.bio %}
        <i>{{ user.bio }</i>}
    {% else %}
        <i>This user has not provided a bio.</i>
    {% endif %}
    ```
    语句使用`{% ... %}`标识，在语句结束的时候，必须添加结束标识`{% endif %}`
3. 模板`for`语句语法：`for`语句用来迭代一个序列
   1.
   ```python
    {% for movie in movies %}
        <li>{{ movie.name }} - {{ movie.year }}</li>
    {% endfor %}
    ```
    语句使用`{% ... %}`标识，在语句结束的时候，必须添加结束标识`{% endfor %}`
   2. 常见的循环变量：
    | 变量名         | 说明                          |
    | :------------- | :---------------------------- |
    | loop.index     | 当前迭代数（从1开始计数）     |
    | loop.index0    | 当前迭代数（从0开始计数）     |
    | loop.revindex  | 当前反向迭代数（从1开始计数） |
    | loop.revindex0 | 当前反向迭代数（从0开始计数） |
    | loop.first     | 如果是第一个元素，则为True    |
    | loop.last      | 如果是最后一个元素，则为True  |
    | loop.previtem  | 上一个迭代的条目              |
    | loop.nextitem  | 下一个迭代的条目              |
    | loop.length    | 序列包含的元素数量            |

