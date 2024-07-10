---
title: "Manjaro安装搜狗中文输入法"
date: 2021-07-26T20:51:12+08:00
description:
tags: [linux]
categories: Linux笔记

draft: false
comment: false
---

​ 本文用于分享和备忘，使用于最新的 Manjaro 版本

## 过程

本教程仅限使用于 **Manjaro 的最新版本** ，Arch 系其他系统使用出错本人**概不负责**

首先，确认自己具有如下的先决条件：

- 自己的 Manjaro 已经配备好了 archlinuxcn 源，如没有，请按照如下命令添加清华大学的 archlinuxcn 源：

```bash
sudo vim /etc/pacman.conf 或 sudo nano /etc/pacman.conf
```

并在文件中插入以下内容：

```
[archlinuxcn]
Server = https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/$arch
```

勘误：随后应该执行如下命令再继续操作：

```
sudo pacman -Sy archlinuxcn-keyring
```

P.S.：上方清华源可以替换为其他源，例如中科大源

- 自己的 Manjaro 已经安装好了 yay，如没有，请按照如下命令安装：

```bash
sudo pacman -Sy yay
```

然后，请按照如下命令进行配置：

```bash
sudo pacman -Sy fcitx
sudo pacman -Sy fcitx-configtool
sudo pacman -S base-devel
yay fcitx-sogoupinyin
yay fcitx-qt4
# 以上四步是fcitx和搜狗拼音的配置
```

执行完后请继续执行如下一条命令：

```bash
vim ~/.xprofile
```

这时你会获得一个文件，在这个文件中加入如下内容：

> export GTK_IM_MODULE=fcitx
>
> export QT_IM_MODULE=fcitx
>
> export XMODIFIERS="@im=fcitx"

之后，注销即可

作者：Sun 思晴

链接：[manjaro Linux，有什么较为简单的方法，可安装中文输入法? - 知乎](https://www.zhihu.com/question/330715155/answer/1437640623 "manjaro Linux，有什么较为简单的方法，可安装中文输入法? - 知乎")

来源：知乎

著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
