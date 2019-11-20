## 日志概述
1. 日志会记录下操作，运行的一些相关内容
2. 查看日志是获取信息，排查异常，发现问题的最好途径
3. 日志可在控制台显示，也可以记录到文件中，或者同时输出
4. 日志级别 一般指的是： DEBUG, INFO, WARNING, ERROR, CRITICAL 等严重等级进行划分
5. python 的 logging 提供了一组便利的日志函数，分别是： debug(), info(), warning(), error(), critical()。

```
DEBUG : 详细信息一般只在调试问题时使用
INFO : 事情按预期进行
WARNNING : 某些没有预料到的事件提示，或者将来可能出现问题的提示。
ERROR : 更严重的问题，软件的一部分功能已不能被执行
CRITICAL ： 严重错误，表明软件不能继续运行
```
6. logging 的四大组件
```
日志器  Logger     提供了应用程序一直使用的接口
处理器  Handler    将 logger 创建的日志记录发送到合适的目的输出
过滤器  Filter     提供更细粒度的控制工具来决定输出哪条日志记录，丢弃哪条日志记录
格式器  Formatter  决定日志记录的最终输出格式

logger 是入口，真正工作的是 handler, handler 还可以通过 filter 和 formatter 对要输出的日志内容做过滤和格式化处理
```

## 日志输出
### 输出到控制台
python 中日志的默认等级是 WARNING, DEBUG 和 INFO 级别的日志不会得到显示。
```
import logging

logging.info('info message')
logging.warning('warning message')
logging.error('error message')
```
logging 提供 basciConfig 让使用者可以适时调整默认日志级别
```
import logging

logging.basicConfig(level=logging.DEBUG)

logging.info('info message')
logging.warning('warning message')
logging.error('error message')
```
### 输出到文件
在 basciConfig 中填写 filename(日志名) ,filemode(写入方式)
```
import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='test.log',
                    filemode='a')

logging.info('info message')
logging.warning('warning message')
logging.error('error message')
```
## 同时输出到文件及控制器
[对比](https://github.com/itswl/work/blob/master/%E6%9C%80%E5%90%8E%E4%B8%80%E7%89%88/script/logger.py)
```
import os
import logging
import uuid
from logging import Handler, FileHandler, StreamHandler


class PathFileHandler(FileHandler):
    def __init__(self, path, filename, mode = 'a', encoding = None, delay = False):
        filename = os.fspath(filename)
        if not os.path.exists(path):
            os.mkdir(path)
        self.baseFilename = os.path.join(path, filename)
        self.mode = mode
        self.encoding = encoding
        self.delay =delay
        if delay:
            Handler.__init__(self)
            self.stream = None
        else:
            StreamHandler.__init__(self, self._open())


class Loggers():
    level_relations = {
        'debug' : logging.DEBUG, 'info' : logging.INFO, 'warning' : logging.WARNING,
        'error' : logging.ERROR, 'critical' : logging.CRITICAL
    }
    uid = uuid.uuid4()
    def __init__(self, filename = f'{uid}.log', level = 'info', log_dir = 'log',
                 fmt = "[%(asctime)s] [%(levelname)8s]  %(message)s"
                 ):
        self.logger =logging.getLogger(filename)
        abspath = os.path.dirname(os.path.abspath(__file__))
        self.directory = os.path.join(abspath, log_dir)
        format_str = logging.Formatter(fmt)
        self.logger.setLevel(self.level_relations.get(level))
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(format_str)
        file_handler = PathFileHandler(path=self.directory, filename=filename, mode='a')
        file_handler.setFormatter(format_str)
        self.logger.addHandler(stream_handler)
        self.logger.addHandler(file_handler)


if __name__ == '__main__':
    text = 'hahaha'
    log = Loggers(level='debug')
    log.logger.info(4)
    log.logger.info(5)
    log.logger.info(text)
```

