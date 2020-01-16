# 在 /home 目录下创建redis-cluster-test 文件夹
```
➜ mkdir -p /home/redis-cluster-test
➜ cd  /home/redis-cluster-test
```
# 把下列信息写入redis-cluster.tmpl文件中
```
port ${PORT}
protected-mode no
cluster-enabled yes
cluster-config-file nodes.conf
cluster-node-timeout 5000
cluster-announce-ip 192.168.1.157
cluster-announce-port ${PORT}
cluster-announce-bus-port 1${PORT}
appendonly yes
```
 # 当前目录下生成conf和data目标，并生成配置信息
 共生成6个文件夹，从7001到7006，每个文件夹下包含data和conf文件夹，同时conf里面有redis.conf配置文件
 ```
 #
for port in `seq 7001 7006`; do \   # 7001 ~7006
  mkdir -p ./${port}/conf \
  && PORT=${port} envsubst < ./redis-cluster.tmpl > ./${port}/conf/redis.conf \
  && mkdir -p ./${port}/data; \
done
```
#  创建6个redis容器
```
for port in `seq 7001 7006`; do \
  docker run -d -ti \
  -v `pwd`/${port}/conf/redis.conf:/usr/local/etc/redis/redis.conf \
  -v `pwd`/${port}/data:/data \
  --restart always --name redis-${port} --net host \
  --sysctl net.core.somaxconn=1024 redis:latest redis-server /usr/local/etc/redis/redis.conf; \
done
```
# 进入任一容器
```
docker exec -it redis-7001 bash
```


