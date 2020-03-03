## 简介
**Redis 是完全开源免费的，遵守BSD协议，是一个高性能的key-value数据库。**
1. Redis支持数据的持久化，可以将内存中的数据保持在磁盘中，重启的时候可以再次加载进行使用。
2. Redis不仅仅支持简单的key-value类型的数据，同时还提供list，set，zset，hash等数据结构的存储。
3. Redis支持数据的备份，即master-slave模式的数据备份
4. 高可用，分布式

Redis运行在内存中但是可以持久化到磁盘(性能极高)，所以在对不同数据集进行高速读写时需要权衡内存，应为数据量不能大于硬件内存.

**主要用途** ： 数据库，缓存和消息中间件

## 安装
```
wget http://download.redis.io/releases/redis-5.0.5.tar.gz
tar xzf redis-5.0.5.tar.gz
cd redis-5.0.5
make 


./redis-server  # 启动redis服务
./redis-server redis.conf  # 依据配置，启动redis服务

./redis-cli  # 使用测试客户端程序redis-cli和redis服务交互

# eg:
$ ./redis-cli
redis> ping
PONG  # 以上操作代表 redis已经安装完成。

# 在远程服务器上执行命令
redis-cli -h host -p port -a password

eg:
$redis-cli -h 127.0.0.1 -p 6379 -a "mypass"
redis 127.0.0.1:6379>
redis 127.0.0.1:6379> PING

PONG

```

### 配置  redis.conf

可以通过修改 redis.conf 文件或使用 CONFIG set 命令(**CONFIG SET CONFIG_SETTING_NAME NEW_CONFIG_VALUE**)来修改配置

eg：
```
redis 127.0.0.1:6379> CONFIG SET loglevel "notice"
OK
redis 127.0.0.1:6379> CONFIG GET loglevel

1) "loglevel"
2) "notice"
```
具体配置信息参考文档






