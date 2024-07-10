---
title: "openSSH实现免密登录"
date: 2021-02-09T20:20:05+08:00
description:
tags: [linux, openssh]
categories: Linux笔记

draft: false
comment: false
---

## 001

首先在客户端使用 `ssh-keygen -t rsa` 生成一对密钥，当系统提示输入与密钥相关的密码时，直接按下 `Enter` 键即可。

这样，会在 `~/.ssh/` 下生成两个密钥，一个是私钥 `id_rsa`，一个是公钥 `id_rsa.pub`。

![image-20210213161224537](https://img-blog.csdnimg.cn/img_convert/8902a82dfa657036c707dad325bf04f1.png)

## 002

使用 `scp`命令将公钥 `id_rsa.pub` 上载到远程服务器中的 `~/.ssh/`中，

![image-20210213162146448](https://img-blog.csdnimg.cn/img_convert/b48417639995a1ec7054c07a0614cb8d.png)

转移到远程机器中，并将其内容追加到同一目录中的 `authorized_keys` 中。

![image-20210213162317011](https://img-blog.csdnimg.cn/img_convert/99aa49611bd613bf8dcc505962ed042c.png)

## END

![image-20210213162456242](https://img-blog.csdnimg.cn/img_convert/4e939b8bbf5ba27f2cfa59a1e8d9573b.png)

​
