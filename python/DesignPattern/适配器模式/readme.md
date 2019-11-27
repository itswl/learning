## 适配器模式具有以下要素：
1. 目标  --定义客户端所使用的特定于 领域的接口
2. 客户端  -- 使用遵从于 目标接口的对象
3. 适配者类  --由于对象不遵从目标而必须修改的接口
4. 适配器  -- 将适配者类中所具有的接口 修改为我们想要在客户端中 使用的接口的代码


**1.定义我们希望适应的组成部分是什么**
**2.识别出客户端需要的接口**
**3.设计和实现适配器以便将客户端所需的接口映射到适配者类所提供的接口**


客户端从适配者类中解耦出来并且被耦合到接口，这样实现了可扩展性和可维护性

### 不要重复自己

1. 面向接口 而非 面向现实进行编程
2. 支持对象组合，而非继承

### 关注点分离
 
将系统分割为 单独单元 并让每个单元尤其自己的关注点。单元彼此越独立，系统的维护和扩展也会变的越容易。


```
class ObjectAdapter(object):
    def __init__(self, what_i_have, provided_function):
        self.what_i_have = what_i_have
        self.required_function = provided_function
    
    def __getattr__(self, attr):
        return getatrr(self.what_i_have, attr)
        
```
