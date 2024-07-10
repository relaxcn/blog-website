---
title: "配置VSCode的Java开发环境"
date: 2020-08-21T18:07:58+08:00
description:
tags: [软件教程]
categories: 软件教程

draft: false
comment: false
---

## 前言

平台：Windows10
最近痴迷于 VS Code 的开发环境配置，原因就在于它的轻巧和免费，还能当一个非常棒的文本编辑器。如果之前你配置过 VS Code 并且失败了，那么**建议重新安装**，并彻底删除`C:\Users\Administrator\.vscode`和`C:\Users\Administrator\AppData\Roaming\Code`内的所有文件。

## 一键配置和安装

VS Code 官方文档中，提供了自动安装和配置 Java 开发环境的程序[Installer of Visual Studio Code for Java developers](https://aka.ms/vscode-java-installer-win)，[私有云备份](https://nas.chens.life/index.php/s/PmGLeQRW4D9m2LJ)，密码：`chens.life`。

打开之后，程序会自动检测 VS Code、Java JDK 和相关插件，并会自动进行下载和安装。

![](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xMS8yMDIwMDgxMTExNDQ1OC5wbmc?x-oss-process=image/format,png)

## 手动配置

如果不想使用自动配置，则可以手动配置。尤其是 JDK 下载缓慢，我们可以事先安装和配置好 JDK 开发环境，这样也可以指定 JDK 的版本。

### 配置 JDK 开发环境

从[Oracle 官网](https://www.oracle.com/java/technologies/javase-downloads.html)下载需要的 JDK 版本，记住安装的路径，方便之后配置系统环境变量。依次进入`控制面板\系统和安全\系统 > 高级系统设置> 环境变量`，新建`CLASSPATH`和`JAVA_HOME`，修改`Path`。

| 变量             | 值                                             |
| ---------------- | ---------------------------------------------- |
| JAVA_HOME        | C:\Program Files\Java\jdk-13.0.2（换成自己的） |
| CLASSPATH        | .;%JAVA_HOME%\lib;%JAVA_HOME%\lib\tool.jar     |
| 添加两条 Path 值 | %JAVA_HOME%\bin 和 %CLASSPATH%                 |

在 cmd 中输入`java -version`验证是否配置正确。

### 安装 VS Code 插件

1. [Language Support for Java(TM) by Red Hat](https://marketplace.visualstudio.com/items?itemName=redhat.java)
2. [Debugger for Java](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-debug)
3. [Java Test Runner](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-test)
4. [Maven for Java](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-maven)
5. [Java Dependency Viewer](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-dependency)

### 配置 VS Code

`Ctrl+Shift+P`跳出控制面板，输入命令**Java：Configure Java Runtime**，即可看到关于 JDK 的设置。一般必设置，除非需要多个 JDK。

![03](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xMS8yMDIwMDgxMTEyMTQwMC5wbmc?x-oss-process=image/format,png)

## 测试

新建文件夹，**右键在 Code 中打开**，新建`hello.java`文件，键入

```java
public class hello{
    public static void main(String[] args){
        System.out.println("hello world\n");
    }
}
```

点击`Run`即可运行 Java 程序。

> 注意：如果不是在文件中打开 VS Code，单独打开一个 java 文件可能会出错！！
>
> 必须在文件中打开 VS Code！

![01.gif](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xMS8wMS5naWY)

## 结尾

其实微软官方提供的一键安装工具就非常的好用，我们可以先把 VS Code、Java JDK 安装配置好之后，再运行安装工具。

### 参考文档

- https://code.visualstudio.com/docs/java/java-tutorial
