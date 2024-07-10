---
title: "vscode在编译c\\c++时报错“The PrelaunchTask ‘g++‘ terminated with exit code 1“"
date: 2021-06-16T20:35:45+08:00
description:
tags: [Bugs解决记录, CC++]
categories: Bugs解决记录

draft: false
comment: false
---

​## 原因

我这里是因为之前在 Linux 的项目完整的复制到了 Windows 下面，所以`gcc`和`gdb`的路径配置错误，只需要修改当前目录下`.vscode`中的配置文件中的路径地址即可。

![image-20210616224623597](https://img-blog.csdnimg.cn/img_convert/57917682a98b8228da1b34091ed8b05d.png)

## 操作

修改`gcc`和`gdb`的路径即可。

![image-20210616224718715](https://img-blog.csdnimg.cn/img_convert/cb26a783d692af458c3e051268ddf383.png)

![image-20210616224737532](https://img-blog.csdnimg.cn/img_convert/05c8fd7c4eadd01af474524e85417dae.png)
