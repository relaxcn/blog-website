---
title: "vcpkg + cmake + vscode 配置教程"
date: 2023-01-27T15:58:36+08:00
description: 本文是使用  vcpkg 、cmake 、vscode 进行 C++ 开发的环境配置教程。
tags: [vcpkg, cmake, vscode]
categories: 软件教程
draft: false
comment : false
---

本文是使用 `vcpkg` 、`cmake` 、`vscode` 进行 C++ 开发的环境配置教程。

## 环境描述

1. Linux  Debin11 5.15.79.1-microsoft-standard-WSL2
2. git version 2.30.2
3. curl 7.74.0
4. tar (GNU tar) 1.34
5. cmake version 3.18.4
6. vcpkg package management program version 2023-01-24
7. gcc (Debian 10.2.1-6) 10.2.1 20210110

## 安装 vcpkg

首先安装上述环境工具：

```bash
sudo apt install gcc g++ gdb git curl tar make cmake
```

从 Github 仓库中克隆 `vcpkg` 的文件：

```bash
git clone https://github.com/Microsoft/vcpkg.git
```

运行初始化脚本：

```bash
./vcpkg/bootstrap-vcpkg.sh
```

> 注意：这一步将会从 Github 下载文件，使用魔法会更加方便，只需设置一下代理即可：
>
> ```bash
> export http_proxy=ip:port
> export https_proxy=ip:port
> ```

成功之后，在 `vcpkg` 文件夹内将会有一个二进制可执行文件 `vcpkg`，此时即可使用 `vcpkg` 。

## 安装所需要的库

使用命令 `search` 和 `install` 可以搜索和安装库。例如我将要安装 `oatpp` Web 框架：

```bash
./vcpkg/vcpkg search oatpp
./vcpkg/vcpkg install oatpp[*]:x64-linux
```

`x64-linux` 代表安装目标的机器类型。

> 这一步会从 GitHub 中下载 oatpp 的源代码，所以需要魔法科技。

成功之后会提醒 oatpp 提供了 CMake 目标。

![image-20230127152746973](image-20230127152746973.png)

## 配置 vscode

新建一个项目文件夹，使用 vscode 打开该文件夹。

```bash
mkdir oatpp-test
cd oatpp-test
code .
```

 安装 vscode 插件：C/C++ Extension Pack、CMake ，之后重启 vscode。

`Ctrl + Shift + p` 输入 `settings json` 开发工作区设置（JSON）。填入：

```json
{
    "cmake.configureSettings": {
      "CMAKE_TOOLCHAIN_FILE": "<path to vcpkg>/scripts/buildsystems/vcpkg.cmake",
      "VCPKG_TARGET_TRIPLET": "x64-linux"
    }
}
```

>  注意：将 `<path to vspkg>` 替换为你的 `vcpkg` 路径！！！

创建 `CMakeLists.txt` 文件，填入：

```cmake
cmake_minimum_required(VERSION 3.18)
project(oatpp-test)
add_executable(oatpp-test main.cpp)
set(CMAKE_CXX_STANDARD 17)

find_package(oatpp CONFIG REQUIRED)

target_link_libraries(oatpp-test PRIVATE oatpp::oatpp oatpp::oatpp-test)
```

创建 `main.cpp` 文件，填入：

```c++
#include "oatpp/network/Server.hpp"
#include "oatpp/network/tcp/server/ConnectionProvider.hpp"
#include "oatpp/web/server/HttpConnectionHandler.hpp"

class HelloHandler : public oatpp::web::server::HttpRequestHandler {
public:
  std::shared_ptr<OutgoingResponse>
  handle(const std::shared_ptr<IncomingRequest> &request) override {
    OATPP_LOGI("HelloHandler", "this is a request!");
    auto i = request->getHeaders().get("User-Agent")->c_str();
    OATPP_LOGI("HelloHandler", "User-Agent : %s", i);
    return ResponseFactory::createResponse(Status::CODE_200, "Hello World");
  }
};

void run() {

  /* Create Router for HTTP requests routing */
  auto router = oatpp::web::server::HttpRouter::createShared();

  router->route("GET", "/hello", std::make_shared<HelloHandler>());
  /* Create HTTP connection handler with router */
  auto connectionHandler =
      oatpp::web::server::HttpConnectionHandler::createShared(router);

  /* Create TCP connection provider */
  auto connectionProvider =
      oatpp::network::tcp::server::ConnectionProvider::createShared(
          {"localhost", 8000, oatpp::network::Address::IP_4});

  /* Create server which takes provided TCP connections and passes them to HTTP
   * connection handler */
  oatpp::network::Server server(connectionProvider, connectionHandler);

  /* Print info about server port */
  OATPP_LOGI("MyApp", "Server running on port %s",
             connectionProvider->getProperty("port").getData());
  /* Run server */
  server.run();
}

int main() {

  /* Init oatpp Environment */
  oatpp::base::Environment::init();

  /* Run App */
  run();

  /* Destroy oatpp Environment */
  oatpp::base::Environment::destroy();

  return 0;
}
```

此代码参考 oatpp 官方文档：[https://oatpp.io/docs/start/step-by-step/#add-request-handler](https://oatpp.io/docs/start/step-by-step/#add-request-handler)

`Ctrl + Shift + p` 输入 `cmake configure` ，选择 **CMake：配置**。这将会配置该 CMake 工程项目。

完成之后即可发现 `main.cpp` 中的代码已经不报错了，在 vscode 底部状态栏也出现了 CMake 工具。

![image-20230127155145068](image-20230127155145068.png)

点击 `Build` 之后再点击最右边的运行箭头，即可编译运行该测试程序。

![image-20230127155553208](image-20230127155553208.png)

访问 [http://localhost:8000/hello](http://localhost:8000/hello)，即可看到字符 `Hello World`。终端中可以看到访问端的 `User-Agent`。

![image-20230127155513464](image-20230127155513464.png)