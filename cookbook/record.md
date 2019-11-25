
### 解压可迭代对象赋值给多个变量
```
 items = [1, 10, 7, 4, 5, (1,2,3)]
 head,*tail,(*_,end) =items
 ```
 
### 保留最后 N 个元素
``` 
from collections import deque
    >>> q = deque(maxlen=3)
    >>> q.append(1)
    >>> q.append(2)
    >>> q.append(3)
    >>> q
    deque([1, 2, 3], maxlen=3)
    >>> q.append(4)
    >>> q
    deque([2, 3, 4], maxlen=3)
    >>> q.append(5)
    >>> q
    deque([3, 4, 5], maxlen=3)
```
##### 不指定，那么无限大小队列
```
    >>> q = deque()
    >>> q.append(1)
    >>> q.append(2)
    >>> q.append(3)
    >>> q
    deque([1, 2, 3])
    >>> q.appendleft(4)
    >>> q
    deque([4, 1, 2, 3])
    >>> q.pop()  # 取出队列中最后一个元素
    3
    >>> q
    deque([4, 1, 2])
    >>> q.popleft()
    4
    >>> q
    deque([1, 2])
	
```
	在队列两端插入或删除元素时间复杂度都是 ``O(1)`` ，区别于列表，在列表的开头插入或删除元素的时间复杂度为 ``O(N)``
### 从一个集合中获得最大或者最小的 N 个元素列表
heapq 模块有两个函数：``nlargest()`` 和 ``nsmallest()`` 可以完美解决这个问题。

```

    import heapq
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
    print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]
    
    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
    expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
```
#### 对集合进行排序
    >>> nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    >>> import heapq
    >>> heap = list(nums)
    >>> heapq.heapify(heap) # 从小到大排序
    >>> heap
    [-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]
    >>>
    >>> heapq.heappop(heap)  # 弹出最小元素
    -4
    >>> heapq.heappop(heap)
    1
    >>> heapq.heappop(heap)
    2
  
 ####
 ```
    >>> line = 'asdf fjdk; afed, fjek,asdf, foo'
    >>> import re
    >>> re.split(r'[;,\s]\s*', line)
    ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
```

### 按顺序插入字典
```
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 4
d['grok'] = 3
for key in d:
    print(key, d[key])
 '''
foo 1
bar 2
spam 4
grok 3

import json
a = json.dumps(d)
type(a) # str 
print(a)  # '{"foo": 1, "bar": 2, "spam": 4, "grok": 3}'

 '''
 ```
 ### 在两个字典中寻找相同点（比如相同的键、相同的值等等）
 ```
a = {
        'x' : 1,
        'y' : 2,
        'z' : 3
    }
b = {
        'w' : 10,
        'x' : 11,
        'y' : 2
    }
    

# Find keys in common
# 类似于集合求合集差集等。
a.keys() & b.keys() # { 'x', 'y' }
# Find keys in a that are not in b
a.keys() - b.keys() # { 'z' }
# Find (key,value) pairs in common
a.items() & b.items() # { ('y', 2) }

# 使用列表推导式 从字典a 中删除 键 'z','w' 
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
  
# 值非唯一，不建议用来进行 集合 操作
```

#### 不打乱顺序去重
```
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
list(add(a)) # [1, 5, 2, 9, 10]
```

#### 可用slice() 优化切片操作
```
items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
items[a] # 等同于 items[2, 4] 
a = slice(2,10,2)
items[a]  # 等同于 items[2,10,2]
a.start # 2
a.stop  # 10
a.step # 2 

    >>> s = 'HelloWorld'
    >>> a.indices(len(s))
    (5, 10, 2)
    >>> for i in range(*a.indices(len(s))):
    ...     print(s[i])
    ...
    W
    r
    d
```

看一下range函数
 ```
 In [178]: a = (5,10,2)

In [179]: range(a)


In [180]: range(*a)
Out[180]: range(5, 10, 2)
* 就是将 a 中元素当 位置参数传进去
** 就是当字典
 def kw_dict(**kwargs):
        return kwargs
    print kw_dict(a=1,b=2,c=3) == {'a':1, 'b':2, 'c':3}
 ```
