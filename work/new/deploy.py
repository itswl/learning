# 伪代码
import os
import socket
import re
import sys
import pexpect
import config 
import logging
import time

current_path = config.current_path

logging.basicConfig(level="INFO",
                    format="[%(asctime)s] [%(levelname)8s] [%(process)d-%(thread)d] %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    filename=os.path.join(current_path, "install.log"),
                    filemode='a')


class Deploy():
    def __init__(self):
        self.a_package = os.path.join(current_path,self.get_a_package()[0])
        self.version = self.get_a_package()[1]
        self.ip = self.get_host_ip()
        self.password = config.password
        self.status = 'haha'
        
        print('Deploy package is : {}' .format(self.a_package))
        print('Deploy version is : {}' .format(self.version))
        print('Deploy package is on host : {}'.format(self.ip))
        print('FI status : {}'.format(self.status))
        logging.info('Deploy package is : {}' .format(self.a_package))
        logging.info('Deploy version is : {}' .format(self.version))
        logging.info('Deploy package is on host : {}'.format(self.ip))
        logging.info('FI status : {}'.format(self.status))


    def uninstall(self):
        datamodel_path = os.path.join(current_path, 'data_model', 'a.json') 
        with open(datamodel_path,'r') as f:
            s = f.read()
            list = re.findall('"nodemgrip": "[\s\S]*?"',s)
        for str in list:
            hostname = re.compile('"(.*)"').findall(str.split(':')[1])[0]
            if hostname != self.ip:
                cmd1 = ("scp {}/sh/uninstall.sh root@{}:/opt".format(current_path, hostname))
                cmd2 = ('ssh {} "bash /opt/uninstall.sh'.format(hostname))
                cmds = [cmd1,cmd2]
                for cmd in cmds:
                    logging.info(cmd)
                    ssh = pexpect.spawn(cmd)
                    try:
                        i = ssh.expect(['password:', 'yes/no',pexpect.EOF], timeout=5)
                        if i == 0:
                            ssh.sendline(self.password)
                            ssh.expect(pexpect.EOF)
                        ssh.sendline('yes\n')
                        ssh.expect(pexpect.EOF)
                        ssh.sendline(self.password)
                    except pexpect.EOF:
                        logging.info("EOF")
                        ret = -1
                    except pexpect.TIMEOUT:
                        logging.info("TIMEOUT")
                        ret = -2
                    logging.info('unistall {} sucess'.format(hostname))
        os.system('bash {}/sh/uninstall.sh'.format(current_path))
        os.system('bash {}/a/bin/uninstall.sh'.format(current_path))


    def unzip_package(self):
        logging.info(self.a_package)
        os.system('unzip {} -d{} > /dev/null'.format(self.a_package,current_path))
        logging.info('unzip sucess')

    def unzip_plugin(self):
        if self.version == 'aaa':
            os.system('bash {}/a/bin/start.sh stop > /dev/null '.format(current_path))
            os.system('bash {}/a/bin/start.sh start -ip {}'.format(current_path,self.ip))
            os.system('bash {}/a/bin/start.sh stop > /dev/null'.format(current_path))


    def cp_files(self):
        if self.version == 'aaa':
            os.system('bash {}/sh/cp_files_aaa.sh'.format(current_path))
        if self.version == 'bbb':
            os.system('bash {}/sh/cp_files_bbb.sh'.format(current_path))


    def upload_deployparameter(self):
        if self.version == 'aaa':
            new_password = self.get_encrypt_root_key()
            full_path = os.path.join(current_path, 'a') # 某json文件
            with open(full_path,'r') as f:
                jsonfile = f.read()
                old_str = re.findall('"systemPassword": "[\s\S]*?"',jsonfile)[0]
                old_password = old_str.split(': ')[1]

            with open(full_path,'r+') as f:
                new_password = re.sub('\s','',new_password)
                new_password = '"' + new_password + '"'
                new_str = re.sub(old_password, new_password, jsonfile,0)
                f.write(new_str)


    def deploy_start(self):
        if self.version == 'aaa': 
            logging.info('Start to install FI ')
            print('It takes a little time')
            os.system(config.aaa_start)
            print('The installer is running in the background,now you can close this terminal\n')
            print('you can use\n tailf {}/a/var/logs/app.log\n  to check process\n'.format(current_path))
            print('more logs\n cd {}/a/var/logs/tools/icta\n'.format(current_path))

        if self.version == 'bbb':
            logging.info('Start to install FI ')
            p = os.popen('bash {}/ODAEDeployTool/bin/init_root_key.sh','w'.format(current_path))
            p.write(self.password)
            os.system('bash {}/ODAEDeployTool/bin/deploy.sh'.format(current_path))



    def get_status(self):
        pass 


    def get_a_package(self):
        for file in os.listdir(current_path):
            swift_zip_aaa = re.findall(r'\ba-[\s\S]*?zip\b', file)
            swift_zip_bbb = re.findall(r'\bODAEaPlugin-[\s\S]*?zip\b', file)
            if swift_zip_aaa:
                swift_zip = swift_zip_aaa[0]
                version = 'aaa'
            elif swift_zip_bbb:
                swift_zip = swift_zip_bbb[0]
                version = 'bbb'            
        return swift_zip,version


    def get_host_ip(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('1.1.1.1', 80))
            ip = s.getsockname()[0]
        finally:
            s.close()
        return ip


    def get_encrypt_root_key(self):
        ret = -1
        cmd = 'python ' + os.path.join(current_path,'a','bin','encrypt_root_key.pyc')
        ssh = pexpect.spawn(cmd)
        try:
            i = ssh.expect(['password:'], timeout=5)
            if i == 0:
                h = ssh.sendline(self.password)
            ssh.sendline(self.password)
            r = ssh.read()
            t = r.replace(self.password,'')
            text = t.replace('\r\n','')
            return text
        except pexpect.EOF:
            logging.info ("EOF")
            ret = -1
        except pexpect.TIMEOUT:
            logging.info ("TIMEOUT")
            ret = -2
        finally:
            ssh.close()
        return ret


def main():
    if cmd == 'uninstall':
        deploy.uninstall()

    elif cmd != 'uninstall':
        deploy.uninstall()
        deploy.unzip_package()
        deploy.unzip_plugin()
        deploy.cp_files()
        deploy.upload_deployparameter()
        deploy.deploy_start()


if __name__ == '__main__':
    cmd = sys.argv[1]
    deploy = Deploy()
    main()
