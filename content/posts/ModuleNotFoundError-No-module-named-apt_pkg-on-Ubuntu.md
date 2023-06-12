---
title: "ModuleNotFoundError: No module named 'apt_pkg' on Ubuntu"
date: 2020-12-07T20:14:14+08:00
description:
tags: [linux, Bugs解决记录]
categories: Bugs解决记录
featured_image: "/images/notebook.png"
draft: false
comment: false
---

## 环境

- Ubuntu 18.04
- python 3.9

## 问题描述

手动更新了 python 版本到 3.9，原本的是 3.6 版本的。更换了默认的 python 版本之后，就会出现这样的错误。百度了一下，应该是因为包管理的版本还没有改过来，所以冲突了。解决方法就是更换一下软连接的链接文件。

## 解决方法

```
cd /usr/lib/python3/dist-packages/
sudo cp apt_pkg.cpython-36m-x86_64-linux-gnu.so apt_pkg.cpython-39m-x86_64-linux-gnu.so #修改成自己的版本
sudo ln -s apt_pkg.cpython-39m-x86_64-linux-gnu.so apt_pkg.so  #修改成自己的版本
```

成功解决！一些方法根本就不可用，这个软连接应该才是关键。

## 参考链接

[https://stackoverflow.com/questions/13708180/python-dev-installation-error-importerror-no-module-named-apt-pkg](https://stackoverflow.com/questions/13708180/python-dev-installation-error-importerror-no-module-named-apt-pkg "https://stackoverflow.com/questions/13708180/python-dev-installation-error-importerror-no-module-named-apt-pkg")

​
