---
title: "ERROR: Command errored out with exit status 1: when pip install scrapy 在Windows10上使用pip安装Scrapy时报错"
date: 2020-11-08T20:10:02+08:00
description:
tags: [Python, Bugs解决记录]
categories: Bugs解决记录
featured_image: "/images/notebook.png"
draft: false
comment: false
---

## 描述

环境：

- windows10 LTSC 1809
- python 3.9 64bit
- pip version :20.2.4

动作：

- pip install scrapy

错误信息：

> Running setup.py install for Twisted ... error
>
> ERROR: Command errored out with exit status 1:

![010a120e61966fbb68.png](https://img-blog.csdnimg.cn/img_convert/07d86a6915ff915161bea04d9a6be9e0.png)

## 查阅资料

经过谷歌之后，发现有许多人出现了这个错误。一种是缺少 Visual C++14 Tool，另一个问题就是缺少 Scrapy 的依赖包 \***\*[Twisted](https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted "Twisted")\*\*** 。所以，经过实践，只是安装 Visual C++14 Tool 还不行，还需要手动下载 Twisted 进行安装之后，再执行 `pip install scrapy`。

参考链接：[Error when install scrapy in window by using pip install scrapy · Issue #2881 · scrapy/scrapy · GitHub](https://github.com/scrapy/scrapy/issues/2881 "Error when install scrapy in window by using pip install scrapy · Issue #2881 · scrapy/scrapy · GitHub") 和 [在 python 3.8.1 上面安装 scrapy（报错显示说没有相关 twisted 文件/scrapy 安装失败）\_qq_43738233 的博客-CSDN 博客](https://blog.csdn.net/qq_43738233/article/details/106588512 "在python 3.8.1 上面安装scrapy（报错显示说没有相关twisted文件/scrapy安装失败）_qq_43738233的博客-CSDN博客")

## 解决方法

### 01

升级 pip `pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U`

升级 piptool `pip install -i https://pypi.tuna.tsinghua.edu.cn/simple piptool -U`

### 02

安装 Visual C++ Tool 组件，不用完全安装。链接：[百度网盘 请输入提取码](https://pan.baidu.com/s/17u_2gypf-G9eAvp_Ibhu-g "百度网盘 请输入提取码")

提取码：awxz

### 03

安装完成之后，手动安装 Twisted。下载相应版本的安装包(64 位或者 32 位) [https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted](https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted "https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted")

![20201108210252.png](https://img-blog.csdnimg.cn/img_convert/573454660c2bf071197fff8b18f4e4f5.png)

将文件复制到 python 文件夹中的 Scripts 文件夹中，例如我的是 `C:\Users\Ease Chen\AppData\Local\Programs\Python\Python39\Scripts`

在 Scripts 文件夹中打开终端，执行 `pip install Twisted-20.3.0-cp39-cp39-win_amd64.whl`

安装成功之后，再次执行 `pip install scrapy`，即可安装成功！！

​
