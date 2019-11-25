## docker
**Linux 容器**不是模拟一个完整的操作系统，而是对进程进行隔离。对于容器里面的进程来说，它接触到的各种资源都是虚拟的，从而实现与底层系统的隔离

Docker 属于 Linux 容器的一种封装，提供简单易用的容器使用接口

**Docker** 将应用程序与该程序的依赖，打包在一个文件(**image**)里面。运行这个文件，就会生成一个虚拟容器。程序在这个虚拟容器里运行，就好像在真实的物理机上运行一样.
容器还可以进行版本管理、复制、分享、修改，就像管理普通的代码一样。

**image 文件可以看作是容器的模板。Docker 根据 image 文件生成容器的实例。同一个 image 文件，可以生成多个同时运行的容器实例**
## docker 安装
```
curl https://get.docker.com > /tmp/install.sh
chmod +x /tmp/install.sh
/tmp/install.sh
sudo usermod -aG docker root
service docker restart
service docker status
```

## 快速确认
`docker version `

## 第一个镜像

```
docker run debian echo "hello world"
```

1. **docker run**  : 启动容器
2. **debian** : 使用的镜像名称  （在docker hub 进行搜素，并下载最新版）
3. **echo "hello world"** : 执行的命令


```
docker run -i -t debian /bin/bash
```


1. **-i -t**  : 附有一个 tty 的交互会话     -i 支持stdin , -t 终端或伪终端
2. **/bin/bash** : 获得一个 bash shell
3. **退出 shell, 容器就会停止**

``` 
docker run --name weilai -h docker -i -t debian /bin/bash  # -h 指定hostname --name 指定docker name
docker inspect weilai # 获取 weilai 容器的更多信息
doker diff weilai  # 查看 weilai 文件的更改
docker logs weilai # weilai 容器里曾经发生的事情
docker ps # 正在运行的 docker 容器
docker ps -a # 列出所有容器
docker start weilai # 启动已有容器   docker run 是启动一个新的实例  
docker attach weilai  # 切换到运行交互式容器
docker stop weilai  # 停止容器
docker rm weilai 

```
