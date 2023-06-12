---
title: "super与this的区别，更进一步的区别！——Java学习"
date: 2020-04-03T17:53:19+08:00
description:
tags: [Java]
categories: xv6-Java学习
featured_image: "/images/notebook.png"
draft: false
comment: false
---

## this 与 super 的含义

在 Java 中，this 有两层含义：

1. 指示隐式参数的引用（就是当前对象的引用）
2. 调用该类的其他构造器

而 super 也有两层含义：

1. 调用超类的方法
2. 调用超类的构造器

---

## 前言

在写这篇文章之前，我也查阅了其他博主关于 super 与 this 的区别的文章，他们都讲的很对，但是没有说到我想知道的重点。例如[cheneypku](https://me.csdn.net/zuoyang1990)的这篇文章 [Java 中 this 与 super 的区别](https://blog.csdn.net/zuoyang1990/article/details/53471494) 所述:

> 它们的区别:
> 1、super()主要是对父类构造函数的调用，this()是对重载构造函数的调用
> 2、super()主要是在继承了父类的子类的构造函数中使用，是在不同类中的使用；this()主要是在同一类的不同构造函数中的使用

但是，它们还有一点不同，那就是：

**super 不是一个对象的引用，因此不能够将 super 赋给另一个对象变量，他只是一个指示编译器调用超类(或父类)方法的特殊关键字。**

## 例证

### this

可以把 this 赋值给对象类型的对象变量，进而调用类中的数据字段。

```java
public class Students{
    private String name;
    private String otherName;
    private int age;

    Students S = this;    //编译通过

    public Students(String name, String otherName, int age){
        S(otherName); //出现错误！
        //or
        this(otherName);//编译通过！所以在调用其它构造器时，还是只能使用this()！
        S.age = age;  //可以正常引用Students类中的数据字段
    }
    public Students(String OtherName){
        S.otherName = OtherName;
    }

}
```

这说明，this 实际上是当前对象的一个引用，可以被赋值给相应的对象变量。**但是，当需要调用类中的其他构造器时，还是只能够使用 this()语句！**

### super

```java
class Person{
    private String name;
    public Person(String name){ //超类的构造函数
        this.name = name;
    }
    public String getName(){ //定义一个方法
        return name;
    }
}
public class Students extends Person{
    private String name;
    private int age;

    Person P = super;//已经出现了编译错误！！
    public Students(String name, int age){
        P(name);//编译错误！
        P.getName();//错误！！也不能调用超类的方法！
        this.age = age;
    }
}
```

所以，super 不能够赋给一个对应的对象变量，它不是一个对象的引用！

## 总结

它们的相同点是：调用构造器的语句只能够作为另一个构造器的**第一条**语句出现，这也是它们不能够出现在同一个构造器内的原因。

**而 this 的本质是一个对象的引用，super 只是一个指示编译器调用超类方法的特殊关键字，但在调用本类中的其他构造器时，还是只能够使用 this()语句。**

虽然这个点很小，但是希望能够帮助各位更加深刻的理解 this 和 super 的区别！不正之处，还希望读者不吝赐教！
