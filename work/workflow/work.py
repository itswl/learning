# 工作流程
# 运行前先修改host
# paramiko 模块需安装

from os import path
from os import listdir
import os
import sys
from ssh_connection_sh import *
from upload import *
from cmd_list import CMD

## 完整流程
def a():
    a1() 

def b():
    b1() 


if __name__ == '__main__':
    print('start work')
    a():
    b():

