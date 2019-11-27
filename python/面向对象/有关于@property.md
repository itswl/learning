## 有关于@property
### 1. 将方法改为属性
这种类型的attributes并不会被实际的存储，而是在需要的时候计算出来

```
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

c = Circle(3)
print(c.area()) #  方法调用
print(c.diameter) # 属性访问
print(c.perimeter)
```

### 2. 做限定
参考前文

### 3. 
