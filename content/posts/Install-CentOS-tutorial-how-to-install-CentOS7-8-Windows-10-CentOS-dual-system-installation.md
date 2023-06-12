---
title: "安装CentOS教程，如何安装CentOS 7.8，Windows 10，CentOS双系统安装"
date: 2020-08-21T18:12:13+08:00
description:
tags: [软件教程]
categories: 软件教程
featured_image: "/images/notebook.png"
draft: false
comment: false
---

## 为 CentOS 系统分配硬盘空间

目前有两种方案，一种是一块硬盘上的双系统，另外一种是单独安装在一块硬盘上面（这个不需要多说），我们主要说一下在一块硬盘上为 CentOS 分配空间。

搜索 **创建并格式化硬盘分区**，或者 右键开始菜单，选择 **磁盘管理**。找到有空余空间的磁盘点击 **压缩卷**。

根据自己的需求分配空间大小，这个分配 20G 做个示范。

## 制作安装盘

### 下载 CentOS 7.8 ISO 镜像文件

这里从 [阿里云开源镜像站](https://developer.aliyun.com/mirror/centos?spm=a2c6h.13651102.0.0.3e221b11eBXSZk)，下载 CentOS 7.8 ，直链 https://mirrors.aliyun.com/centos/7.8.2003/isos/x86_64/CentOS-7-x86_64-DVD-2003.iso。

### 安装 balenaEtcher

https://www.balena.io/etcher/，下载安装。由于国内速度不好，本站提供最新版(2020.8.15)备份，[balenaEtcher](https://nas.chens.life/index.php/s/5mYmg5RSs6HMW96)。密码:`chens.life`。

### 制作安装盘

打开 balenaEtcher，选择镜像文件和 U 盘，等待制作完成。

![](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xNS8yMDIwMDgxNTEyMzI1OC5wbmc?x-oss-process=image/format,png)

## 安装系统

开机进入 BIOS 设置 U 盘为第一启动项，或者开机按 F12 UEFI 启动（不同的主板型号，按键有所不同，请自行查询）。

**选择第二项 `Test this media & install CentOS 7`**

![02](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xNS8yMDIwMDgxNTE4NTkxNy5wbmc?x-oss-process=image/format,png)

**选择语言**

![03](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xNS8yMDIwMDgxNTE5MDAxMy5wbmc?x-oss-process=image/format,png)

选择 `软件 > 软件选择`，一般选择 GNOME 桌面，图形界面系统更容易入手和操作。

![04-1](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xNS8yMDIwMDgxNTE5MDEzMS5wbmc?x-oss-process=image/format,png)

![05](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xNS8yMDIwMDgxNTE5MDI0OS5wbmc?x-oss-process=image/format,png)

然后选择`系统 > 安装位置`，在这一步中，选择你想要安装的硬盘或者刚才分配的硬盘分区。有能力的可以自己配置分区，不过自动配置分区足矣。

![06](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xNS8yMDIwMDgxNTE5MDMyNy5wbmc?x-oss-process=image/format,png)

如果想要回收空间或者格式化硬盘，勾选`我想让额外空间可用`，这样就可以格式化这些空间了。选择想要回收的空间，点击`删除`，之后`回收空间`即可，点击**完成**。

![07](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xNS8yMDIwMDgxNTE5MDU0Ny5wbmc?x-oss-process=image/format,png)

在等待其安装的过程中，我们设置一下 root 密码和普通用户名和密码。

![08](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xNS8yMDIwMDgxNTE5MDc1OS5wbmc?x-oss-process=image/format,png)

设置普通用户密码时，如果密码过弱，则需要点击两次`完成`才可以确认。勾选`将此用户作为管理员`，这样一来，我们便可以让普通用户使用自己的密码拥有 **暂时拥有 root 权限** 的权利，避免了来回切换用户的麻烦。

![09](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xNS8yMDIwMDgxNTE5MDgxMC5wbmc?x-oss-process=image/format,png)

之后耐心等待安装完成，全部完成之后，点击`重启`即可。

![10](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xNS8yMDIwMDgxNTE5MTAwMS5wbmc?x-oss-process=image/format,png)

重启之后，我们还需要接受一个许可证，才可以授权使用 GNOME 图形界面软件。选择不带有图形界面的软件安装，则不会出现。

![11](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xNS8yMDIwMDgxNTE5MTEwNi5wbmc?x-oss-process=image/format,png)

安装完成，如果想以 root 用户登录，则还需要点击更多用户，手动输入 root 账户进行登录。不过我不建议这样做，root 的权限太高，容易对系统造成破环。正常使用的话，使用一般用户即可。如果暂时需要 root 权限，则可使用`sudo`暂时取得 root 权限。

![12](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xNS8yMDIwMDgxNTE5MTU1Ny5wbmc?x-oss-process=image/format,png)

至此，安装过程完全结束。

## 结语

本教程仅为简单的安装概括，希望能够帮助到他人。
