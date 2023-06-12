---
title: "Python语言程序设计基础（第二版）嵩天高等教育出版社第四章答案"
date: 2020-10-25T20:05:47+08:00
description:
tags: [Python, 读书笔记]
categories: 读书笔记
featured_image: "/images/notebook.png"
draft: false
comment: false
---

4.1

```
from random import randint
x = randint(0,9)
print("猜数游戏，请输入0到9之间的整数".center(20,'*'))
n = eval(input("请输入："))
i= 1
while n != x:
    if n > x:
        print("太大了！")
    elif n < x:
        print("太小了！")
    n = eval(input("请输入："))
    i += 1

print("预测{}次，你猜中了!".format(i))
```

4.2

```
print("统计各个类型的字符数量".center(20,'*'))
Str = input("请输入一串字符：")

char, number, space, other = 0,0,0,0
for i in Str:
    if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
        char += 1
    elif '0' <= i <= '9':
        number += 1
    elif i == ' ':
        space += 1
    else:
        other += 1
print("有{}个英文字母，{}个数字，{}个空格，{}个其他字符。".format(char, number, space, other))
```

4.3

```
num1, num2 = eval(input("请输入两个整数，用逗号隔开:"))
max = 1
min = 1
i = 1
# 储存输入的值，以便后续使用
a, b = num1, num2
while i <= num1 if num1<=num2 else num2:
    if num1%i == 0 and num2%i == 0:
        max *= i
        num1, num2 = num1/i, num2/i
        # 把i充值为1
        i = 1
    i += 1
min = a*b/max
print("最大公约数为{}，最小公倍数为{}".format(max,min))
```

4.4

```
from random import randint
x = randint(0,100)
print("猜数游戏，请输入0到100之间的整数".center(20,'*'))
n = eval(input("请输入："))
i= 1
while n != x:
    if n > x:
        print("太大了！")
    elif n < x:
        print("太小了！")
    n = eval(input("请输入："))
    i += 1

print("预测{}次，你猜中了!".format(i))
```

4.6

```
from random import *
times = 1000000
NoChangeRight = 0
ChangeRight = 0
for i in range(times):
    # 设置1号和2号门后面是山羊
    hit = randint(1,3)
    if hit in [1,2]:
        NoChangeRight += 1
# 改变时，需选择一个与之前不同的门
    ReHit = randint(1,3)
    while ReHit == hit:
        ReHit = randint(1,3)

    if ReHit in [1,2]:
        ChangeRight += 1

NoChange = NoChangeRight/times
Change = ChangeRight/times
print("不改变的获胜几率为{}，反之为{}".format(NoChange, Change))
```

4.7

```
from random import randint
x = randint(0,9)
print("猜数游戏，请输入0到9之间的整数".center(20,'*'))
# 获取正确的数字
while True:
    try:
        n = eval(input("请输入："))
    except:
        print("错误，必须输入一个整数！")
    else:
        break
i= 1
while n != x:
    if n > x:
        print("太大了！")
    elif n < x:
        print("太小了！")
        # 获取正确的数字
    while True:
        try:
            n = eval(input("请输入："))
        except:
            print("错误，必须输入一个整数！")
        else:
            break

    i += 1

print("预测{}次，你猜中了!".format(i))
```

​
