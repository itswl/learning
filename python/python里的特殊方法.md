## 特殊方法是什么
是一种具有特殊魅力的正常方法，python通过这些方法可以赋予你的class魔力。

这些魔法方法 都是以双下划线`__`作为 前缀和后缀。

## 初始化

**`__new__()`创造实例， `__init__()`初始化实例。**

`__init__()` 是一个类 (class) 的第一个方法，也叫构造函数。 是第一个被创建，但不是第一个被执行的。

`__new__()` 才是最早被调用的方法 



1. `__new__()`  : 先读取参数( 如类名称,args,和kwargs）, 然后 __new__() 方法把这些参数传递给 `__init__()` , `__new__(class_name, args, kwargs)`
2. `__init__()` : 类的初始化方法或构造方法, 几乎用于 全局的初始化目的。 `__init__(slef, args, kwargs)` 
3. `__del__()`  : 类的析构函数，定义一个对象被垃圾回收的行为。 `__del__(self)`

```
class SimpleInit:
    def __new__(cls):
        print("__new__ is called")
        return super(SimpleInit, cls).__new__(cls)  # 不过与python3.7后的dataclass 不兼容，dataclass 机制得好好看一下

    def __init__(self, value=10):
        print('__init__ is called')
        print("self is: ", self)
        self._list = [value]

    def __del__(self):
        print(self._list)
        del self._list
        print(self._list)

a = SimpleInit()
a.__del__()
'''
输出如下：
__new__ is called   # __new__()创造实例， __init__()初始化实例
__init__ is called
self is:  <__main__.SimpleInit object at 0x0000017E8A132470>
[10]
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-22-3666a9307d4d> in <module>
----> 1 a.__del__()

<ipython-input-21-cb926d3eed30> in __del__(self)
     12         print(self._list)
     13         del self._list
---> 14         print(self._list)
     15
     16 a = SimpleInit()

AttributeError: 'SimpleInit' object has no attribute '_list'
'''
```

## 算术运算,增量赋值

1.  `__add__(self.other)  +    __iadd__(self.other)  +=`
2.  `__sub__(self.other)  -    __isub__(self.other)  -=`
3.  `__mul__(self.other)  *    __imul__(self.other)  *=`
4.  `__floordiv__(self.other) //   __ifloordiv__(self.other) //=`
5.  `__div__(self.other) /   __idiv__(self.other) /=`
5.  `__mod__(self.other)  %   __imod__(self.other)  %=`
6.  `__and__(self.other)  &   __iand__(self.other)  &=`
7.  `__or__(self.other)  |    __ior__(self.other)  |=`
8.  `__xor__(self.other)  ^   __ixor__(self.other)  ^=`
9.  `__pow__(self.other)  **   __ipow__(self.other)  **=`
10. `__lshift__(self.other)  <<   __ilshift__(self.other)  <<=`
11. `__rshift__(self.other)  >>   __irshift__(self.other)  >>=`
```
from dataclasses import dataclass, field

@dataclass
class Simpleadder:
    _elements:list = list

    def __add__(self, other):
        return self._elements + other._elements


a = Simpleadder([1,2,3,4,5])
b = Simpleadder([4,5,6,7,8])
print(a, b)  # Simpleadder(_elements=[1, 2, 3, 4, 5]) Simpleadder(_elements=[4, 5, 6, 7, 8])
print(a + b)  # [1, 2, 3, 4, 5, 4, 5, 6, 7, 8]
```
## 比较运算
**python3.7 可使用dataclass**

1. `__eq__(self.other)  ==`
2. `__ne__(self.other)  !=`
3. `__lt__(self.other)  <`
4. `__gt__(self.other)  >`
5. `__le__(self.other)  <=`
6. `__ge__(self.other)  >=`

## 类型转换
1. `__int__(self)`      int
2. `__long__(self)`     long
3. `__float__(self) `   float
4. `__complex__(self)`  complex
5. `__oct__(self)`      octal (八进制)
6. `__hex__(self)`      (十六进制)
7. `__index__(self)`    转为int, 当对象被用于切片表达式

## 最常用
1. `__str__(self)` 
2. `__repr__(self)`  类似`__str__()`  str()主要用于人类可读, repr() 机器可读
3. `__hash__(self)`  定义了行为调用hash()
4. `__len__(self)`   返回容器长度
5. `__getitem__(self)` __setitem__(self)
6. `__delitem__(self)`  定义一个删除一个项目的行为
7. `__iter__(self)`    返回一个迭代容器
8. `__call__(self)`    使实例能够像函数一样被调用，同时不影响实例本身的生命周期

**`__call__()`不影响一个实例的构造和析构。但是`__call__()`可以用来改变实例的内部成员的值**
```
from dataclasses import dataclass

@dataclass()
class X:
    a:int
    b:int
    range:int

    def __call__(self):
        print('__call__ with （{}, {}）'.format(self.a, self.b))


x = X(1,2,3)
print(x)
x()   #  把实例直接当函数调用
```
