---
title: "LibreOffice设置为中文字体"
date: 2021-07-09T20:37:35+08:00
description:
tags: [软件教程]
categories: 软件教程
featured_image: "/images/notebook.png"
draft: false
comment: false
---

## 前言

在 Manjaro 或者 Archlinux 中安装完 LibreOffice 之后，发现无法将其设置为中文字体。参考 Wiki 发现，还需要安装中文字体包，**libreoffice-fresh-zh-cn**

## 方法

首先安装字体包

```bash
sudo pacman -Sy libreoffice-fresh-zh-cn
```

之后打开 LibreOffice，依次点击`Tools->Options->Language Settings->Languages`点击切换到简体中文

![](https://img-blog.csdnimg.cn/20210709203451720.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTc0ODczNA==,size_16,color_FFFFFF,t_70)重启软件即可！
