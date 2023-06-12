---
title: "博客园美化——添加Apalyer音乐播放器"
date: 2020-05-19T18:03:45+08:00
description:
tags: [博客]
categories: 博客
featured_image: "/images/notebook.png"
draft: false
comment: false
---

## 前言

这几天申请了博客园的博客，非常顺利便捷。审核大概还不到一个小时，效率是很高的了，赞一个！

之前折腾过 GitHub Page+hexo+next，对于我这种前端小白来说真实有点难度，不过最终还是弄了一个蛮漂亮的博客网站，见[https://chens.life](https://chens.life)，欢迎访问！奈何 🐕 百度对 GitHub 的收录是真的不好，csdn 的广告商业化让人作呕，就试了试博客园。

想给博客加个音乐播放器，还是用著名[Aplayer](https://github.com/MoePlayer/APlayer)，美观漂亮。可以参考它们的[官方中文文档](https://aplayer.js.org/#/zh-Hans/)，而我们要做的很简单！

## 引入 css 和 js

> 前提是需要申请 js 权限，大概一个小时就会通过

在页脚 HTML 代码中加入：

```html
<!-- 为博客底部添加音乐组件 -->
<div id="player" class="aplayer"></div>
<link
  href="https://files.cnblogs.com/files/shwee/APlayer.min_v1.10.1.css"
  rel="stylesheet"
/>
<script src="https://files.cnblogs.com/files/shwee/APlayer.min_v1.10.1.js"></script>

<script type="text/javascript">
  const ap = new APlayer({
    container: document.getElementById("player"),
    fixed: true,
    autoplay: true, //自动播放
    audio: [
      {
        name: "The Song Of Doremi",
        artist: "林澜叶",
        url: ".mp3",
        cover: ".ico",
      },
      {
        name: "阳光甚好，微风不噪",
        artist: "何石",
        url: ".mp3",
        cover: ".ico",
      },
    ],
  });
  ap.init();
</script>
```

填入歌曲 URL 和封面外链即可！可是如何获取外联呢，这里提供一种方法。

## 获取音乐和封面外链

> 这里以网易云为例

### 获取音乐外链

打开[http://music.xf1433.com/](http://music.xf1433.com/)，选择音乐地址，复制自己喜欢的音乐的地址，就可获取到外链。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200519112127782.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTc0ODczNA==,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200519112140292.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTc0ODczNA==,size_16,color_FFFFFF,t_70)

### 获取封面外链

在网易云歌曲页面，按 F12 之后打开调试窗口，点击那个最左上角的小按钮，
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200519112230483.png)
再点击封面图片，即可看到图片的外链，复制下来就行了！
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200519112238150.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTc0ODczNA==,size_16,color_FFFFFF,t_70)

## 最终效果如图

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200519112313557.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTc0ODczNA==,size_16,color_FFFFFF,t_70)如有更好的方法，欢迎交流。
