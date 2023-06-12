---
title: "[FAILED] Failed to Start Pkgfile Database Update in Manjaro"
date: 2021-07-29T20:52:56+08:00
description:
tags: [linux]
categories: Bugs解决记录
featured_image: "/images/notebook.png"
draft: false
comment: false
---

​## 问题描述

环境：Manjaro

在开机加载时出现上述错误。

## 解决方法

执行：

```
sudo pkgfile -u
```

重启即可。

参考链接：[https://forum.manjaro.org/t/failed-failed-to-start-pkgfile-database-update/31731/](https://forum.manjaro.org/t/failed-failed-to-start-pkgfile-database-update/31731/ "https://forum.manjaro.org/t/failed-failed-to-start-pkgfile-database-update/31731/")
