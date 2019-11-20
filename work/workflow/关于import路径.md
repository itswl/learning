import sys
sys.path.append("..") # 将上层目录加入路径.
sys.path.append("/home") # 将/home 加入路径.


## 一个模块只能被导入一次
from imp import *
reload(sys) # 重新导入某模块
