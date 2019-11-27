1. `docker search redis`  查询镜像
2. `docker pull redis`  拉取官方镜像
3. `docker images`  查看一下是否成功
4. 启动镜像

4.1. 下载并凭需求修改redis.conf，配置文件放在/opt/data/redis/目录下
4.2  docker启动redis

```
$ mkdir -p /opt/data/redis
$ docker run -p 6379:6379 --name myredis -v /opt/data/redis/redis.conf:/etc/redis/redis.conf -v /opt/data/redis:/data -d redis redis-server /etc/redis/redis.conf --appendonly yes 
```
命令解释说明：
-p 6379:6379  ##端口映射，:前表示主机部分，:后表示容器部分。
--name myredis  ##指定容器名称，查看和进行操作都比较方便。

-v /opt/data/redis:/data ##将主机中/opt/data/redis目录下的redis挂载到容器的/data
-v /opt/data/redis/redis.conf:/etc/redis/redis.conf ##将主机中redis.conf配置文件挂载到容器的/etc/redis/redis.conf文件中

-d redis 表示后台启动redis
redis-server /etc/redis/redis.conf  以配置文件启动redis，加载容器内的conf文件，最终找到的是挂载的目录/opt/data/redis/redis.conf
--appendonly yes 开启redis 持久化
5. `docker ps` 查看容器启动情况
6. 连接redis的几种方式

```
docker exec -ti 5f4c4cf5a5f5 redis-cli

docker exec -ti 5f4c4cf5a5f5 redis-cli a "redis passwd"

docker exec -ti 5f4c4cf5a5f5 redis-cli -h localhost -p 6379 
docker exec -ti 5f4c4cf5a5f5 redis-cli -h 127.0.0.1 -p 6379 
docker exec -ti 5f4c4cf5a5f5 redis-cli -h 172.17.0.3 -p 6379

// 注意，5f4c4cf5a5f5是容器运行的id
```
docker-compose.yml文件内容：
```
redis:
  image: redis
  container_name: test-redis
  restart: always
  ports:
    - 6379:6379
  volumes:
    - /opt/data/redis:/data
  command: redis-server --appendonly yes --requirepass "redis"
```

7. 客户端连接
docker run -it redis:latest redis-cli -h localhost -p 6379