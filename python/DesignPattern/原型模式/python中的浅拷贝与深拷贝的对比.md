# python 浅拷贝与深拷贝

## python的引用计数

1. int float str tuple 为不可变对象
2. list dict set  为可变对象

python 内不可变对象的内存管理方式是**引用计数**，python 不会对值相同的不可变对象，申请单独的内存空间。只会记录它的引用次数。
```
import copy
a = 'weilai'
b = a
c = copy.copy(a)
if id(a) == id(b) == id(c):
    print(f'all id is {id(a)}')
else:
    print(f'id(a) is {id(a)}')
    print(f'id(b) is {id(b)}')
    print(f'id(c) is {id(c)}')
```

## 浅拷贝
浅拷贝会创建一个新的对象，对于对象中的元素，他依然会引用原来的物体
```
import copy 
a = ['weilai', 'handsome']
b = a
c = copy.copy(a)
if id(a) == id(b) == id(c):
    print(f'all id is {id(a)}')
else:
    print(f'id(a) is {id(a)}')
    print(f'id(b) is {id(b)}')
    print(f'id(c) is {id(c)}')  # c创建了一个新对象，指向原来的 a

a.append('cool')
print(a)
print(b)
print(c)  # c 还是['weilai', 'handsome']
```
由于浅拷贝会使用原始元素的引用（内存地址），所以在操作对象内部的可变元素时，其结果是会影响到拷贝对象的

```
import copy 
a = [[1, 2, 3], 3, 4]
b = a
c = copy.copy(a)  # [[1, 2, 3], 3, 4]
a[0][0] = 'a' 
a[1] = 'b'
print(a)  # [['a', 2, 3], 'b', 4]
print(b)  # [['a', 2, 3], 'b', 4]
print(c)  # [['a', 2, 3], 3, 4]
```
## 深拷贝
**深拷贝遇到可变对象，则又会进行一层对象的创建，操作被考对象内部的可变对象，不影响拷贝对象内部的值。
```
import copy 
a = [[1, 2, 3], 3, 4]
b = a
c = copy.deepcopy(a)  # [[1, 2, 3], 3, 4]
a[0][0] = 'a' 
a[1] = 'b'
print(a)  # [['a', 2, 3], 'b', 4]
print(b)  # [['a', 2, 3], 'b', 4]
print(c)  # [[1, 2, 3], 3, 4]

```

## 总结


**python变量实际上是指向相关值在内存中存储位置的指针 。 深浅拷贝都是对源对象的复制，占用不同的内存空间**
1. 如果源对象只有一级目录的话，源对象做任何改动，不影响深浅拷贝对象
2. 如果源对象不止一级目录的话，源对象做任何改动，都要影响浅拷贝，但不影响深拷贝
3. 序列对象的切片其实是浅拷贝，即只拷贝顶级的对象
