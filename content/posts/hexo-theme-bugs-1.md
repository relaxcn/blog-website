---
title: "关于Hexo,Next主题的‘下一页’、‘上一页’按钮错误的解决方法"
date: 2020-05-10T18:02:05+08:00
description:
tags: [Hexo]
categories: Hexo

draft: false
comment: false
---

## 关于 Next 主题的‘下一页’、‘上一页’按钮错误显示为 html 代码的解决方法

我在建立自己的博客过程中遇到了页面‘下一页‘和’上一页‘按钮显示为 html 代码`<i class="fa fa-angle-right"></i>`的问题，虽然可以点击不影响使用，但是这确实影响美观。
![](https://imgconvert.csdnimg.cn/aHR0cDovL2Rucy5jaGVucy5saWZlLyVFNiU4OCVBQSVFNSVCMSU4RjIwMjAtMDUtMTAlRTQlQjglOEIlRTUlOEQlODgxMi41OS4yNy5wbmc?x-oss-process=image/format,png)
本文提供一种解决方法，如下：

打开`next > layout > _partials > pagination.swig` ，将错误的 html 代码改为‘下一页’和‘上一页’即可！如图：

![](https://imgconvert.csdnimg.cn/aHR0cDovL2Rucy5jaGVucy5saWZlLyVFNiU4OCVBQSVFNSVCMSU4RjIwMjAtMDUtMTAlRTQlQjglOEIlRTUlOEQlODgxLjI5LjQ0LnBuZw?x-oss-process=image/format,png)

结果如下，恢复正常：

![](https://imgconvert.csdnimg.cn/aHR0cDovL2Rucy5jaGVucy5saWZlLzMucG5n?x-oss-process=image/format,png)
