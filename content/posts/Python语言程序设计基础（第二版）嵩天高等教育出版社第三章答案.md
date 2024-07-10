---
title: "Python语言程序设计基础（第二版）嵩天高等教育出版社第三章答案"
date: 2020-10-25T20:05:47+08:00
description:
tags: [Python, 读书笔记]
categories: 读书笔记

draft: false
comment: false
---

3.1

```
step = 0.5
year = 10
weight = eval(input("请输入你在地球上的重量(KG)："))

weight_in_earth = weight+year*step
weght_in_month = weight_in_earth*0.165
print("十年后，你的体重为：\n地球上：{:.2f}\n月球上：{:.2f}".format(weight_in_earth, weght_in_month))
```

3.2

```
# 连续学习的天数
x = 0
# 天数
day = 0
# 初始能力值
base = 1
# 周期
cycle = 7

for day in range(365):
    if 0 <= x < 3:
        x += 1
    elif 3 <= x < cycle:
        x += 1
        base *= (0.01+1)
    elif x == 7:
        x = 0
print("连续学习365天后，能力值为{:.2}".format(base))
```

3.3

```
# 连续学习的天数
x = 0
# 天数
day = 0
# 初始能力值
base = 1
# 周期
cycle = 7

for day in range(365):
    # 每十天休息一次
    if day%10 == 0:
        x = 0
    elif 0 <= x < 3:
        x += 1
    elif 3 <= x < cycle:
        x += 1
        base *= (0.01+1)
    elif x == 7:
        x = 0
print("连续学习365天后，能力值为{:.2}".format(base))
```

3.4

```
print("判断是否为回文数".center(20,'-'))
number = input("请输入一个数字：")
# 反转字符串
reverseNumber = number[::-1]

if eval(reverseNumber) == eval(number):
    print("这个数字是回文数")
else:
    print("不是回文数")
```

3.5

```
print("+ - - - - + - - - - + - - - - +")
for i in range(4):
    print("\n|         |         |         |")
print("\n")
print("+ - - - - + - - - - + - - - - +")
for i in range(4):
    print("\n|         |         |         |")
print("\n")
print("+ - - - - + - - - - + - - - - +")
```

3.6

```
import time
print("程序开始".center(50,'-'))
print("Starting", end='')
for i in range(50):
    print("·",end='')
    time.sleep(0.1)
print("Done!")
print("程序结束".center(50,'-'))
```

3.7

> 这道题虽然是让观察结果，但是书中给出的有一些小的瑕疵。仔细观察就可以发现，转动的并不是按照顺序转的，应该把第三个和第四个字符调换才正确！

```
import time
while True:
    for i in ["/", "-", "\\","|", "|"]:
        print("{:s}\r".format(i),end='')
        time.sleep(0.1)
```

3.8

> 首先需要安装 tqdm 第三方库，但是实际运行的结果并不是那么好。不知道书的作者是怎么想的。

```
pip install tqdm
```

​
