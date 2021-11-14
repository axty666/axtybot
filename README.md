# axtybot
运行于MARYT/VANILO服务器群内的玩家机器人，使用nonebot+gocqhttp搭建

实际运行于装载ubuntu18系统的海外vps上，状态良好

如果您想在装载windows系统上使用，请前往https://github.com/RisingInIris2017/MARYTBot

### **开始使用**

------
#### **准备**

------

首先，确保有一台能够稳定提供服务的主机

安装screen(保证稳定提供服务)

```
sudo apt install screen
```

安装python 3.8+和pip3

```
sudo apt install python3
```

```
sudo apt install python3-pip
```

安装nonebot

```
pip install nonebot
```


下载本项目并解压到主机上相应位置（以解压到axtybot文件夹为例）

```
cd axtybot    #切换到axtybot文件夹内
ls            #列出axtybot文件夹内文件夹
```

不出意外的话列出的文件夹应该是这样的:

```
axty
gocqhttp
```
#### **运行gocqhttp**
```
screen -r gocqhttp #新建一个叫做gocqhttp的screen
cd gocqhttp        #切换到gocqhttp文件夹内
./go-cqhttp        #运行gocqhttp
```

#### **运行nonebot**

```
screen -r nonebot   #新建一个叫做nonebot的screen
cd axty             #切换到axty文件夹内
python bot.py       #运行nonebot
```

不出意外的话，您将成功运行起来本项目