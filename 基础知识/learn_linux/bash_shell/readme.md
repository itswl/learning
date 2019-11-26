# 基础
 1. `.bash_history` 历史记录
 2. `Tab` 补全
 3. `alias` 命令别名， alias lm = 'ls -al' , unalias lm (临时)  vi /root/.bashrc （永久）
 4. `type cd` 命令类型 
 5. `\` 转义

## 变量
1. 变量未设置时，默认为空
2. `PATH=$PATH:/home/bin` 变量累加
3. `export PATH` 使变量成为环境变量
4. 一般默认  大写为系统变量   小写为自行设置变量
5. 变量中 单引号''（纯文本）  与 双引号 “” (保持原本特性)
6. `current_path=$(pwd)`  接命令赋值给变量。  等同于 
``` 
current_path=`pwd`
# 建议都用 $(pwd)
``` 

7. `unset current_path` 取消变量
8. 子进程取消的变量 对 父进程无影响，子进程只继承父进程的环境变量与export。
9. `work=/opt/software`  可以`cd $work` 。写入.bash_profile 全局生效。
10. `env` 查看环境变量
11. `set` 查看所有变量
12. `echo $?` 只与上一个命令有关，上一个命令成功返回0

## 变量读取，数组与声明
```
read -s -p "please input root password:" serverPwd # -p 提示 -s 不显示
echo $serverPwd
echo -e "\n" # -e 启用反斜杠转义 （换行）
```
**数组**
```
var[1]='small'
var[2]='big'
echo "$var[1],$var[2]"
```
declare 和 typeset 一样声明变量类型
```
sum=100+1
echo $sun  # 100+1
declare -i sum=100+1
echo $sun # 101

```
## $ 
```
$0		当前脚本的文件名
$n		传递给脚本或函数的参数。n 是一个数字，表示第几个参数。例如，第一个参数是$1，第二个参数是$2。
$#		传递给脚本或函数的参数个数。
$*		传递给脚本或函数的所有参数。 # 双引号内，会识别成一个整体
$@		传递给脚本或函数的所有参数。 # 双引号内，还是会识别成一个一个参数
$?		上个命令的退出状态，或函数的返回值。一般情况下，大部分命令执行成功会返回 0，失败返回 1。
$$		当前Shell进程ID。对于 Shell 脚本，就是这些脚本所在的进程ID
```
## 与文件系统及程序的限制关系：ulimit

## 数据流重定向
st:standard
1. stdin < << (代码0)
2. stout > >> (代码0)
3. stderr 2> 2>> (代码2)
4. >/dev/null ,2>/dev/null 丢弃输出
5. > list 2>&1 (都输出 list)或 &> list

## 命令执行判断依据
1. cmd1,cmd2,cmd3 依次执行
2. cmd1 && cmd2 && cmd3 前面成功，后面才执行（$# = 0）
3. cmd1 || cmd2 || cmd3 前面成功，后面就不执行（$# = 0）

## 管道命令（pipe）
**将前一个命令的stout(不会处理stderr) 传到下一个命令的stdin中**
```
yes|bash ...sh(执行命令输入yes)
echo $PATH |cut -d ':' -f 4 # 以 : 分割$PATH ,取出第4个
echo $PATH |cut -d ':' -f 3,5 # 以 : 分割$PATH ,取出第3,5个
export | cut -c 12- # 取出12到最后的字符
last | grep -i root # 找出last中的含root行，忽略大小写 
last | grep -v root # 不含root行
last | grep root|cut -d ' ' -f 1| sort | uniq -ic # i 忽略大小写 c 计数
cat /etc/os-release | wc  # 输出  行 字数 字符数
wc -l(行) -w(英文单字) -m (多少字符)
```
## 双向重定向（tee）
**将数据流同时输出到屏幕和文件中**
```
last |tee -a last.list # -a 累加
```
# shell脚本
**shell script 是利用shell的功能所写的一个纯文本文件，将一些shell的语法命令写在里面，搭配正则表达式，管道命令与数据流重定向等功能达到我们想要的目的。**
