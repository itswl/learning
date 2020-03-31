pip3 install jupyter
 jupyter notebook --generate-config
 
jupyter contrib nbextension install --user --skip-running-check
vi /root/.jupyter/jupyter_notebook_config.py

 rm /etc/nginx/sites-enabled/default
ln -s /root/flask_nginx.conf /etc/nginx/conf.d/

setsid uwsgi --ini ./flask_uwsgi.ini &
nohup jupyter notebook --allow-root  > jupyter.log 2>&1 &
service nginx restart
