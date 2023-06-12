---
title: "Ubuntu Linux下禁止服务开机自启动"
date: 2020-12-29T20:15:19+08:00
description:
tags: [linux]
categories: Linux笔记
featured_image: "/images/notebook.png"
draft: false
comment: false
---

​## 前言

由于学习需要，电脑上安装了 MSSQL 和 MySQL。目前课程已经结束，暂时用不到数据库了。但是他们还是会在开机自启，而且占用的内存还不少，尤其是 MSSQL。所以就查了一下怎么禁止他们开机自启。

## 使用 Systemctl 管理工具

```
systemctl is-enabled servicename.service #查询服务是否开机启动
systemctl enable *.service #开机运行服务
systemctl disable *.service #取消开机运行
systemctl start *.service #启动服务
systemctl stop *.service #停止服务
systemctl restart *.service #重启服务
systemctl reload *.service #重新加载服务配置文件
systemctl status *.service #查询服务运行状态
```

我们要使用的就是 `systemctl disable mssql-server.service `和 `systemctl disable mysql.service `，输入 root 密码即可关闭服务自启！

​
