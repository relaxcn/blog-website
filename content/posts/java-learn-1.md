---
title: "Java中访问控制修饰符的详解和示例——Java学习"
date: 2020-04-02T17:39:18+08:00
description:
tags: [Java]
categories: Java学习
featured_image: "/images/notebook.png"
draft: false
comment: false
---

### 简述

在 Java 中共有四个：

1.  public —— 对外部完全可见
2.  protected —— 对本包和所有子类可见
3.  默认（不需要修饰符）—— 对本包可见
4.  private —— 仅对本类可见

从上到下，public 的开放程度最高。

- | 对外完全可见       | 对本包和所有子类可见 | 仅对本包可见  | 仅对本类可见         |
  | ------------------ | -------------------- | ------------- | -------------------- | ----------- |
  | **访问控制修饰符** | **Public**           | **Protected** | **默认（无修饰符）** | **Private** |
  | 同一包中的其它类   | ✓                    | ✓             | ✓                    | ✗           |
  | 同一包中的子类     | ✓                    | ✓             | ✓                    | ✗           |
  | 不同包中的其它类   | ✓                    | ✗             | ✗                    | ✗           |
  | 不同包中的子类     | ✓                    | ✓             | ✗                    | ✗           |

简言之就是，public 全开放，protected 对本包和子类（不论是不是在本包中）开放，默认的只对本包开放（不论是不是子类），private 仅对本类开放（只有定义它的类内部才能够使用，非常不开放）。
建议在定义每个类的私有字段，也就是成员变量时使用 private 修饰符，这样才能够确保类的封装性。

### 实例演示

定义两个包：A 包和 B 包。
A 包中有类：aFather 、aClass、aSon；B 包中有类：bClass、bSon
定义类：aSon、bSon 是 aFather 的子类。具体如下
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200402195005763.PNG)

#### 包 A

##### aFather.java

定义了一个父类 aFather，和各实例字段，如下：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200402203022941.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTc0ODczNA==,size_16,color_FFFFFF,t_70)

##### aClass.java

aClass 为 A 包中的一个普通类。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200402203035709.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTc0ODczNA==,size_16,color_FFFFFF,t_70)
显然在同一包中，除了**~~private~~** ，都可以正常访问父类的**Public、Protected 和默认定义**的实例字段。

##### aSon.java

aSon 为 A 包（同一包）中的 aFather 类的子类
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200402203048371.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTc0ODczNA==,size_16,color_FFFFFF,t_70)
同样，同一包中的子类可以正常访问父类的**Public、Protected、默认定义** 的实例字段。

#### 包 B

##### bClass.java

bClass 为 B 包中的一个普通类。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200402203058633.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTc0ODczNA==,size_16,color_FFFFFF,t_70)
可以看出，非 aFather 子类的类：bClass 只能访问 A 包中类的 **Public** 的实例字段。

##### bSon.java

bSon 为 B 包中的，aFather 类（A 包中）的子类。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200402203108703.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTc0ODczNA==,size_16,color_FFFFFF,t_70)
而 B 包中的 bSon 类 是 A 包中 aFather 类的子类，可以访问父类（超类）中由**Public、Protected**定义的实例字段，其他的无法访问。

由此看出，开头所说：

1.  public —— 对外部完全可见
2.  protected —— 对本包和所有子类可见
3.  默认（不需要修饰符）—— 对本包可见
4.  private —— 仅对本类可见

便更易于理解了！
