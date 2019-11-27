**当希望通过一个通用接口来创建对象，而不是让创建代码分散在整个系统中**

**创建一个集中式的系统来进行对象创建的一种方式就是使用工厂模式**

原型模式不需要子类化，不过需要一个初始化操作，而工厂模式需要子类化，但不需要初始化

## 工厂模式一个简单的实现
原始代码
```
import pygame

windows_dimensions = 800,600
screen = pygame.display.set_mode(windows_dimensions)

x,y = 100, 100

player_quits = False

while not player_quits:
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            player_quits = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -=4
        if pressed[pygame.K_DOWN]: y += 4
        if pressed[pygame.K_LEFT]: x -= 4
        if pressed[pygame.K_RIGHT]: x += 4

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen,(255, 255, 0 ), pygame.Rect(x, y, 20, 20))

    pygame.display.flip()
```

**改写，方便扩展**

shape_factory.py
```
import pygame
import time
# pygame.init()

class Shape():
    def __init__(self,x ,y):
        self.x = x
        self.y = y

    def draw(self):
        raise NotImplementedError()

    def move(self, direction):
        if direction == 'up':
            self.y -= 4
        if direction == 'down':
            self.y += 4
        if direction == 'left':
            self.x -= 4
        if direction == 'right':
            self.x += 4

    @staticmethod
    def factory(type):   # 工厂模式,可在这里加type类型
        if type == 'Circle':
            return Circle(100, 100)
        if type == 'Square':
            return Square(100, 100)
            assert 0, 'Bad shape requested:  ' + type

class Square(Shape):
    def draw(self):
        pygame.draw.rect(screen,(255, 255, 0 ), pygame.Rect(self.x, self.y, 20, 20))

class Circle(Shape):
    def draw(self):
        pygame.draw.circle(screen, (0, 255, 255), (self.x, self.y),10)

if __name__ == '__main__':
    windows_dimensions = 800,600
    screen = pygame.display.set_mode(windows_dimensions)

    obj = Shape.factory('Circle')
    player_quits = False

    while not player_quits:
        for event in  pygame.event.get():
            if event.type == pygame.QUIT:
                player_quits = True

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]: obj.move('up')
            if pressed[pygame.K_DOWN]: obj.move('down')
            if pressed[pygame.K_LEFT]: obj.move('left')
            if pressed[pygame.K_RIGHT]: obj.move('right')

            screen.fill((0, 0, 0))
            obj.draw()

        pygame.display.flip()
```

## 抽象工厂
**当希望创建单个接口来访问整个工厂集合时，可以使用一个抽象工厂**
```
import  abc
class AbstractFactory():  # 抽象工厂会定义这些具体工厂的结构，之后这些具体工厂会创建本例中的原型和正方形
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def make_object(self):
        return

class CircleFactory(AbstractFactory):
    def make_object(self):
        # do  something
        return Circle()

class SquareFactory(AbstractFactory):
    def make_object(self):
        # do  something
        return Square()

def draw_function(factory):
    drawable = factory.make_object()
    drawable.draw()

def prepare_client():
    squareFactory = SquareFactory()
    draw_function(squareFactory)

    circleFactory = CircleFactory()
    draw_function(circleFactory)

```
