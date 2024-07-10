---
title: "利用阿里云服务器免费体验wordpress博客个人网站"
date: 2020-09-25T20:00:37+08:00
description:
tags: [网站教程]
categories: 网站教程

draft: false
comment: false
---

​## 前言

目前市面上有许许多多的虚拟云服务器 ECS，例如阿里云、华为云、又拍云等等，他们提供很多的云服务，但 ECS 是个很重要的项目。它就相当于一台远程的电脑，我们可以在上面搭建自己需要的各种服务。使用厂商提供的的 ECS 的最大的好处就是其稳定性，不用担心故障或者数据丢失又或者是停电。

本例就以阿里云 ECS，加上久负盛名的 word press 这个强大的软件来进行演示，搭建一个属于自己的一片小天地，开始自己的创作之旅。

## 云服务器

然后，我们需要一台云服务器，可以使用[阿里云的学生机](https://promotion.aliyun.com/ntms/act/campus2018?spm=5176.12825654.gzwmvexct.d119.1d002c4aNTahpe&scm=20140722.2530.1.2512 "阿里云的学生机")，每月 9.9 非常的便宜。也可以注册体验阿里云的免费限时的云服务器[基于 ECS 搭建云上博客 - 云起实验室-在线实验-上云实践-阿里云开发者社区-阿里云官方实验平台-阿里云](https://developer.aliyun.com/adc/scenario/fdecd528be6145dcbe747f0206e361f3?spm=5176.229592.3969757060.1.38ef3d92S4cxI8 "基于ECS搭建云上博客 - 云起实验室-在线实验-上云实践-阿里云开发者社区-阿里云官方实验平台-阿里云")

注册登录就可以看到自己服务器的公网 IP 和相关信息。

![](https://img-blog.csdnimg.cn/img_convert/e651cc5823b475ea5c24e058815d2a63.png)

再点击创建资源，等待创建完成，在这里，我们不适用阿里云官方的教程，我们用宝塔面板将会更加的便捷和简单。

![](https://img-blog.csdnimg.cn/img_convert/42f62877675bc6c276d4e2e61e7046ed.png)

## 安装宝塔面板

使用 shell 软件进行登录，见我之前的文章 [如何申请 XShell 和 XFtp 的免费家庭学生版本](https://chens.life/How-to-apply-for-the-free-XShell-and-XFtp.html "如何申请XShell和XFtp的免费家庭学生版本")。

![](https://img-blog.csdnimg.cn/img_convert/a8be22c75098deab29ae1061be7ac5f3.png)

输入刚才的 IP 地址，名称随意，端口为 22，

![](https://img-blog.csdnimg.cn/img_convert/8d754c5304dc0806edbd4fa5807065ac.png)

输入用户名为 root，

![](https://img-blog.csdnimg.cn/img_convert/d5542d0c1e6a6d65a638d9627f692fa3.png)

输入刚才得到的密码，点击确定。

![](https://img-blog.csdnimg.cn/img_convert/9c4d15177e315cf172ec4471991962b4.png)

之后进行连接，即可成功连接。

在 shell 中输入 `yum install -y wget && wget -O install.sh http://download.bt.cn/install/install_6.0.sh && sh install.sh`，耐心等待安装完成。

![](https://img-blog.csdnimg.cn/img_convert/4999aef2bd118ae27f5ebcba2598da94.png)

输入 `y`

![](https://img-blog.csdnimg.cn/img_convert/3584088498f6e8f520d3130c99731561.png)

安装完成后进行后台登录，复制外网面板地址，使用用户名和密码进行登录。

![](https://img-blog.csdnimg.cn/img_convert/a59daab5b07b614787ecf3e591ba1d64.png)

![](https://img-blog.csdnimg.cn/img_convert/f72dc92521fcb928aaf7642ec82b0356.png)

![](https://img-blog.csdnimg.cn/img_convert/b74672a28cff5259694e35dc6c6ea2e3.png)

## 安装网页环境

第一次启动会让其选择想要的网站部署环境，推荐 LNMP，更加节省资源。

![](https://img-blog.csdnimg.cn/img_convert/77a8702a8cac321aa2ef756f34afe463.png)

等待安装完成。

![](https://img-blog.csdnimg.cn/img_convert/60394942253d12785338cc470d89d617.png)

## 一键安装 word press

在软件商店中，选择一键部署，在选择第一个 Word Press

![](https://img-blog.csdnimg.cn/img_convert/8755af9de19c8c428038a0a230419d78.png)

填入域名，这里我是用 IP 地址，你可以替换为自己的域名，不过要提前设置域名解析到此 IP 地址。

![](https://img-blog.csdnimg.cn/img_convert/79025af77852c8654116e9564bd41edd.png)

点击进入安装界面，这里的数据库账号资料后面要使用。

![](https://img-blog.csdnimg.cn/img_convert/5e9d9f6a33f2d374b3db62d384312ae6.png)

![](https://img-blog.csdnimg.cn/img_convert/a8abc520402f7db698a78527be519a47.png)

![](https://img-blog.csdnimg.cn/img_convert/67e70d7457726534d477368ed41d3f93.png)

![](https://img-blog.csdnimg.cn/img_convert/80d366daf7efcdfd7d2c4b384d3b4424.png)

![](https://img-blog.csdnimg.cn/img_convert/75c6249d33f0da76766ed3b1e35ff197.png)

至此，博客的安装就完成了，我们在浏览器地址输入刚才设置的 IP 地址或者是自己的域名后，即可访问到我们的博客页面。

![](https://img-blog.csdnimg.cn/img_convert/1fe8f218b2d089f5457f0e11b806d633.png)

![](https://img-blog.csdnimg.cn/img_convert/24682877baacb892402bdec9c5135f04.png)

## 后台管理

浏览器输入`IP地址或者自己的域名/wp-login.php`,即可进入登录界面，输入刚才设置的用户名和密码即可进入后台。

![](https://img-blog.csdnimg.cn/img_convert/c0953b91ae4aa9910024d2c5319d1c34.png)

## 后记

word press 是一个强大的建站程序，全球许多大型企业或者中小企业都在使用。它不仅仅局限于个人博客，很多商业网站也能很好的应对。

本文只是个再简单不过的基础教程，更多的高级用法等待你的发掘！
