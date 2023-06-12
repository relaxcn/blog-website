---
title: "failed to resolve: maybe a missing crate  front_of_house ?failed to resolve: use of undeclared crate"
date: 2021-04-22T20:24:36+08:00
description:
tags: [Rust]
categories: Rust, Bugs解决记录
featured_image: "/images/notebook.png"
draft: false
comment: false
---

## 前言

在学习 Rust 时，官方文档 的 7.3 节的例子中(创建模块和引用)，出现了以下错误：

![](https://img-blog.csdnimg.cn/img_convert/a7cfe974fa81cd80957b614c95c82c8a.png)

## 解决方法

方法也很简单，如果是使用 cargo new --lib name 创建的模块的话，默认在 src/lib.rs 中的第一行会添加：

```bash
#[cfg(test)]
```

只要注释掉这一行即可。即

```bash
//#[cfg(test)]
```
