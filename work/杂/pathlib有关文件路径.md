
**面向对象的文件系统路径**

pathlib 提供表示文件系统路径的类，适用于不同的操作系统

纯路径提供纯粹的计算操作，具体路径继承纯路径且可以进行 I/O 操作
```
import pathlib
print(pathlib.PurePath(__file__)) # 文件路径
print(pathlib.PurePath(__file__).match('*.py'))
print(pathlib.Path.cwd())  #  当前路径 （运行路径）
print(pathlib.Path.cwd().parent)  # 上一级
print(pathlib.Path.cwd().parent.parent)  # 上上级


parts = ['first', 'second', 'third']
print(pathlib.Path.cwd().parent.joinpath(*parts))  # 在上一级开始拼接路径
```

**更多**
```
from pathlib import Path
Path.iterdir() # 遍历目录的子目录或者文件

Path.is_dir() # 判断是否是目录

Path.glob() # 过滤目录(返回生成器)

Path.resolve() # 返回绝对路径

Path.exists() # 判断路径是否存在

Path.open() # 打开文件(支持with)

Path.unlink() # 删除文件或目录(目录非空触发异常)

# 基本属性
Path.parts # 分割路径 类似os.path.split(), 不过返回元组

Path.drive # 返回驱动器名称

Path.root # 返回路径的根目录

Path.anchor # 自动判断返回drive或root

Path.parents # 返回所有上级目录的列表

# 改变路径
Path.with_name() # 更改路径名称, 更改最后一级路径名

Path.with_suffix() # 更改路径后缀

#拼接路径
Path.joinpath() # 拼接路径

Path.relative_to() # 计算相对路径

# 测试路径
Path.match() # 测试路径是否符合pattern

Path.is_dir() # 是否是文件

Path.is_absolute() # 是否是绝对路径

Path.is_reserved() # 是否是预留路径

Path.exists() # 判断路径是否真实存在

# 其他方法
Path.cwd() # 返回当前目录的路径对象

Path.home() # 返回当前用户的home路径对象

Path.stat()  # 返回路径信息, 同os.stat()

Path.chmod()  # 更改路径权限, 类似os.chmod()

Path.expanduser() # 展开~返回完整路径对象

Path.mkdir() # 创建目录

Path.rename()  # 重命名路径

Path.rglob()  # 递归遍历所有子目录的文件

```


```
import pathlib
'''
有关文件路径
'''
current_p = pathlib.Path.cwd() # 当前运行路径
print(current_p)
p = pathlib.Path(__file__)

print(p.stat()) # 获取文件信息

print(p) # 文件相对运行路径的路径
print(p.resolve())  # 返回文件所在的绝对路径
print(p.resolve().parent.parent)  # 返回文件上上级路径
print(pathlib.PurePath(p.resolve()).parts) # 将绝对路径以元组的方式返回
print(pathlib.Path.home())  # 家目录 例如: /home/root
print(pathlib.Path(p).exists() ) # 判断路径或文件是否存在

print(p.name) # 获取文件名 path.py
print(p.stem) # 获取文件名（没后缀）
print(p.suffix)  # 获取文件的后缀名 .py
print(p.suffixes)  #  获取文件的后缀名 ['.py'],  可能会有 ['.tar','.gz']


new_path1 = p.with_name('test.py')
print(new_path1) # 路径下 + test.py
new_path1.touch()  # 创建文件
print(new_path1) # 最后文件名改为test.py  (仅仅改字符串)
new_path2 = new_path1.with_suffix('.txt')
try:
    new_path1.rename(pathlib.Path(new_path2)) # 改为 .txt
except Exception as e:
    print(f'{e}')
    new_path1.replace(pathlib.Path(new_path2))
finally:
    print('已改名完成')

'''
路径拼接
'''
path = pathlib.Path(current_p,'parent_path','path')
print(path)
path1 = pathlib.Path(path).joinpath('hahaha','path1.py')
print(path1)


'''
遍历文件夹
'''
print([path for path in current_p.iterdir()]) # 当前路径下所有路径
print([path for path in current_p.glob('*.py')]) # 找出当前路径下含有 .py 的路径
print([path for path in current_p.rglob('*.py')])  # 找出当前路径下所有(子，子子...)含有 .py 的路径

'''
文件操作
open(mode='r', bufferiong=-1, encoding=None, errors=None, newline=None)
'''
with p.resolve().open(encoding = 'utf-8') as f:
    print(f.read())

# 对于简单文件操作
# .read_text(): 以文本模式打开路径并并以字符串形式返回内容。
# .read_bytes(): 以二进制/字节模式打开路径并以字节串的形式返回内容。
# .write_text(): 打开路径并向其写入字符串数据。
# .write_bytes(): 以二进制/字节模式打开路径并向其写入数据。
print(p.resolve().read_text(encoding='utf-8'))

'''
文件夹创建及删除
'''

ex_path = pathlib.Path(current_p,'parent_path','path')
# 创建文件目录，由于parents为True，所以逐级创建出来。
ex_path.mkdir(parents = True, exist_ok = True)
# 删除路径对象目录，如果要删除的文件夹内包含文件就会报错
ex_path = pathlib.Path(current_p,'parent_path','path')
ex_path.mkdir(parents = True, exist_ok = True)
new_path1 = ex_path.with_name('test.py')
print(new_path1) # 路径下 + test.py
new_path1.touch()  # 创建文件
new_path2 = new_path1.with_suffix('.txt')
print(new_path2) # 最后文件名改为test.py  (仅仅改字符串)
try:
    new_path1.rename(pathlib.Path(new_path2)) # 改为 .txt
except Exception as e:
    print(f'{e}')
    new_path1.replace(pathlib.Path(new_path2)) # 替换文件
finally:
    print('已改名完成')
try:
    pathlib.Path(new_path2).unlink()  # 删除 test.txt
    ex_path.parent.rmdir()  # 删除文件夹 非空则会报错
except Exception as e:
    print(f'{e}')
    import shutil
    shutil.rmtree(ex_path.parent)  # 递归删除

```
https://blog.csdn.net/itanders/article/details/88754606

[pathlib官方文档](https://docs.python.org/zh-cn/3/library/pathlib.html)
