## 新建用户
```
root 权限下：
useradd test
passwd test

userdel -r test # 连同文件夹一起删掉



addgrop friends
usermod -l
addgrop -g/G
```

## 例行工作
```
at
cron
```

## 程序管理与selinux初探
1. 程序一般放在磁盘中，通过用户的执行来触发，触发后会加载到内存中成为一个个体，就是进程。
2. &   后台运行  (关掉终端会停止)   nohup + cmd + &   或者setsid + cmd + &  
3. fg  %1    将job 1拿到前台来
4. vi 下 ctrl + z 可将vi 放到后台。
5. kill  # kill -9 %1
6. bg  后台暂停的 让 后台运行

7. top -d 5 -p 12345
8. free -g
9. uname -a
10. uptime
11. netstat -a

### SELinux
**Security Enhanced Linux**


## screen 
```
screen -dmS test   # 创建 test 窗口
screen -r test     # 连接 test 窗口
screen -d test 后  screen -r test   # 如果连接不上，这样连接
screen -S test -X quit  # 删除 test 窗口
```


`rsync`  同步

`rsync -arv ./ back/`

`rsync -arv ./ root@107.172.82.37:/root/back/`
