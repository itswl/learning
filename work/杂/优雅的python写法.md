# 学习python cook book 有感

## 1. 交换变量
```
a, b = b, a 
```
## 2. 循环遍历区间
```
for i in range(6):
    print (i)
```    
## 3. 带有索引位置的集合遍历
```
for i, color in enumerate(colors):
    print (i ,colors[i])
```
## 4. 字符串拼接
```
print '. ' .join(names)  
'''
join 方法全程只会产生一个字符串对象，而每执行一次 + 操作，就会在内存中生成一个新的字符串对象
'''
```
现在已经可以直接使用加号，不会影响效率。（不要被落后的经验给拖累了）
## 5. 打开/关闭文件
```
with open ('xxx.xxx','r') as f:
    data = f.read()
```   
## 6. 列表推导式
```
[i for i in range(10)]
```
## 7. 善用装饰器
```
'''
装饰器可以吧与业务逻辑无关的代码抽离出来，让代码保持干净清爽，且能多次利用
url 曾使用过直接从cache读出，没有的话存到saved中
'''
import urllib.request as urllib

def cache(func):
    saved = {}
    
    def wrapper(url):
        if url in saved:
            return saved[url]
        else:
            page = func(url)
            saved[url] = page
            return page
        
        return wrapper 
        
@cache
def web_lookup(url):
    return urllib.urlopen(url).read()
```
## 8. 合理使用列表
```
'''
list是一个查询效率高于更新操作的数据结构,
删除/插入 一个元素 执行的效率较低，因为还要对剩下的元素进行移动
'''
from collections import deque
names = deque([1, 2, 3, 4, 'haha'])
names.popleft()
names.appendleft('mark')

'''
deque 是一个双向队列的数据结构，删除元素和插入元素会很快
'''
```
## 9. 序列解包
```
p = '1' ,  '2' , '3' , 4 
a, b, c, d, = p
```

## 10. 遍历字典的 key 和 value
```
dict ={1:'haha',2:'xixi'}
for key, value in dict.items():
    print(key ,' + ', value)
'''
dict.items 返回迭代器对象，可节省更多的内存
'''
```
## 11. 链式比较操作
```
age = 18
if 18 < age < 60:
    print('young man')
    
False == True == True == True
# False 
```
## 12. if/else
```
text = '男' if gender == 'male' else '女'
```
## 13. True/Fales 值判断
```
if a:
    do_someting()
if b:
    do_someting()
'''
a,b 的值有就是True, 没有就是False
'''
```
## 14. 字符串格式化
```
a,b = 'haha', [1,2,3]
s = f'str is {a}, list is {b}' 
'''
不支持python2
'''
```
python3.8  f-strings 支持 =
```
a,b = 'haha', [1,2,3]
s = f'str {a = }, list {b = }' 
```
## 15. 列表切片
```
items = range(10)
sub_items = items[1:4]  # 取第1号到第4号元素
odd_items = items[1::2]  # 第1号到最后面，步长为2 （奇数）
copy_items = items[::]  # 或者 items[:]
```
## 16. 善用生成器
```
def fib(n):
    a, b = 0, 1
    while a < n:
        yeild a 
        a ,b = b, a + b
'''
生成器的好处是无需一次性把所有元素加载到内存，
只有迭代获取元素时才返回该元素，
而列表是预先一次性把全部元素加载到内存中
遇到 yield 会暂停执行另一个函数
'''
```
# 17. 获取字典元素
```
d = {'name':'foo'}
d.get('name','unknow')
d.get('age','unknow')
```
# 18. 预设字典默认值
```
groups = {}
for (key, value) in data:
    groups.setdefault(key, []).append(value)

from collections import defaultdict
groups = defaultdict(list)
for (key, value) in data:
    groups[key].append(value)
```

## 19 字典/列表/集合 推导式
```
numbers = [1, 2, 3, 4]
my_dict = {number: number*2 for number in numbers}
print(my_dict)
```

## 20. for/else
'''
python 特有的语法格式，else中的代码在for 循环完所有元素成后执行
'''
```
flagfound = False
mylist = [1, 2, 3, 'theflag', 4, 5, 6]
for i in mylist:
    if i == 'theflag':
        flagfound = True
        break
    print(i)    
else:
    raisd ValueError('list argument missing terminal flag')
```
## 21 一些特性
### 给数字加\_分组并不影响实际
```
a = 11_22_33_44
error = 0xbad_c0ffee
```
### 将类型注释添加到函数和方法中
注释仅是一种类型的提示, 对实际运行没有影响
```
a: int =2   # 声明变量
def my_add(a:str,b:int) -> int:  # 声明方法返回值
    return a + b
my_add(1,2)
```
借助typing模块
```
from typing import List, Tuple, Dict
names: List[str] = ['haha', 'xixi']
version: Tuple[int, int, int] = (3, 7, 8)
operations: Dict[str, bool] = {'show' : False, 'sort' : True}

```
### 直接操作数字
```
PI =3.141592653
f'PI is {PI:.4f}'
```
### 将值赋值给未初始化的变量
python3.8 “海象运算符”,  `:=`可在表达式内部为变量赋值
```
if (my_variable := input()):
    print(f'input {my_variable}') #exists now
else:
    print('input nothoing')
```
### 仅限位置形参
python3.8 

形参 a 和 b 为仅限位置形参，c 或 d 可以是位置形参或关键字形参，而 e 或 f 要求为关键字形参
```
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)
f(10, 20, 30, d=40, e=50, f=60)
```
