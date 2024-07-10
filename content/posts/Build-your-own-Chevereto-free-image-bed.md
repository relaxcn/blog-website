---
title: "搭建自己的Chevereto免费图床—写博客更加得心应手了！"
date: 2020-08-21T18:15:15+08:00
description:
tags: [软件教程]
categories: 软件教程

draft: false
comment: false
---

## 前言

自从有了个人博客，图片的上传和使用就成了一个亘古不变的问题和痛点。在网上找了很多免费的图床网站，虽然这种产业面临着随时跑路的危险，但也不乏一些确实很不错的网站。那么他们是怎么运作下去的呢，那当然就是 VIP 服务或者广告了。不冲 VIP 就会有图片大小和数量的限制，还会有一些烦人的广告出现。

所以，本教程就结合自身经历，给大家分享如何利用开源免费的 Cheverto 软件搭建一个免费的，自己掌控的图床。前提是得拥有一个云服务器或者自己的本地服务器。**至于如何搭建本地服务器，请看我的另一篇文章 [自建本地服务器，自建 Web 服务器——保姆级教程！](http://localhost:1313/posts/how-to-build-your-own-local-server-web-server/)。**

## 环境

1. 一台服务器（云服务器或者本地服务器）本例为 Centos 7.8
2. 宝塔面板 Nginx 环境
3. 域名

> 本文使用虚拟机演示，所以网站地址是虚拟机的内网 IP

### 安装宝塔面板

参考 [https://www.bt.cn/bbs/thread-19376-1-1.html](https://www.bt.cn/bbs/thread-19376-1-1.html) 在终端中输入

```
sudo yum install -y wget && wget -O install.sh http://download.bt.cn/install/install_6.0.sh && sh install.sh
```

## 搭建

### 准备

添加一个站点 [img.chens.life](https://img.chens.life)（根据自己喜欢），本例使用 IP 地址。**之后在自己域名的 dns 解析中添加相应解析条目。**

![02](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xOS8yMDIwMDgxOTE3NDkwMS5wbmc?x-oss-process=image/format,png#vwid=708&vhei=101)

创建一个数据库。

![03](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xOS8yMDIwMDgxOTE3NTAzMi5wbmc?x-oss-process=image/format,png#vwid=657&vhei=442)

在[https://github.com/Chevereto/Chevereto-Free/releases](https://chevereto.com/download/file/installer)下载最新在线安装文件。如果无法在线安装，下载离线安装包**本例使用离线安装方式，更加便捷**。

解压，上传至网站的根目录。修改目录文件权限为 777 。可以使用宝塔面板，也可以使用 shell 命令。在线安装的需要把`install.php`权限改为 777。同样的操作。

![04](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xOS8yMDIwMDgxOTE4MTMwMy5wbmc?x-oss-process=image/format,png#vwid=1636&vhei=805)

![05](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xOS8yMDIwMDgxOTE4MTMxMi5wbmc?x-oss-process=image/format,png#vwid=489&vhei=315)

### 修改伪静态配置

在`网站设置 > 伪静态`中填入

```
location / {
    if (-f $request_filename/index.html){ rewrite (.*) $1/index.html break; } if (-f $request_filename/index.php){ rewrite (.*) $1/index.php; } if (!-f $request_filename){ rewrite (.*) /index.php; } try_files $uri $uri/ /api.php; } location /admin { try_files $uri /admin/index.php?$args;
    }
```

确定保存。

### 安装

在浏览器中打开网址**`http://192.168.116.134/`**，在线安装的打开网址**`http://192.168.116.134/installer.php`**。将我的 IP 地址替换为自己设置的网址。

![10](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xOS8yMDIwMDgxOTE5MDkwNC5wbmc?x-oss-process=image/format,png#vwid=1008&vhei=904)

填写基本的用户名和密码，更改一下网站模式。社区模式中，游客可以上传文件使用。

![08](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xOS8yMDIwMDgxOTE5MTExNC5wbmc?x-oss-process=image/format,png#vwid=844&vhei=922)

完成安装后，直接进入管理控制台，需要登录进入。

![09](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xOS8yMDIwMDgxOTE5MTIyOS5wbmc?x-oss-process=image/format,png#vwid=860&vhei=251)

### 更改控制台语言

进入控制台之后，点击 设置 > 语言，选择 简体中文，稍等片刻。

![11](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xOS8yMDIwMDgxOTE5NDM0Ni5wbmc?x-oss-process=image/format,png#vwid=983&vhei=523)

![12](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xOS8yMDIwMDgxOTE5NDM1NC5wbmc?x-oss-process=image/format,png#vwid=778&vhei=330)

**保存之后不会立即更换，需要等待一段时间**。安装完成。

### 设置封面图片、网站名称、最大上传大小

在 **仪表盘**的 **网站**中设置网站名称、标题、各种功能的设定。

在 **图片上传**中可设置最大上传大小（游客或注册用户的）。

在 **主页**中可设置背景图片。

## 使用 PicGo 配合

### 下载安装 PicGo

[https://github.com/Molunerfinn/PicGo/releases](https://github.com/Molunerfinn/PicGo/releases)

#### 获取 API v1 key

在仪表盘，设置，API 中查找。

![13](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xOS8yMDIwMDgxOTE5NTYwNy5wbmc?x-oss-process=image/format,png#vwid=711&vhei=306)

### 配置 PicGo

#### 搜索安装 web-uploader 插件

![14](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xOS8yMDIwMDgxOTE5NTgwNS5wbmc?x-oss-process=image/format,png#vwid=1000&vhei=564)

#### 配置插件

在 API 地址中填入，将 IP 换成自己的域名。

```
http://192.168.116.134/api/1/upload
```

post 参数填入 `source`，JSON 路径填入 `image.url`，自定义 Body 中填入

```
{"key":"5b163035fb0ab96a7f68416f60d96abf"}
```

将后面的 API key 换成自己的。点击确定，设置成默认图床。

![15](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xOS8yMDIwMDgxOTE5NTgyNy5wbmc?x-oss-process=image/format,png#vwid=1000&vhei=564)

以后只要将图片拖入即可自动上传获得想要的地址。

## 结语

本教程结合亲身经历分享给大家，希望能够帮助到他人。
