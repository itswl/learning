**当项目有几个部分不会影响代码的执行时，（例如日志记录）那么使用全局状态是可以接受的**

**避免使用全局状态的原因之一就是不想使 项目一部分中的代码修改全局状态**

logger_class.py 
```
# def log_message(msg):
#     with open( 'filename.log', 'a' ) as log_file:
#         log_file.write(f"{msg}\n")   # 代替 format，python3新特性
#
# log_message('save this for later')

class Logger():

    def __init__(self, filename):
        self.filename = filename

    def _write_log(self, level, msg):
        with open(self.filename , 'a') as log_file:
            log_file.write('{0} {1}\n'.format(level, msg))

    def critical(self, msg):
        self._write_log('CRUTICAL',msg)


    def error(self, msg):
        self._write_log('ERROR',msg)


    def warn(self, msg):
        self._write_log('WARN',msg)


    def info(self, msg):
        self._write_log('INFO', msg)


    def debug(self, msg):
        self._write_log('DEBUG',msg)

```
main_script.py
```
# import logger
#
#
# for i in range(4):
#     logger.log_message(f'log massger {i}')

from logger_class import Logger

logger_object = Logger('filename_class')
logger_object.info( 'hahahaha')

```
**__init__函数并不是真正意义上的构造函数，__init__方法做的事情是在对象创建好之后初始化变量。真正创建实例的是__new__方法**
```
class Singleton(object):
    '''
    实现__new__方法  
    并在将一个类的实例绑定到类变量_instance上,  
    如果cls._instance为None说明该类还没有实例化过,实例化该类,并返回  
    如果cls._instance不为None,直接返回cls._instance  
    '''
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)

        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1)
print(s2)

```
