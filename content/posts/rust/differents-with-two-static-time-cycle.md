---
title: "Rust 中两种 static 生命周期标注的区别"
date: 2024-12-01T23:23:17+08:00
description: "本文介绍了 Rust 中的两种 static 生命周期标注： T: 'static 和 T: &'static, 它们是有本质区别的。"
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

那么 `&a_str` 指向一个字符串字面值，它一定在整个程序运行中存在，所以编译通过，它不在乎引用本身的作用域。

## 总结

通过上述例子可以看到:

1. `T: 'static` 在乎的是 T 类型本身的生命周期，也就是 T 类型本身的作用域;

2. `T: &'static` 在乎的是 T 类型指向的数据的作用域。

在一般代码实践中，应该避免使用 `T: &'static` ，因为这表明，即使 T 类型的作用域不是整个程序运行周期，编译器也会使其通过编译，就如第三个例子。

然而在遇到难以解决的生命周期的问题的时候，可以适当使用 `T: 'static` 使程序通过编译，使编译器理解我们的意思，不再阻拦我们。
