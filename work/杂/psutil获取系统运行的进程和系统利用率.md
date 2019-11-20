# 三大模块
1. System related function
2. Processes
3. Windows Service

# 安装方法
`pip install psutil`

`pip install -user psutil `

# 使用方法
```
import psutil

'''
待探索
'''
# cpu 节选
psutil.cpu_times() # 将系统cpu时间作为命名元组返回
psutil.cpu_percent(interval=None, percpu=None)  # cpu 使用百分比
psutil.cpu_percent(interval=3, percpu=True) # 3秒间隔中，cpu 的占用率
psutil.cpu_count()  # cpu 逻辑核心数
psutil.cpu_count(logical=True) # cpu 物理核心数


for i in range(10):
    psutil.cpu_percent(interval=3, percpu=True)  # 3秒间隔中，cpu 的占用率

# 内存节选
psutil.virtual_memory()  # 将系统内存使用情况作为命名元组返回

# 当内存不足，发出提示
dan = 300 * 1024 * 1024 # 单位为b
if psutil.virtual_memory().available <= dan:
    print('memory warning')

# 进程信息
psutil.pids()
[p.info for p in psutil.process_iter(attrs=['pid', 'name']) if 'python' in p.info['name']]
```

# 更多
单个进程信息
```
p = psutil.Process(2423) 
p.name()   #进程名
p.exe()    #进程的bin路径
p.cwd()    #进程的工作目录绝对路径
p.status()   #进程状态
p.create_time()  #进程创建时间
p.uids()    #进程uid信息
p.gids()    #进程的gid信息
p.cpu_times()   #进程的cpu时间信息,包括user,system两个cpu信息
p.cpu_affinity()  #get进程cpu亲和度,如果要设置cpu亲和度,将cpu号作为参考就好
p.memory_percent()  #进程内存利用率
p.memory_info()    #进程内存rss,vms信息
p.io_counters()    #进程的IO信息,包括读写IO数字及参数
p.connectios()   #返回进程列表
p.num_threads()  #进程开启的线程数
听过psutil的Popen方法启动应用程序，可以跟踪程序的相关信息
from subprocess import PIPE
p = psutil.Popen(["/usr/bin/python", "-c", "print('hello')"],stdout=PIPE)
p.name()
p.username()
```

# 获取开机时间
```
psutil.boot_time() # 时间戳

datetime.datetime.fromtimestamp(psutil.boot_time ()).strftime("%Y-%m-%d %H: %M: %S") #转换成自然时间格式
``
