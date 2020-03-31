pip3 install jupyter

 vi /usr/share/vim/vim81/defaults.vim
 
 
 jupyter notebook --generate-config
 
jupyter contrib nbextension install --user --skip-running-check


vi /root/.jupyter/jupyter_notebook_config.py

 rm /etc/nginx/sites-enabled/default
 
 
ln -s /root/flask_nginx.conf /etc/nginx/conf.d/

setsid uwsgi --ini /root/flask_uwsgi.ini &


nohup jupyter notebook --allow-root  > jupyter.log 2>&1 &


service nginx restart


```
from notebook.auth import passwd
passwd()

```

```
# 允许通过任意绑定服务器的ip访问
c.NotebookApp.ip = '*'
# 用于访问的端口
c.NotebookApp.port = 8527
# 不自动打开浏览器
c.NotebookApp.open_browser = False
# 设置登录密码
c.NotebookApp.password = 'sha1:14855cd59712:1cf1063d38e08cd2703a07a52b66714281676b6d'
# 设置默认目录
c.NotebookApp.notebook_dir = u'/root/'
c.NotebookApp.base_url = '/jupyter/'

```
