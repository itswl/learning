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
使用`ConnectionPool` 连接

```
from redis import StrictRedis, ConnectionPool

pool = ConnectionPool(host='localhost', port=6379, db=0, password=password)
# localhost port=6379 默认数据库 password=password
redis = StrictRedis(connection_pool=pool) 
#redis.set('name', 'weilai')
print(redis.get('name'))

```

`ConnectionPool` 还支持通过 url 来构建

```
redis://[:password]@host:port/db  # tcp
rediss://[:password]@host:port/db  # tcp +ssl 
unix://[:password]@/path/to/socket.sock?db=db  # UNIX socket 连接 
```
eg:
```
url = 'redis://:password@localhost:6379/0'
pool = ConnectionPool.from_url(url)
redis = StrictRedis(connection_pool=pool) 
print(redis.get('name'))
```
## 类 改写
```
import redis

class TestString:
    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0) 
    
    def test_set(self):
        result = self.r.set('name2','weilai2') 
        print(result)
        return result

    def test_get(self):
        result = self.r.get('name2')
        print(result)
        return result

def main():
    str_obj =  TestString()
    str_obj.test_set()
    str_obj.test_get()

if __name__ == '__main__':
    main()
```

