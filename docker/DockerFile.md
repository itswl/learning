## 简介

Dockerfile是由一系列命令和参数构成的脚本，这些命令应用于操作系统基础镜像并最终创建的一个新镜像；

## 常用命令
`FROM image:tag` : 使用的基础镜像构建
`MAINTAINER user_info` : 声明镜像维护者信息
`LABEL value` :  镜像描述元信息 (可以多条)
`ENV key value` : 设置环境变量 (可以多条)
`RUN command` :  构建镜像时需要运行的命令 (可以多条)
`WORKDIR path_dir` : 设置终端默认登录进来的工作目录
`EXPOSE port` :  当前容器对外暴露出的端口
`ADD source_dir/file dest_dir/file` :  宿主机内文件复制到容器，压缩文件会解压
`COPY source_dir/file dest_dir/file` : 同 `ADD`，不过压缩文件不解压
`VOLUME ` : 创建一个 可以从本机或其他容器挂载的挂载点，一般用来存放数据库和需要保存的数据
`CMD ` : 指定容器启动时要运行的命令，多个CMD，最后一个生效      CMD <command> 或CMD ["<executeable>","<param1>","<param2>",...] CMD ["<param1>","<param2>",...]
`ENTRYPOINT` : 指定容器启动时要运行的命令
`ONBUILD ` : 为子镜像服务
```
简单实例：父镜像Dockerfile:
FROM centos
ONBUILD RUN yum -y install vim
CMD /bin/bash
 
子镜像简单点：
FROM parent
```

## Dockerfile
```
FROM centos
MAINTAINER caofeng<caofeng2012@126.com>
 
LABEL name="imwl CentOS Image" \
    build-date="20180916"
    
ENV WORKPATH /home/
WORKDIR $WORKPATH
 
RUN yum -y install net-tools
RUN yum -y install vim
 
EXPOSE 80
CMD /bin/bash
```
