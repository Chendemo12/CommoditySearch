# -*- encoding: utf-8 -*-
# @Author:  LiChenguang
# @Data  :  2020/02/27
# @Email :  chendemo12@gmail.com
# @sys   :  Ubuntu 18.04
# @WebSite: www.searcher.ltd
# @Last Modified time:  2020/02/27


from flask import Flask
from flask import render_template


app = Flask(__name__)
#app.config.from_pyfile('setting.py')



@app.route('/')
def index():
    return render_template('base.html')



if __name__ == "__main__":

   index()