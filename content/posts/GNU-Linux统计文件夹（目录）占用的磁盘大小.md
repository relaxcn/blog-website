---
title: "GNU Linux统计文件夹（目录）占用的磁盘大小"
date: 2021-02-09T20:18:35+08:00
description:
tags: [linux]
categories: Linux笔记
featured_image: "/images/notebook.png"
draft: false
comment: false
---

在 Linux 中使用 `ls`时，显示的文件夹大小始终为 4kb。这是因为在 Linux 中目录也是一个文件，里面存储着特有的数据结构，所以 `ls` 显示的就是这个目录文件的大小，并不是这个目录中所有文件的大小的总和。

## 命令

使用 `du` 命令就可以统计一个目录下所有目录所占用的真正的磁盘大小。

```
du [options] [directorys or files]
```

## 选项说明

- -a：显示所有的子目录和**子文件**的磁盘总用量。
- -h：使用友好的单位显示大小，如 KB、MB、G 等。
- -s：不显示子目录的信息，只显示当前查询的目录的磁盘总用量。
- 不加选项时：显示所有**子目录**的磁盘使用量。相比于 `-a` 少了子文件的信息。

## 例如

### 不加选项时

![image-20210209155354669](https://img-blog.csdnimg.cn/img_convert/d440d534f12b83e35f6f1a148afebc60.png)

![image-20210209155418798](https://img-blog.csdnimg.cn/img_convert/5ab4b51d825ff7aeb3ce64f0a6ad1c75.png)

### 使用-a

![image-20210209155603894](https://img-blog.csdnimg.cn/img_convert/e72cec3c9578b97abbb1090ca9ec7007.png)

包括了子文件。

### 使用-s

![image-20210209155650693](https://img-blog.csdnimg.cn/img_convert/55ae6faa75fb1c9a78607f437798fd19.png)
