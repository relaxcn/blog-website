---
title: "Differents With Two Static Time Cycle"
date: 2024-12-01T23:23:17+08:00
description: Rust 中有两种 static 生命周期标注
tags: [rust-time-cycle]
categories: Rust
draft: false
comment : false
---

## Rust 中的 static 生命周期标注

Rust 中有的 static 生命周期意味着该类型的生命周期同整个程序的生命周期相同，意味着编译器会认为它一直是有效的。

在 Rust 中，有两种使用 static 生命周期标注的方法：

1. 一种是类型本身的生命周期为 static: `T: 'static`.
2. 另一种是，该类型指向的数据的生命周期为 static: `T: &'static`.

它们之间是有本质区别的。

### T: 'static

它表示规定 T 类型本身的生命周期是是 static 的。

```rust
use std::fmt::Display;

fn main() {
    static_bound("a static str"); // OK
}

// 'static 要求 T 类型的可以在 'static 生命周期内使用
fn static_bound<T: Display + 'static>(t: T) {
  println!("{}", t);
}
```

这是 OK 的，因为 static_bound 的参数要求生命周期必须为 static,而字符串字面值的生命周期正好符合。

但是下面的写法是错误的：

```rust
use std::fmt::Display;

fn main() {
    {
        let a_str = "a string".to_string();
        // 通过引用传递，生命周期依赖于 a_str 的作用域
        // 然而 a_str 的作用域不是整个程序(static)
        static_bound(&a_str); // OK
    }
    
}

// 'static 要求 T 类型的可以在 'static 生命周期内使用
fn static_bound<T: Display + 'static>(t: T) {
  println!("{}", t);
}
```

`a_str` 的生命周期不是 static，而 `static_bound` 要求 T 类型的生命周期必须为 static，所以编译报错，提示 `a_str` 存活的不够长。

### T: '&static

我们将 `static_bound` 的参数列表改一下 `(t: &T)`，表示T的引用的内容的生命周期是 static,此时编译通过。

```rust
use std::fmt::Display;

fn main() {
    {
        let a_str = "a string".to_string();
        // 通过引用传递，生命周期依赖于 a_str 的作用域
        // 然后 a_str 的作用域不是整个程序(static)
        static_bound(&a_str); // OK
    }
    
}

// 'static 要求 T 类型的可以在 'static 生命周期内使用
fn static_bound<T: Display + 'static>(t: &T) {
  println!("{}", t);
}
```

这是因为 `&'static` 不管类型本身的生命周期，它只在乎引用所指向的内存中的数据是否在整个程序运行中存在。

那么 `&s_str` 指向一个字符串字面值，它一定在整个程序运行中存在，所以编译通过，它不在乎引用本身的作用域。