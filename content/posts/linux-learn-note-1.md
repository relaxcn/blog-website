---
title: "Linux学习日志第一天——基础命令①"
date: 2020-04-04T17:56:13+08:00
description:
tags: [linux]
categories: linux笔记

draft: false
comment: false
---

### 前言

趁着今天放假，我终于打开了收藏夹里吃了好长时间灰的 Linux 学习视频（呜呜呜~~，我对不起你~）。谨以此系列博客记录和巩固所学知识。

今天主要是 Linux 基础命令：

1. ls，及其相关选项
2. pwd
3. cd
4. mkdir，及其相关选项

### 命令的作用及基本构成

命令是用来告知 Linux 系统，并与 Linux 系统进行交互的一种语言。其主要使用场景是在终端窗口中，这也是上世纪操作系统的主流交互方式，例如微软早期的 DOS 系统，如今仍保留在 Windows 系统中的 CMD（命令提示符），还有 mac 中的终端窗口。

在 Linux 中，一串完整的命令主要由以下几个部分构成：1、命令关键字 2、选项 3、操作对象（或路径）。即形如：`关键字 【选项】 【操作对象（或路径）】` 这样的字段。【】号括起来的部分可以省略。

> 另外：关于详细的选项说明，可以使用命令：关键字 --help 来获取具体用法及详细介绍，例如:ls --help,本文适用于初学着的简单入门。

### 关于路径

` / 表示根目录，./表示当前目录,     ../ 表示上一层目录。`

在 Linux 中，文件系统的路径有两种，一种是相对路径，一种是绝对路径。

1. 相对路径：相对于当前目录，以当前目录为参考规定的其他文件的路径。其特征是路径前不加” **`/`** “，或者直接使用” **`./`** “表示当前目录。
2. 绝对路径：目录前面加” **/** “，从根目录开始的路径为绝对路径。

绝对路径很清晰明了，缺点就是太长。而相对路径虽然字符数不多，但是比较复杂，容易弄迷糊。至于到底使用哪一个，就见仁见智了。

### 命令 ls (list)

ls 命令用于在终端窗口打印指定目录下的所有文件夹及文件，并有许多可供选择的选项：

1. -l（小写的 L）：打印详细文件信息，包括大小，用户权限，所属用户组等。
2. -a ：用于显示目录中的隐藏文件夹或文件。
3. -h ：用于显示文件大小以 KB、MB、GB 等单位。

其用法为：`#ls [选项] [路径]` ，[ ]号内的内容可以省略，如路径省略，则表示当前目录(` ./` )。

它们可以组合使用，例如：`#ls -la /etc/apt`，或者`#ls -lah` （如目录省略则表示当前目录）。如图：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200404232653475.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTc0ODczNA==,size_16,color_FFFFFF,t_70)

### 命令 pwd (print working directory)

pwd 命令用于打印当前目录的绝对地址。如图：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200404232856275.png)

### 命令 cd （change directory）

这个命令表示进入到某个目录中去，在 Windows 中的 CMD 中也很常见，其用法为：

`cd 路径`，相对路径和绝对路径都可以，如图：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200404232940984.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200404232956833.png)
另外，可以直接使用 `cd ~ `进入当前用户目录，如图：

### 命令 mkdir （make directory）

此命令用于创建指定目录下的指定目录（也就是文件夹）。例如：

`#mkdir My`（表示当前目录，也可使用绝对目录）
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200404233520170.png)

意为在已存在当前目录下创建一个名为 My 的文件夹，但是不能创建**不存在目录**下的一个文件夹，例如：

`#mkdir MY/a/b/c/d`

**因为 My/ 目录下没有 a/ 目录，所以这样是错误的**。这时候就要使用 mkdir 的一个选项：`-p` 。此选项可以连续创建不同层级的目录文件夹：

`#mkdir -p My/a/b/c/d`
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200404233727464.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTc0ODczNA==,size_16,color_FFFFFF,t_70)

这样，就创建了一个 d 目录，放在/etc/a/b/c/目录下。

### 结语

加油！坚持就是胜利！
