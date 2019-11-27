**在原型模式中，优先使用组合而非继承。组成的类使我们可以在运行时替换那些组成部分，从而彻底改善系统的可测试性和可维护性。**
## 原型模式在一般情况下的样子

**声明一个抽象基类**

prototype_1.py
```
from abc import ABCMeta, abstractmethod

class Prototype(metaclass=ABCMeta):
    @abstractmethod
    def clone(self):
        pass
```
**调用**

concrete.py
```
from prototype_1 import Prototype
from copy import deepcopy

class Concrete(Prototype):
    def clone(self):
    return deepcopy(self)
```
**扩展该抽象基类时，会强制实现clone方法。
