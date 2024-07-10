---
title: "Python语言程序设计基础（第二版）嵩天高等教育出版社第二章答案"
date: 2020-10-18T20:05:47+08:00
description:
tags: [Python, 读书笔记]
categories: 读书笔记

draft: false
comment: false
---

2.2

```
TempStr = input("请输入带符号的金钱值(美元：$，人民币：￥)：")
if TempStr[-1] == '$':
    dollor = eval(TempStr[0:-1])
    rmb = dollor*6
    print("{}美元等于{}人民币".format(dollor,rmb))
elif TempStr[-1] == '￥':
    rmb = eval(TempStr[0:-1])
    dollor = rmb / 6
    print("{}人民币等于{}美元".format(rmb, dollor))
else:
    print("格式错误")
```

2.3

```
from turtle import *
week = ['black', 'grey', 'gold','violet','purple', 'green', 'red']
setup(0.99,0.99,0,0)
pensize(25)
penup()
fd(-250)
pendown()
seth(-40)
for i in range(4):
    pencolor(week[i])
    circle(40,80)
    pencolor(week[i])
    circle(-40,80)
circle(40, 40)
fd(40)
circle(16, 180)
fd(40*2/3)
done()
```

2.4

```
import turtle
def drawTriangle(length):
    turtle.fd(length)
    turtle.left(120)
    turtle.fd(length)
    turtle.left(120)
    turtle.fd(length)
    turtle.left(120)

turtle.setup(0.99,0.99,0,0)
turtle.pensize(10)
turtle.pencolor("red")
drawTriangle(300)
```

2.5

```
import turtle
def drawTriangle(length):
    turtle.fd(length)
    turtle.left(120)
    turtle.fd(length)
    turtle.left(120)
    turtle.fd(length)
    turtle.left(120)

turtle.setup(0.99,0.99,0,0)
turtle.pensize(3)
turtle.pencolor("red")

drawTriangle(200)
turtle.right(60)
drawTriangle(200)
turtle.right(60)
drawTriangle(200)
turtle.seth(0)
turtle.fd(200)
turtle.right(120)
drawTriangle(200)
turtle.done()
```

2.6

```
import turtle

turtle.setup(0.99,0.99,0,0)
turtle.pencolor("red")
turtle.pensize(3)
turtle.seth(90)
turtle.penup()
turtle.fd(200)
turtle.seth(0)
for i in range(4):
    turtle.penup()
    turtle.fd(100)
    turtle.pendown()
    turtle.fd(300)
    turtle.penup()
    turtle.fd(100)
    turtle.right(90)
turtle.done()
```

2.7

```
import math
import turtle
def drawTriangle(length):
    turtle.fd(length)
    turtle.left(120)
    turtle.fd(length)
    turtle.left(120)
    turtle.fd(length)
    turtle.left(120)
turtle.setup(0.99,0.99,0,0)
turtle.pensize(3)
turtle.pencolor("red")
# 设置边长和初始角度
turtle.seth(-30)
length = 200

drawTriangle(length)

turtle.penup()
turtle.fd(length/2)
turtle.right(90)
turtle.fd(math.sqrt(3) * length/6)
turtle.left(150)
turtle.pendown()

drawTriangle(length)
turtle.done()
```

2.8

```
import turtle as t
t.setup(0.99,0.99,0,0)
t.pencolor("red")
t.penup()
t.fd(-200)
t.seth(90)
t.pendown()

plus = 2
basic = 1
time = 300
for i in range(time):
    t.fd(basic)
    t.left(90)
    basic+=plus
t.done()
```

​
