---
title: "NextCloud如何通过修改数据库表，达到替换文件而不改变分享的链接地址的效果，以及自定义分享的链接地址"
date: 2020-08-23T19:44:59+08:00
description:
tags: [软件教程]
categories: 软件教程

draft: false
comment: false
---

## 前言

近日有一些已经分享过的文件需要修改或者调整，但是如果再次上传分享的话，之前的链接就会失效。有没有即**不改变分享的链接地址**，又能够**替换**已经分享过的文件的方法呢？

我在百度 Google 上搜索一番就发现，根本没有人有这样的经历或者需求，那我还真算是个奇葩······折腾一番之后无果，我开始思考：链接的地址会不会写入了数据库表中呢？能不能修改相关的数据库表的数据来达到**重新指向新的分享文件，还不改变之前的分享链接**呢？如果可行的话，甚至还可以**自定义分享链接**！

## 方法

通过宝塔面板打开 next cloud 的数据库

![01](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8yMy8yMDIwMDgyMzE3NDc0OS5wbmc?x-oss-process=image/format,png)

打开自己 next cloud 的数据库表，搜索 `share`，找到 `oc_share`，点击浏览

![02](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8yMy8yMDIwMDgyMzE3NDgxOS5wbmc?x-oss-process=image/format,png)

之后就会发现，所有的分享数据都在这张表中！且是一一对应的关系。

![03](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8yMy8yMDIwMDgyMzE3NDgyOS5wbmc?x-oss-process=image/format,png)

包括文件的路径，和分享的后缀链接（这个就是一个固定的字符串`token`）。而我们要做的就很简单了，在自己希望替换文件的那个分享链接的那条数据中，将`file_target`指向新的文件就大功告成了！

同时，如果希望自定义链接地址，也可以修改表中的 `token`的那串字符。

![04](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8yMy8yMDIwMDgyMzE3NDgzOS5wbmc?x-oss-process=image/format,png)

## 结语

本文结合亲身经历分享给大家，希望能够帮助到他人。
