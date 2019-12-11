# -*- encoding: utf-8 -*-
# @Author  :  LiChenguang
# @Data  :  2019/12/07
# @Email  :  chendemo12@gmail.com
# @sys  :  elementary OS
# @WebSite  :  www.searcher.ltd
# @Last Modified time  :  2019/12/07


from tmRankSpyder import TmRankSpyder   # 天猫商品爬虫
from dataClean import DataClean         # 数据清洗类


# 实例化类
TmRankSpyder = TmRankSpyder()
DataClean = DataClean()

# 商品名列表
good_list = DataClean.get_GoodsList()
# 已爬取的商品名
good_gotten = []
# 未爬取的商品名
good_never = good_list


TmRankSpyder.login() #登录
TmRankSpyder.get_FirstPageRank(good_list)
