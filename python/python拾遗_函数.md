## 函数

1. 函数有机会给一组语句命名
2. 函数可以减少重复代码
3. 一长段程序可以拆分为多个函数，组合起来使用
4. 一次书写, 多次调用。


在函数内部 **实参**会赋值给**形参**的变量

```
def print_twice(x):
    print(x)
    print(x)
a = print_twice('haha')
a == None  # True # 没有return,返回None  只会实现函数作用
```
#### 增量开发
每次只增加和测试一小部分代码，来避免长时间的调试过程

eg: 圆心坐标(x1,y1)例如(0,0),圆上一点的坐标(x2,y2)例如(2,2), 计算圆的面积。

1. 圆的面积
```
import math
def area(radius):
    return math.pi * radius **2
a = area(2)  # a 等于return的值
print(area(2),a)
```
2. 圆的半径
```
def distance(x1, y1, x2, y2):
   '''
   计算两点之间的距离   文档字符串，一般用来简明的解释函数是用来做什么的
   '''
   dx = x2 -x1
   dy = y2 -y1    # 临时变量，在计算中可以用来保存中间计算值
   dsquared = dx ** 2 + dy ** 2  
   result = math.sqrt(dsquared)  # 脚手架代码，构建时有用，最终可以删除
   return result
```
3. 计算结果
```
radius = distance(x1, y1, x2, y2)
result = area(radius)
```
封装成一个函数
```
def circle_area(x1, y1, x2, y2):
    radius = distance(x1, y1, x2, y2)
    result = area(radius)
    return result
```
简化  
```
def circle_area(x1, y1, x2, y2):
    return area(distance(x1, y1, x2, y2))
circle_area(0, 0, 2, 2)  # 25.132741228718352
```

### 递归
调用自己的函数称为 **递归的函数**，执行过程称为**递归**

无限递归,会在递归深度到上限时报错
```
def recurse():
    recurse()
recurse()  # RecursionError: maximum recursion depth exceeded
```

```
def print_n(s, n):
    if n <= 0:
        retrun
    print(s)
    print_n(s,n-1)
print_n('haha', 5)
```

```
def countdown(n):
    if n > 100000:   # 守卫,保护后面代码，避免出现错误
        print('over limit')  
        return  
    elif n <= 0:
        print('haha')
    else:
        print(n)
        countdown(n-1)
countdown(10000000000000)  
```

while 循环
```
def countdown(n):
    if n > 100000:   # 守卫,保护后面代码，避免出现错误
        print('over limit')  
        return  
    while n > 0:
        print(n)
        n -= 1
    print('haha')
countdown(10000000000000)  
```

```
while 1:
    line = input('>')
    if line == 'done':
        break   #  使用 break 退出循环
    print(line)
```
