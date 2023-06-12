---
title: "Elementaryos键盘设置从系统设置面板中消失"
date: 2020-12-06T20:12:46+08:00
description:
tags: [linux, Bugs解决记录]
categories: Bugs解决记录
featured_image: "/images/notebook.png"
draft: false
comment: false
---

## 问题描述

本人正在使用 Elementary OS 5.1.7 Hera，某天突然想设置自定义快捷键，但是却发现键盘设置已经从系统设置面板中消失了，这叫人如何是好。于是就一阵百度，百度了个寂寞。国内用 Linux 的本来就少，用 Elementary OS 就可想而知，当然是少得可怜。所以关于这方面的资料基本都是一些老旧的东西，找不到解决问题的办法。最后还是我蹩脚的英语和谷歌拯救了我。

## 环境

- Elementary OS 5.1.7 Hera

## 解决办法

安装 `switchboard-plug-keyboard`和 `wingpanel-indicator-keyboard`这两个包即可！

```
sudo apt install switchboard-plug-keyboard
sudo apt install wingpanel-indicator-keyboard
```

## 参考来源

[https://elementaryos.stackexchange.com/questions/24711/keyboard-configuration-missing-from-system-settings](https://elementaryos.stackexchange.com/questions/24711/keyboard-configuration-missing-from-system-settings "https://elementaryos.stackexchange.com/questions/24711/keyboard-configuration-missing-from-system-settings")
