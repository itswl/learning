# docker
**Linux 容器**不是模拟一个完整的操作系统，而是对进程进行隔离。对于容器里面的进程来说，它接触到的各种资源都是虚拟的，从而实现与底层系统的隔离

Docker 属于 Linux 容器的一种封装，提供简单易用的容器使用接口

**Docker** 将应用程序与该程序的依赖，打包在一个文件(**image**)里面。运行这个文件，就会生成一个虚拟容器。程序在这个虚拟容器里运行，就好像在真实的物理机上运行一样.

容器还可以进行版本管理、复制、分享、修改，就像管理普通的代码一样。

**image 文件可以看作是容器的模板。Docker 根据 image 文件生成容器的实例。同一个 image 文件，可以生成多个同时运行的容器实例**

容器是完全使用沙箱机制，相互之间不会有任何接口（类似 iPhone 的 app）,更重要的是容器性能开销极低。
 
Docker 从 17.03 版本之后分为 CE（Community Edition: 社区版） 和 EE（Enterprise Edition: 企业版）

### docker 用途
1. 简化环境搭建
2. 简化运维工作量
3. 微服务利器

### docker 安装
` uname -r` 内核版本大于 `3.10`

```
curl https://get.docker.com > /tmp/install.sh
chmod +x /tmp/install.sh
/tmp/install.sh
sudo usermod -aG docker root
service docker restart
service docker status
systemctl enable docker   # 开机自启
docker info  #  获取docker信息
docker --help # docker 帮助文档

```

### 快速确认

`docker version `


### 换源
`vi /etc/docker`  目录下找到在`daemon.json`文件（没有就新建），将下面内容写入(阿里云)
```
{
 "registry-mirrors": ["https://xxxxxxx.mirror.aliyuncs.com"]
}
```

#### 重启daemon
`systemctl daemon-reload`
 
#### 重启docker服务
`systemctl restart docker`

### 第一个镜像

```
docker run debian echo "hello world"
```

1. **docker run**  : 启动容器
2. **debian** : 使用的镜像名称  （本地如果没有镜像，就在docker hub 进行搜素，并下载最新版）
3. **echo "hello world"** : 执行的命令


```
docker run -i -t debian /bin/bash   
docker run -i -t debian   #  也可以不加  /bin/bash
```


1. **-i -t**  : 附有一个 tty 的交互会话     -i 支持stdin , -t 终端或伪终端
2. **/bin/bash** : 获得一个 bash shell
3. **退出 shell, 容器就会停止**, **Ctrl+ P + Q 退出而不停止**

``` 
docker run --name weilai -h docker -it debian /bin/bash  # -h 指定hostname --name 指定docker name
docker inspect weilai # 获取 weilai 容器的更多信息
doker diff weilai  # 查看 weilai 文件的更改
docker logs weilai # weilai 容器日志记录
docker ps # 正在运行的 docker 容器
docker ps -a # 列出所有容器
docker ps -n 2  # 显示最近创建的2个容器
docker ps -f status=exited # 查看停止的容器
docker start weilai # 启动已有容器   docker run 是启动一个新的实例  
docker attach weilai  # 切换到运行交互式容器
docker cp weilai:/tmp /home # 拷贝容器下的/tmp 到宿主机下的 /home 目录下
docker cp weilai:/tmp /home
docker exec  weilai ls -l # 进入容器 执行 ls -l 并回到宿主机，显示结果
docker start weilai # 查看容器进程
docker stop weilai  # 停止容器
docker kill weilai # 强制停止（不建议）
docker rm weilai # 删除容器
docker rmi -f debian # 删除 debian  -f 强制删除

```


`docker run` ：创建和启动一个新的容器实例，操作对象是镜像，选项较多，如果你要创建和启动一个容器，只能用run；
`docker exec`: 在已运行的容器中，执行命令，操作对象是容器，如果你要进入已运行的容器，并且执行命令，用exec；
`docker attach`: 同样操作的是已运行的容器，可以将本机标准输入（键盘输入）输到容器中，也可以将容器的输出显示在本机的屏幕上，如果你想查看容器运行过程中产生的标准输入输出，用attach；

## docker 镜像
`docker images` : 列出本机所有镜像
```
docker images -qa # -a 显示所有镜像（含中间层） -q 只显示镜像id
docker images --digests # 显示镜像的摘要信息
docker images --no-trunc # 显示完整的镜像信息 
```

`docker search redis` : 搜索 `redis` 镜像
`docker pull redis:latest`  :  拉取 `redis:latest` 镜像 (TAG  默认为 latest

删除多个镜像：`docker rmi -f 镜像名称1:[TAG] 镜像名称2:[TAG]`
中间空格隔开
 
删除全部镜像：`docker rmi -f $(docker images -qa)`

同样的

强制删除 `docker rm -f 容器ID或name`

删除多个容器 
`docker rm -f 容器ID1  容器ID2 `
 
删除所有容器

`docker rm -f $(docker ps -qa)`
 




