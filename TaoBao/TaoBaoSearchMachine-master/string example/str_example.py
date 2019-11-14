# -*- coding: utf-8 -*-
result = '''Stm32f103c8t6
0 0
Shop name:  risym旗舰店
Price:  [17.5, 9.8]
1 2
Shop name:  文鑫伟数码专营店
Price:  [5.88]
2 3
Shop name:  新亚洲兴佳电子
Price:  [6.5, 5.3]
3 4
Shop name:  上海芯城
Price:  [7.5, 5.8]
4 5
Shop name:  zhangyongweng998
Price:  [9.9, 26.0, 8.0]
5 6
Shop name:  优信电子企业店
Price:  [9.3, 6.4, 21.8]
6 8
Shop name:  深圳市持胜电子有限公司
Price:  [5.4, 5.4, 5.4]
7 9
Shop name:  深圳市义胜电子有限公司
Price:  [5.4]
8 10
Shop name:  深圳市万泰隆电子
Price:  [5.5, 4.2]
9 11
Shop name:  jayos企业店
Price:  [9.7, 9.5, 25.0]
10 12
Shop name:  信德电子
Price:  [8.7, 18.0, 16.5]
11 14
Shop name:  合肥飞宇单片机
Price:  [26.0]
12 15
Shop name:  深圳市海瑟威电子商行
Price:  [9.0, 8.7]
13 16
Shop name:  微芯华业数码专营店
Price:  [6.7]
14 17
Shop name:  evk123
Price:  [18.9]
15 19
Shop name:  楠兴数码专营店
Price:  [6.08, 3.6]
16 20
Shop name:  蓝缘886
Price:  [4.9, 5.66]
17 21
Shop name:  q1q2q3w1w2w31
Price:  [69.0, 18.9, 59.0]
18 22
Shop name:  电子元件大全
Price:  [7.25, 24.99]
19 23
Shop name:  chenzhiyang8
Price:  [58.0, 147.0]
20 24
Shop name:  hcx9144011
Price:  [18.0, 17.5, 7.0]
21 25
Shop name:  telesky旗舰店
Price:  [15.3, 35.6, 23.75, 9.8, 24.51]
22 26
Shop name:  sushini1994
Price:  [5.65, 5.1, 6.0]
23 27
Shop name:  光之翼zc
Price:  [19.88, 95.0]
24 28
Shop name:  华东小舟
Price:  [7.3, 5.8]
25 29
Shop name:  yang15986809048
Price:  [5.18, 5.4]
26 31
Shop name:  七星虫旗舰店
Price:  [23.9]
27 33
Shop name:  passonipaul
Price:  [65.0, 39.0, 9.9]
28 34
Shop name:  chenjunyang2009
Price:  [150.0, 11.8, 60.0]
29 35
Shop name:  zhaowen_win
Price:  [15.0]
30 36
Shop name:  佳仕通数码专营店
Price:  [9.85, 15.35, 15.9, 7.99, 28.0]
31 37
Shop name:  mtydz168
Price:  [5.7]
32 38
Shop name:  硬石电子
Price:  [198.0]
33 39
Shop name:  crisrita
Price:  [159.0, 68.0]
34 40
Shop name:  深圳大裕电子商行
Price:  [6.6, 5.55]
35 41
Shop name:  kylie丽人工作室
Price:  [13.7, 10.0, 27.0]
36 42
Shop name:  佳信微数码专营店
Price:  [18.0, 11.2, 25.0, 9.0]
37 43
Shop name:  瑶瑶美少女
Price:  [5.36, 5.8, 6.45]
38 44
Shop name:  selingna5555
Price:  [16.5, 16.8, 11.8, 13.5]
39 45
Shop name:  ping8165
Price:  [19.0, 9.0]
40 46
Shop name:  吴明武2013
Price:  [9.8, 150.0]
[17.5, 9.8, 5.88, 6.5, 5.3, 7.5, 5.8, 9.9, 26.0, 8.0, 9.3, 6.4, 21.8, 5.4, 5.4, 5.4, 5.4, 5.5, 4.2, 9.7, 9.5, 25.0, 8.7, 18.0, 16.5, 26.0, 9.0, 8.7, 6.7, 18.9, 6.08, 3.6, 4.9, 5.66, 69.0, 18.9, 59.0, 7.25, 24.99, 58.0, 147.0, 18.0, 17.5, 7.0, 15.3, 35.6, 23.75, 9.8, 24.51, 5.65, 5.1, 6.0, 19.88, 95.0, 7.3, 5.8, 5.18, 5.4, 23.9, 65.0, 39.0, 9.9, 150.0, 11.8, 60.0, 15.0, 9.85, 15.35, 15.9, 7.99, 28.0, 5.7, 198.0, 159.0, 68.0, 6.6, 5.55, 13.7, 10.0, 27.0, 18.0, 11.2, 25.0, 9.0, 5.36, 5.8, 6.45, 16.5, 16.8, 11.8, 13.5, 19.0, 9.0, 9.8, 150.0]
2311.28
24.3292631579
36.3982708161'''

# print result

a = 0.01
b = "def"
c = "ghi"

abc = []
abc.append(str(a))
abc.append(b)
abc.append(c)

c = ""
for i in range(len(abc)):
    c = c + " " + abc[i]
c = c.replace(" ",",")

print c






