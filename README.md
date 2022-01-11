# axtybot
运行于MARYT/VANILO服务器群内的玩家机器人，使用nonebot+gocqhttp搭建

~~在运行于装载ubuntu18系统的256mb内存的海外vps上时状态良好~~

目前已加入国内高性能vps豪华套餐（）

如果您想在装载windows系统的主机上使用，请前往https://github.com/RisingInIris2017/MARYTBot

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

安装nonebot(如果您想运行本项目还需要安装jieba分词和pythonping等几个包)

```
pip install nonebot
```
可选（安装jieba分词和pythonping和nonebot的计划任务(会顺带安装APScheduler)和用来转换时区的第三方模块）
```
pip install jieba pythonping "nonebot[scheduler]" pytz
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
screen -R gocqhttp #进入叫做gocqhttp的screen里面，如果没有叫这个名字的screen则会创建一个同名的
cd gocqhttp        #切换到gocqhttp文件夹内
./go-cqhttp        #运行gocqhttp
```

#### **运行nonebot**

```
screen -R nonebot   #进入叫做nonebot的screen里面，如果没有叫这个名字的screen则会创建一个同名的
cd axty             #切换到axty文件夹内
python bot.py       #运行nonebot
```

不出意外的话，您将成功运行起来本项目
