---
title: "如何搭建自己的本地服务器，Web服务器"
date: 2020-08-21T18:13:23+08:00
description:
tags: [linux]
categories: Linux笔记

draft: false
comment: false
---

先上图！大致思路就是如此。

![思维导图](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xMy8yMDIwMDgxMzEyNTQwMy5wbmc?x-oss-process=image/format,png)

## 前言

暑假因为疫情在家无事可做，便白嫖了阿里云大半年的虚拟主机。虽然它只有 1 核 2G，1M 的带宽，但也给了我一个实践的机会，让我有机会了解学习 apache、php、js、Linux 等等······

显然！我们已经不再满足于一百多 KB 的带宽，缓慢的 cpu 速度和狭小的 50G 系统盘了！自建一个性能强大，带宽 300M（这取决于自己的宽带），硬盘容量随意增加的本地服务器势在必得！终于，功夫不负有心人，我在折腾了一个通宵之后就肝了出来，于此将我的经验分享出来，希望能帮助到大家。

### 本地服务器的好处

毋庸置疑，那就是可操控性、可拓展性和极致性价比。相比于各类云服务厂商（阿里云、腾讯云等）动辄一年好几千的“高端”配置，我这个穷人还是老实折腾我的本地服务器吧（不争气的眼泪流了下来，呜呜呜~~）

### 本地服务器的弊端

当然了，本地服务器毕竟不是专业的服务器。况且国家对于互联网的管控还是很严格的，所以这就导致了本地服务器的一些弊端。例如，

1. 本地服务器不够稳定，容易受到**停电**、机器故障、网络故障等各类不可控因素的影响；
2. 我们所部署的本地服务器并不是专业的服务器，本身的并发能力不强，所以不适合用户数量特别巨大的人；
3. 电信运营商对于家用宽带做了诸多限制，**封禁了 80，22 等常用端口**。虽然能够通过端口映射或修改端口来解决，但还是不太美观。幸运的是，我这里的 443 端口没有被封，不要太开心~~

## 前提准备

### 公网 IP

这是至关重要的一项。打开[http://ip.3322.net](http://ip.3322.net)，查看返回的 IP 地址与光猫普通用户后台的 IP 地址是否相同，如果相同，则当前 IP 为公网 IP。如果不相同，则需要向电信运营商申请公网 IP。打给自己的运营商客服，告诉她家里要装 NAS 或者监控，申请公网 IP。

### 光猫改为桥接

一般我们安装的光猫都自带路由器和拨号功能，但是不具有[端口映射](https://baike.baidu.com/item/%E7%AB%AF%E5%8F%A3%E6%98%A0%E5%B0%84/98247?fr=aladdin)功能，无法将本地局域网内的服务器映射到公网上面。所以我们需要让路由器来进行拨号任务，而光猫单独进行光电信号转换。

将光猫改为桥接需要用超级管理员登录光猫后台，一般为`192.168.1.1/admin`，**不同的光猫情况不同，去百度搜搜自己的光猫型号**。另外超级管理员密码要找装机师傅要，他们一般以各种理由推辞，难搞哦~。如果搞不定就去万能的淘宝吧！（别怪我没提示哦~）我自己也是找的淘宝。。。

### 一台旧电脑

我是用的是一台老式的 Dell 灵越笔记本，4G RAM，i5 八代 U，500G HDD。这对于个人博客服务器来说是绰绰有余了，足以抵得上阿里云好几千的服务器了。

### 一个域名

#### 为什么需要域名

在这里我说一下为什么我们还需要一个域名呢？直接适用 IP 地址访问不就好了？反正是自己使用的。

因为我们向电信运营商申请的公网 IP 是动态的，也就是说隔一段时间就会改变，不是固定的 IP 地址。那么能不能申请固定的 IP 地址呢？答案是可以，但是非常贵，面对大型企业的。我这种穷学生就算了吧。

所以，在有个一个域名之后就可以使用[动态域名解析](https://baike.baidu.com/item/%E5%8A%A8%E6%80%81%E5%9F%9F%E5%90%8D%E8%A7%A3%E6%9E%90/98200?fr=aladdin)，将域名解析到变化的 IP 地址上，这样不论 IP 地址如何变化，我们总是能够访问得到本地的服务器。况且，如果是想做个人博客，只有域名才能够被百度和谷歌收录，才有机会被别人看见。

#### 申请域名

注册域名可以去阿里云万网，也可以去腾讯云，找个合适的域名即可。直接买，即可直接开始使用。

#### 备案

不过我建议，有空的时候去备个案，也不麻烦，时间也不长。况且这样能为以后免去很多麻烦。

各大云服务厂商都有提供代备案服务，直接按照流程走即可。都是免费的，不收取任何费用。

## 中间部署

### 安装 CentOS 7 操作系统

市面上有很多可供选择的服务器系统，Linux 是毋庸置疑必选的——由于它的稳定性。至于为何选 CentOS 7，~~当然是因为我对它熟悉啊~~~~ 咳咳，那当然是因为 CentOS 本身就很适合做 web 服务器，况且用户多，问题容易解决。

具体安装步骤见另一篇文章[https://chens.life/how-to-install-CentOS.html](https://blog.chens.life/how-to-install-CentOS.html)。

在这里， 我们需要选择安装 **基本的网页服务器**，我们不需要图形界面，这将会更加省电和高效。

![02](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xNS8yMDIwMDgxNTEzNDkwMy5wbmc?x-oss-process=image/format,png)

#### 配置网卡驱动

刚安装好的 **基本网页服务器**可能无法连接外网，在 Linux 终端上使用`ping baidu.com`测试一下，如果不通，则需要配置一下相关文件。参考这篇文章https://www.php.cn/centos/445305.html。这里是有线网络的配置方法，至于无线网卡如何驱动，请自行百度Google。

#### 更换国内 yum 源

国内速度太慢，目前国内的大公司有许多开源镜像站，例如阿里云、网易、清华大学、华为等等，这里使用阿里云的 yum 源。

参考官方文档[https://developer.aliyun.com/mirror/centos?spm=a2c6h.13651102.0.0.3e221b11bXrW8A](https://developer.aliyun.com/mirror/centos?spm=a2c6h.13651102.0.0.3e221b11bXrW8A)，依次执行

```java
su
输入root密码
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
curl -o /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-7.repo
yum clean all
yum makecache
```

#### 安装 ssh

```
sudo yum install oppenssh -y
```

启动 ssh 的服务：

```
systemctl start sshd.service
```

设置开机自动启动 ssh 服务

```
systemctl enable sshd.service
```

配置文件在`/etc/ssh/sshd_config`，一般不用修改。

#### 安装 ftp

```
sudo yum install ftp -y
```

ssh 和 ftp 服务都是 22 端口的，我们目前在内网进行部署，所以不必更改端口，后面会进行端口映射，已解决运营商封禁 22 端口的问题。

至此，我们就可以使用 shell 和 ftp 软件进行远程连接了，推荐 xftp 和 xshell，学生和家庭用户免费，在这里申请，[https://www.netsarang.com/zh/free-for-home-school/](https://www.netsarang.com/zh/free-for-home-school/)。也可使用免费版的 FinalShell，[私有云](https://nas.chens.life/index.php/s/Zbd8ELmPstMrMot)，密码：`chens.life`。

### 安装宝塔面板

宝塔面板可以更简单明了的进行网站的部署和服务器的监控，非常值得推荐。参考官方网站[https://www.bt.cn/bbs/thread-19376-1-1.html](https://www.bt.cn/bbs/thread-19376-1-1.html)

#### 一键安装命令

```
sudo yum install -y wget && wget -O install.sh http://download.bt.cn/install/install_6.0.sh && sh install.sh
```

耐心等待其安装完成，之后会得到一个访问地址和账户密码，我们先使用内网访问地址进行操作。

![03](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xOC8yMDIwMDgxODEzMzAzMS5wbmc?x-oss-process=image/format,png)

#### 第一次配置

使用内网登录面板，同意使用条款后进入界面。选择 LNMP 方案安装 web 环境，极速安装。注意！php 版本选择 7.2 版本，以后许多开源好用的软件必须高版本 php 的支持，例如 nextcloud。

![04](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xOC8yMDIwMDgxODEzMzYyNC5wbmc?x-oss-process=image/format,png)

耐心等待安装完成。

#### 修改安全设置

安装完成之后会提醒你

> 当前面板使用的是默认端口[8888]，有安全隐患，请到面板设置中修改面板端口!

所以我们到 `面板设置`中修改**面板端口**、**安全入口**、**面板用户**、**面板密码**，按照自己的需求修改。，例如我将端口修改为`5656`，安全入口修改为`blogtest`。这样设置之后就避免了面板被暴力破解的几率，更加的安全。

![06](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xOC8yMDIwMDgxODEzNTAwOS5wbmc?x-oss-process=image/format,png)

#### 修改默认建站目录

如果`/`目录容量太小，而其他目录空间较大，就可以将**默认建站目录**修改为自己想要的位置。在`面板设置 -> 默认建站目录`修改。本例中只有`/`目录，所以不再演示。

### 配置路由器端口映射

到了这一步就基本完成了服务器环境的搭建，最重要的一步就是如何让外网能够访问自己的服务器，并打开宝塔面板。

首先我们登录自己的路由器控制台，绑定自己服务器的内网 IP 地址，这样防止了端口映射因为服务器内网 IP 地址变动而出错。之后，我们需要进入**端口映射**这一高级功能，填上要映射的外网端口和内网 IP 和端口，即可使用自己的公网 IP 加端口访问到宝塔面板，证明端口映射成功。例如这样

![07](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xOC8yMDIwMDgxODE0MDcxMi5wbmc?x-oss-process=image/format,png)

![08](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xOC8yMDIwMDgxODE0MDcyMy5wbmc?x-oss-process=image/format,png)

宝塔面板的外部和内部端口可以相同，这主要看自己的电信运营商有没有封禁使用的端口。例如要想访问 80 端口的 web 服务器，我们只能把 99（举个例）映射到内网 IP 的 80 端口，这样就实现了外网访问。就是有点难看罢了。

不过，如果你所在的电信运营商没有封禁 443 端口，就可以使用 https 加密来不加端口访问自己的网页了。这需要在端口映射中添加转发规则.

![09](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xOC8yMDIwMDgxODE0MTEwMS5wbmc?x-oss-process=image/format,png)

而你的网址也要申请 ssl 证书，才能开启 https 加密。我们后面会讲到，直接使用宝塔的一键部署功能。

### dns 解析

登录自己的云服务商的 dns 解析管理后台，把域名解析到自己当前的公网 IP。即可通过**域名加端口**的方式访问自己的网站。

## 后期完善

#### 动态域名解析

关于动态域名解析，虽然有花生壳等服务商，但都是收钱的，况且自定义域名也是收费的。我目前再用 GitHub 上的一个开源项目https://github.com/NewFuture/DDNS，根据相关说明配置好以后，让宝塔计划任务每10分钟执行一次，即可实现动态域名解析。

![10](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xOC8yMDIwMDgxODE0MzgwMi5wbmc?x-oss-process=image/format,png)

### ssl 证书部署

在宝塔面板网站设置的 ssl 中，申请 Let's Encrype 证书，选择阿里云 ddns 验证（根据自己的云服务商）。宝塔 ssl 证书在自建服务器的条件下不可用。

![11](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcuY2hlbnMubGlmZS9pbWFnZXMvMjAyMC8wOC8xOC8yMDIwMDgxODE0NDIxMS5wbmc?x-oss-process=image/format,png)

### 笔记本禁止盒盖休眠

`vim /etc/systemd/logind.conf`，将`HandleLidSwitch:`后面改为`ignore`，将前面的`#`去掉。保存退出。然后执行`systemctl restart systemd-logind`即可生效。

## 常见错误

### https 无法访问

只设置了 80 端口的映射，没有设置 443 端口的映射。或者设置了，但是没有点击 **立即生效**。

### CentOS 无法 ping 通，无法连接外网

参考这篇文章即可解决[https://blog.csdn.net/sinat_32079337/article/details/70238107](https://blog.csdn.net/sinat_32079337/article/details/70238107)

## 结尾

这就是我自建 web 服务器的大致过程了，因为使用了虚拟机模拟的一部分内容，所以可能不是 100%的信息一致。但是，道理都是一样的，我们也要合理的利用百度和 Google。希望这会对你有所帮助。

欢迎访问我的个人博客[https://chens.life](https://chens.life)。
