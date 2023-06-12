---
title: "检查型异常和非检查型异常——Java"
date: 2020-05-07T18:01:07+08:00
description:
tags: [Java]
categories: Java
featured_image: "/images/notebook.png"
draft: true
comment: false
---

## 检查型异常和非检查型异常——Java

Java 语言规范将派生于 Error 类或 RuntimeExceprion 类的所有异常称为非检查型（unchecked）异常，所有其他的异常称为检查型（checked）异常。这是个很有用的术语。
Java 中的异常类型分布：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200507212051592.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTc0ODczNA==,size_16,color_FFFFFF,t_70)

但是，单单这样理解有些困难，我查了一些资料，用一些简单的语言来解释它们。

### 检查型异常

检查型异常，简单来说就是在现实中无法避免的，我们在设计程序时无法预知的异常抛出。例如：读取一个文件的内容。如果这个文件不存在或者程序没有读取权限时，就会抛出一个异常。我们必须要用`throws`声明它会出现的异常类型，或者用`try...catch`来捕获异常，并指明出现错误时要执行的操作。例如：

1. 试图超越文件末尾继续读取数据；
2. 试图打开一个不存在的文件；
3. 试图根据给定的字符串查找 Class 对象，而这个字符串表示的类并不存在。

这类检查型异常必须要在代码中声明出来，它是不可避免和预知的。如果没有声明，集成开发环境 IDE 将会报错！它会帮我们检查，故称 _检查型异常_。

这类异常我们必须要解决。

### 非检查型异常

非检查型异常，就是在代码实现阶段就可以预知和避免的一些异常，例如从 **RuntimeExcrption 类** 和 **Error 类** 中继承的那些非检查型异常，RuntimeExcrption 类包括：

1. 错误的强制类型转换；
2. 数组访问越界；
3. 访问 null 指针。

这些异常不需要在代码中生命，IDE 也不会报错指出。这些异常我们完全有能力去避免和预知，IED 不会帮我们检查这其中的错误！故称为 _非检查型异常_。

同时，我们也不需要声明 Java 的内部错误，即从 **Error 类** 继承的异常。任何程序代码都可能抛出那样的异常，而我们对此完全无法控制。

### 结语

这就是对在 Java 中，检查型异常和非检查型异常的简单浅显理解，希望对 Java 的初学者有所帮助。
