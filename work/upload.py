# 利用paramiko模块，安装方法为 pip install paramiko
# 将windows某文件夹下的文件上传到linux某文件夹中
# windows 文件夹地址为local_dir
# linux 文件夹地址为remote_dir
# 此为new 文件夹

import paramiko
import datetime
import os
import sys
from setting import *

def main(local_dir,remote_dir):
    try:
        t=paramiko.Transport((hostname,port))  
        t.connect(username=username,password=password)  
        sftp=paramiko.SFTPClient.from_transport(t)  
        print('upload file start %s ' % datetime.datetime.now())  
        for root,dirs,files in os.walk(local_dir):
            for filespath in files:  
                local_file = os.path.join(root,filespath)
                a = local_file.replace(local_dir,'').replace('\\','/').lstrip('/')
                print('upload', '{}{}'.format(remote_dir,a))
                remote_file = os.path.join(remote_dir,a)
                try:  
                    sftp.put(local_file,remote_file)  
                except Exception as e:  
                    sftp.mkdir(os.path.split(remote_file)[0])  
                    sftp.put(local_file,remote_file)  
            for name in dirs:  
                local_path = os.path.join(root,name)
                a = local_path.replace(local_dir,'').replace('\\','')
                remote_path = os.path.join(remote_dir,a)
                try:  
                    sftp.mkdir(remote_path)
                except Exception as e:  
                    raise e 
        print('upload file success %s ' % datetime.datetime.now())
        print('upload_files_to_',hostname)
        t.close()
    except Exception as e:  
        print('error',e)


if __name__ == '__main__':
    main(local_dir,remote_dir)
    out = input('you can close it')
