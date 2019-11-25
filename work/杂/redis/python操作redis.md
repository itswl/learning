### 1. 准备工作
1. 安装好 `redis` 和 `RedisPy库`
2. `RedisDump`  可以用来做数据导入或导出
### 2. RedisPy库
RedisPy库 提供两个类 `redis` 和 `StrictRedis` 来实现 Redis 的命令操作。

`StrictRedis` 实现了绝大部分官方命令，参数也一一对应。

`redis` 是 `StrictRedis` 的子类，主要功能是用于向后兼容旧版本库里的几个方法。

推荐使用 `StrictRedis` 

### 连接 Redis
```
from redis import StrictRedis
# localhost port=6379 默认数据库 password=password
redis = StrictRedis(host='localhost', port=6379, db=0, password='password') 
redis.set('name', 'weilai')
print(redis.get('name'))
```
