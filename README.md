## **axtybot**

~~运行于MARYT/VANILO服务器群内的玩家机器人，使用nonebot+gocqhttp搭建~~

本分支是第一个同时也是最后一个对于MARYT服务器的内容作支持的版本

适用于 **MARYT 10th**

在运行于装载ubuntu18系统的256mb内存的海外vps上时状态良好

~~目前暂定每周目结束后创建新的分支更新新的周目有关内容~~

如果您想在装载windows系统的主机上使用，请前往[MARYTbot](https://github.com/RisingInIris2017/MARYTBot)

------

### **教程**

首先，确保有一台能够稳定提供服务的主机，这里没有太大的性能要求(能流畅跑起来就行)

#### **准备工作**

注：如果您使用的是ubuntu20则可以考虑不用安装python3.8+（自带）

安装screen(保证稳定提供服务)

```shell
sudo apt install screen
```

安装python 3.8+和pip3

```shell
sudo apt install python3
```

```shell
sudo apt install python3-pip
```

配置python 3.8+(ubuntu20可跳过此步)并且使pip3的python为python3.8+

如果不出意外的话，当您在终端运行 `python -V` 和 `pip -V` 两条命令时会输出如下内容

```python
$：python -V
Python 3.8.12      #这里的3.8.12可以是任意3.8+.x
```

```python
$：pip -V
pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)
#这里的20.0.2可以是任何x.x.x
#from后面的/usr/lib/python3/dist-packages/pip是pip所在的路径(一般是当前所用python/dist-packages/pip目录)
#python 3.8指的是pip的所用的python的版本，需3.8+
```



#### **运行axtybot**

安装nonebot

```shell
pip install nonebot
```
**可选，但如果运行本项目的话是必装的**(不然会在运行时报没找到对应模块，并且依赖于对应模块的插件不会运行)

（依次是安装jieba分词和pythonping和nonebot的计划任务(会顺带安装APScheduler)和用来转换时区的第三方模块）

```shell
pip install jieba pythonping "nonebot[scheduler]" pytz
```


下载本项目并解压到主机上相应位置（以解压到axtybot文件夹为例）

```shell
cd axtybot         #切换到axtybot文件夹内
ls                 #列出axtybot文件夹内文件夹
```

不出意外的话列出的文件夹应该是这样的:

```
axty
gocqhttp
```
#### **运行gocqhttp**
```shell
screen -R gocqhttp #进入叫做gocqhttp的screen里面，如果没有叫这个名字的screen则会创建一个同名的
cd gocqhttp        #切换到gocqhttp文件夹内
./go-cqhttp        #运行gocqhttp
```

#### **运行nonebot**

```shell
screen -R nonebot   #进入叫做nonebot的screen里面，如果没有叫这个名字的screen则会创建一个同名的
cd axty             #切换到axty文件夹内
python bot.py       #运行nonebot
```

不出意外的话，您将成功运行起来本项目

------

### 特性

1. 自动回复包含关键词的语句
2. 定时发送内容
3. 在指定的时间段内自动回复含关键词的语句(1)
4. 待添加

(1)：已实现但因一些原因并未实装，可以在bot_plugins文件夹内找到

------

### 待(hua)更新(da)内容(bing)

1. 简易的修改回答内容
2. 可使用web面板(需要服务器商开启80/443端口)管理
3. 全自动加入黑名单/同意好友
4. 未完持续
