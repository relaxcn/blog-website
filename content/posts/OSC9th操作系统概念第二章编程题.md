---
title: "OSC9th操作系统概念第二章编程题"
date: 2021-03-15T20:22:31+08:00
description:
tags: [linux, 读书笔记]
categories: 读书笔记

draft: false
comment: false
---

## 题目描述

2.3 节描述了一个程序，以将一个文件内容复制到另一个目标文件。这个程序首先提示用户输入源文件名和目标文件名。利用 windows 或 POSIX 的 API，编写这个程序。确保包括所有必要的错误检查以及源文件是否存在。

## 程序

```
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>

int main(void)
{
    char sourceName[100];
    char objName[100];
    int fd1, fd2;
    printf("请输入源文件的名字:");
    scanf("%s", sourceName);
    /*读文件*/
    fd1 = open(sourceName, O_RDONLY);
    /*错误时返回-1*/
    if (fd1 == -1){
        /*print a system error message*/
        perror(sourceName);
        return EXIT_FAILURE;
    }

    printf("请输入目标文件名:");
    scanf("%s", objName);
    char buf[128];
    /*写文件
      O_WRONLY 写入
      O_CREAT 如果不存在则创建改文件
    */
    fd2 = open(objName, O_WRONLY|O_CREAT);

    /*read系统调用，正常情况下返回读取的字符位数，错误时返回-1, 读取到文件结尾时返回0*/
    while (read(fd1, buf, 1) != 0){
        write(fd2, buf, 1);
    }
    close(fd1);
    close(fd2);
    return 0;
}
```

## 系统调用

本题使用了多个系统调用

1. open [open(2) - Linux manual page](https://man7.org/linux/man-pages/man2/open.2.html "open(2) - Linux manual page")
2. read [read(2) - Linux manual page](https://man7.org/linux/man-pages/man2/read.2.html "read(2) - Linux manual page")
3. write [https://chi.jinzhao.wiki/wiki/%E5%86%99%E5%85%A5](https://chi.jinzhao.wiki/wiki/%E5%86%99%E5%85%A5 "https://chi.jinzhao.wiki/wiki/%E5%86%99%E5%85%A5")
4. close
