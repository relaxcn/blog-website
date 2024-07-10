---
title: "PicGo配合Typora怎么配置Chevereto图床，PicGo的Chevereto图床配置"
date: 2020-08-21T18:23:04+08:00
description:
tags: [软件教程]
categories: 软件教程

draft: false
comment: false
---

## 前言

搭配我之前的文章观看哦~：

1. [自建本地服务器，自建 Web 服务器——保姆级教程！](https://chens.life/how-to-build-your-own-local-server-web-server/)
2. [Chevereto 免费图床搭建教程 | vps 搭建免费图床教程](https://chens.life/build-your-own-chevereto-free-image-bed/)

搭建完 Chevereto 私有图床之后，我就开始就开始发愁。图片一个一个单独上传太麻烦了，能不能一键上传添加到文章中呢？答案当然是可以的。

我目前在使用的 MarkDown 编辑器是 Typora，干净简洁，即时渲染很方便，我一直在用。官网：https://typora.io/。Typora设置里面有专门的图床设置， 需要配合 PicGo 来实现。

## 实现前提

- 获取 API v1 key（在 Chevereto 仪表盘 > 设置 > API 中查看）
- 安装 PicGo
- 安装 Typora

PicGo 的官网https://molunerfinn.com/PicGo/

Typora 的官网https://typora.io/

## 过程

### 配置 PicGo

安装`web-uploader`这个插件

![01](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8yMS8yMDIwMDgyMTE1MDUyOS5wbmc?x-oss-process=image/format,png)

配置你的自定义图床设置

![](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8yMS8yMDIwMDgyMTE1MjEzMy5wbmc?x-oss-process=image/format,png)

将我的网址换成自己的，POST 参数名填入`suorce`，JSON 路径填入`image.url`，自定义 Body 填入{"key":"自己的 API key"}。点击确定，设为默认图床。

### Typora 配置

文件 > 偏好设置 > 图像中修改设置如下，

![03](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8yMS8yMDIwMDgyMTE1MjcxNS5wbmc?x-oss-process=image/format,png)

点击验证图片上传即可验证是否成功。

## 错误

### 错误一：Failed to fetch

这是 PicGo 的端口设置错误导致的。打开 `PicGo设置 > 设置Service`，将端口设置为 36677。

![04](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8yMS8yMDIwMDgyMTE1Mjk1MS5wbmc?x-oss-process=image/format,png)

### 错误二：{“success”,false}

这是上传了相同文件名的文件导致的，PicGo 不允许上传同文件名的文件。

在`PicGo设置`中开启 `时间戳上传`即可解决。

![05](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8yMS8yMDIwMDgyMTE1MzE0Ni5wbmc?x-oss-process=image/format,png)
