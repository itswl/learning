[参考](https://itswl.github.io/python%E5%9F%BA%E7%A1%80/python%E4%B9%8B%E5%87%BD%E6%95%B0%E5%BC%8F%E7%BC%96%E7%A8%8B/)

## 1. lambda 函数 （匿名函数）
没有函数名的函数
```
x = lambda a,b : a*b
print(x(2,3))
```
## 2. Map 函数
Map() 是 python 里的内置函数，它可以将 函数应用于各种数据结构中的元素
```
x = map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10,11])
print(x)  # <map object at 0x00000255474D24A8>  迭代器
print(list(x))  # [3, 7, 11, 15, 19] 
```
## 3. filter 函数
与 map()类似，但只返回True的元素
```
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

def filter_odd_numbers(num):
    if num % 2 == 0:
        return True
    else:
        return False
        
filtered_numbers = filter(filter_odd_numbers, numbers)
print(filtered_numbers) # <filter object at 0x00000237EFD62438> 
print(list(filtered_numbers))  # [2, 4, 6, 8]
```
## 4. any(),all()
```
x = [0, 2, 1]
print(all(x))  # False
print(any(x))  # True
```
## 5. zip()
zip() 函数 用于将可迭代对象作为参数，将对象中对应的元素打包成一个个元组，然后返回这些元组组成的列表
```
keys = ['a', 'b', 'c', 'd', 'e']
values = [1, 2, 3, 3]
zipped = dict(zip(keys, values))
print(zipped)  #  {'a': 1, 'b': 2, 'c': 3, 'd': 3}

d = {k:v for k,v in zip(zipped.values(),zipped.keys())}
print(d)  # {1: 'a', 2: 'b', 3: 'd'}

# 根据字典值的大小，对字典的项从大到小排序
print(dict(sorted(d.items(),key=lambda x:x[1],reverse=True))) # {3: 'd', 2: 'b', 1: 'a'}
```
