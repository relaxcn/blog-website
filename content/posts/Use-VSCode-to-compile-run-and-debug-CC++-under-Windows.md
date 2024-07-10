---
title: "Windows下使用VS Code 编译、运行和调试C/C++"
date: 2020-08-21T18:10:26+08:00
description:
tags: [软件教程]
categories: 软件教程

draft: false
comment: false
---

## 编译运行设置

### 前期准备

#### 1、安装 VS Code

在[VS Code](https://code.visualstudio.com/Download)官网下载最新版本安装包，注意 **User Installer** 和 **System Installer** 的区别。一般来说，如果使用 Administration 账户登录的就下载 System Installer 版本的，其他个人账户的下载 User Installer 版本。

![01](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xMS8wMWQyNzU2NWJhZmRjZjU5MzIucG5n?x-oss-process=image/format,png)

安装时，勾选所有的选项。

![image-20200811023756142](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xMS9pbWFnZS0yMDIwMDgxMTAyMzc1NjE0Mi5wbmc?x-oss-process=image/format,png)

#### 2、安装 MinGW

这是必要的 c 语言编译器组件包，下载最新版本[Mingw-w64](https://sourceforge.net/projects/mingw-w64/files/Toolchains targetting Win32/Personal Builds/mingw-builds/installer/mingw-w64-install.exe/download)，由于国内速度慢，可以直接下载离线版本 [Mingw-w64 私有云备份](https://nas.chens.life/index.php/s/nWnktjmX4P3sbay)，密码：`chens.life`。解压到合适的位置之后，需要配置系统变量中 Path 的值，将`<解压路径>\bin`添加进去，例如我的是`C:\mingw64\bin`。

![02](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xMS8wMi5wbmc?x-oss-process=image/format,png)

最后打开 cmd 验证一下是否安装成功，输入`gcc --version`，看是否有版本信息。

#### 3、安装必要插件

在 vscode 中按快捷键`Ctrl+Shift+X`，依次搜索安装如下图的插件。

![03](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xMS8wMy5wbmc?x-oss-process=image/format,png)

### 配置

新建文件夹，例如`hello`，打开文件夹，右键，选择 **通过 Code 打开**。

按快捷键`Ctrl+Shift+P`，输入`c/c++`，选择第一个（UI）图形界面配置。

![image-20200811023234080](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xMS9pbWFnZS0yMDIwMDgxMTAyMzIzNDA4MC5wbmc?x-oss-process=image/format,png)

配置编译器路径，选择刚才解压的路径下的**gcc.exe**，选择 InterlliSense 模式为 **gcc-64**。

![04](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xMS8wNC5wbmc?x-oss-process=image/format,png)

### 测试

新建`hello.c`文件，

![05](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xMS8wNS5wbmc?x-oss-process=image/format,png)

输入

```c
#include <stdio.h>
int main()
{
    printf("hello world\n");
    return 0;
}
```

`Ctrl+S`保存后，快捷键`Ctrl+Alt+N`运行，或者点击右上方小开始按钮。![06](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xMS8wNi5wbmc?x-oss-process=image/format,png)

运行成功。

### 解决一些问题

### 无法向终端输入内容

包含标准输入函数的程序，例如：

```c
#include <stdio.h>
//打印用户输入的字符串
int main()
{
    char s[100];
    char a;
    int i;
    while(a != EOF){
        for (i = 0; (a = getchar()) != '\n' && i < 100 && a != EOF; i++){
            s[i] = a;
        }
        if (a != EOF)
        {
            printf("%s\n", s);
        }

    }
    printf("END\n");
    return 0;
}
```

此时，我们需要改为在命令终端中运行程序。`Ctrl+,`打开设置，搜索 **run in Terminal**，勾选![image-20200811031406638](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xMS9pbWFnZS0yMDIwMDgxMTAzMTQwNjYzOC5wbmc?x-oss-process=image/format,png)

## 调试

一般来说，此时的调试是正常的。如果报错，则需要修改 launch.json 文件，即修改`"miDebuggerPath": <gdb.exe的路径>`，我的是`C:\\mingw64\\bin\\gdb.exe`，这里需使用转义`\\`。

![08](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xMS8wOC5wbmc?x-oss-process=image/format,png)

## 结语

觉得其他文章都写得太过于繁琐，如果按照我的方法应该会简单很多。

参考文档：

- https://code.visualstudio.com/docs/cpp/config-mingw#_prerequisites
- https://zhuanlan.zhihu.com/p/77645306
