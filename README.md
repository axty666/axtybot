## **axtybot**

A MARYT / VANILO PLAYER BOT

运行于MARYT / VANILO服务器群内的玩家机器人，使用nonebot+gocqhttp搭建

------

### **快速开始**

#### **准备工作**

- python 3.8+ 及 pip
- 具备良好网络环境的电脑
- screen （仅在linux环境下需要）

#### **开始组建**

1. 新建文件夹
2. 将本项目放入文件夹中
3. 运行下面的命令

```shell
# 安装依赖
pip install -r requirements.txt
```
4. 前往[gocqhttp](https://github.com/Mrs4s/go-cqhttp/releases)下载对应系统/架构的压缩包
5. 在第一步的文件夹里面新建一个叫做gocqhttp的文件夹
6. 将压缩包的文件解压进文件夹内

现在项目目录应如下：

```yaml
axtybot/
├── gocqhttp/       
│   ├── config.yml
|   ├── go-cqhttp.bat # 仅windows下
│   └── go-cqhttp # windows下为go-cqhttp.exe
└── axty/        
    ├── bot.py
    ├── bot_config.py
    └── public/
    └── bot_plugins/
```

#### **开始运行**

Linux下：

```shell
screen -R nonebot
cd axty             # 切换到axty文件夹内
python bot.py       # 运行nonebot
按住CTRL+A+D
screen -R gocqhttp
cd gocqhttp
./go-cqhttp         # 如果提示权限问题则 chmod +x go-cqhttp
```

Windows下：

- 打开 axty 文件夹
- 双击 bot.py
- 返回到上一级
- 打开 gocqhttp文件夹
- 双击 go-cqhttp.bat

不出意外的话，您将成功运行起来本项目

------

### 特性

- 分周目的插件包 / 内容包
- 分周目的权限管理
- 简易的修改回答内容

------

### 待(hua)更新(da)内容(bing)

1. 可使用web面板(需要服务器商开启80/443端口)管理
2. 全自动加入黑名单/同意好友
3. 未完持续

------

### 感谢名单


感谢 VANILO 管理组对于本bot的支持

感谢苟佬 (azurePh03nix) 解决了我在写bot时碰见的低级问题

感谢 MARYT/ VANILO 玩家对于本bot的欢迎

感谢 Fantasy_Z 对于本项目持续的提供好主意

感谢 凌波佬 的捉虫(反馈错别字)

本bot参考了开源项目 Box-s-ville/luciabot，在此向项目开发者致谢！

本bot参考了开源项目 nonebot/nonebot 的教程,在此向教程编写者致谢！

本bot参考了 MARYTbot 的代码，在此向苟佬致谢！
