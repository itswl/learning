import os
import socket
import re
import config
from logger import LOG
import glob
import time
import json 
import  deploy_common


class Deploy():
    def __init__(self):
        self.swiftdeploy_package = os.path.join(config.SwiftInstall_path,self.get_swiftdeploy_package[0])
        self.version = self.get_swiftdeploy_package[1]
        self.ip = self.get_host_ip
        self.password = config.password
        self.status = self.get_status
        self.hostlist = self.get_hostlist
        self.logging = LOG(os.path.join('install.log'))

    def __repr__(self):
        return '\nDeploy package is : {} \nDeploy version is : {} \nDeploy package is on host : {}\
        \nFI status : {} \nhostlist : {}\n'.format(self.swiftdeploy_package, self.version, self.ip, self.status,self.hostlist)


    def uninstall(self):
        for ip in self.hostlist:
            if ip != self.ip:
                cmd1 = ("scp " + os.path.join(config.SwiftInstall_path, 'script', 'sh','uninstall.sh') + " root@{}:/opt".format(ip))
                cmd2 = ('ssh {} "bash /opt/uninstall.sh"'.format(ip))
                cmds = [cmd1,cmd2]
                for cmd in cmds:
                    self.logging.info(cmd)
                    deploy_common.input_password(cmd)
                self.logging.info('uninstall {}  sucess'.format(ip))
                self.logging.info('uninstall {}  sucess'.format(ip))

            os.system('bash ' + os.path.join(config.SwiftInstall_path, 'script', 'sh','uninstall.sh'))
            if self.version == 'r6':
                os.system('bash ' + os.path.join(config.SwiftInstall_path, 'SwiftDeploy', 'bin', 'uninstall.sh'))
            elif self.version == 'r7':
                os.system('bash ' + os.path.join(config.SwiftInstall_path, 'ODAEDeployTool', 'bin', 'uninstall.sh'))


    def unzip_package(self):
        self.logging.info('unzip ' + self.swiftdeploy_package)
        os.system('unzip {} -d{} > /dev/null'.format(self.swiftdeploy_package,config.SwiftInstall_path))
        self.logging.info('unzip  '+ self.swiftdeploy_package  + '  sucess')


    def init_plugin(self):
        if self.version == 'r6':
            os.system('bash ' + os.path.join(config.SwiftInstall_path, 'SwiftDeploy', 'bin', 'start.sh stop') + ' > /dev/null ')
            os.system('bash ' + os.path.join(config.SwiftInstall_path, 'SwiftDeploy', 'bin', 'start.sh start') +' -ip {}'.format(self.ip))
            os.system('bash ' + os.path.join(config.SwiftInstall_path, 'SwiftDeploy', 'bin', 'start.sh stop') + ' > /dev/null ')
            self.logging.info('init_plugin sucess')


    def cp_files(self):
        if self.version == 'r6':
            os.system('bash ' + os.path.join(config.SwiftInstall_path, 'script', 'sh', 'cp_files_r6.sh'))
        if self.version == 'r7':
            os.system('bash ' + os.path.join(config.SwiftInstall_path, 'script', 'sh', 'cp_files_r7.sh'))


    def upload_deployparameter(self):
        if self.version == 'r6':
            new_password = self.get_encrypt_root_key
            new_password = re.sub('\s','',new_password)
            full_path = os.path.join(config.SwiftInstall_path, 'SwiftDeploy','silentdeploy','deployparameter.json')
            with open(full_path,'r') as f:
                json_file =f.read()
                s = json.loads(json_file)
                old_password = s['vmconfig']['vmBaseInfo']["systemPassword"]
                new_str = re.sub(old_password, new_password, json_file,0)

            with open(full_path,'w') as f:
                f.write(new_str)


    def deploy_start(self):
        if self.version == 'r6':
            self.logging.info('Start to install FI ')
            self.logging.info('It takes a little time')
            os.system(config.r6_start)
            self.logging.info('The installer is running in the background,now you can close this terminal\n')
            self.logging.info('you can use\n tailf ' + os.path.join(config.SwiftInstall_path, 'SwiftDeploy','var','logs','app.log') +'\n  to check process\n')
            self.logging.info('more logs\n cd ' + os.path.join(config.SwiftInstall_path, 'SwiftDeploy','var','logs','tools','icta') + '\n')

        if self.version == 'r7':
            ret = -1
            self.logging.info('Start to install FI ')
            cmd = 'bash ' + os.path.join(config.SwiftInstall_path,'ODAEDeployTool', 'bin', 'init_root_key.sh')
            deploy_common.input_password(cmd)

            self.logging.info('start pre_check')
            p = os.system('bash ' + os.path.join(config.SwiftInstall_path,'ODAEDeployTool', 'bin', 'pre_check.sh'))
            time.sleep(180)
            try:
                with open (os.path.join(config.SwiftInstall_path, 'ODAEDeployTool', 'var', 'logs', 'check_before_install', 'report'),'r') as f:
                    h = f.read()
                    if 'ERROR' in h:
                        self.logging.info('\n' +'the datails:' + '\n' + h + '\n')
                        self.logging.info('ctrl + c to stop and check  \n  after check you can \n'+'bash ' + os.path.join(config.SwiftInstall_path, 'ODAEDeployTool', 'bin', 'deploy.sh') + '\nto deploy')
                        self.logging.info('or  wait 2 minutes to auto_deploy')
                        time.sleep(120)
                        os.system('bash ' + os.path.join(config.SwiftInstall_path,'ODAEDeployTool', 'bin', 'deploy.sh'))
                    else:
                        self.logging.info('pre_check sucess!')
                        os.system('bash ' + os.path.join(config.SwiftInstall_path,'ODAEDeployTool', 'bin', 'deploy.sh'))
            except IOError:
                self.logging.info ("file not exsit!")
                os.system('bash ' + os.path.join(config.SwiftInstall_path,'ODAEDeployTool', 'bin', 'deploy.sh'))


    def retry(self):
        if self.version == 'r7':
            self.logging.info('start retry')
            os.system('bash ' + os.path.join(config.SwiftInstall_path,'ODAEDeployTool', 'bin', 'deploy.sh retry'))
        elif self.version == 'r6':
            self.logging.info('No support')

    def configmgr_install_finish(self):
        if self.version == 'r7':
            os.system('bash ' + os.path.join(config.SwiftInstall_path,'ODAEDeployTool', 'bin', 'configmgr_install_finish.sh'))

    @property
    def get_status(self):
        status = 'default'
        return status


    @property
    def get_swiftdeploy_package(self):
        swift_zip_r6 = glob.glob(os.path.join(config.SwiftInstall_path,'SwiftDeploy-*.zip'))
        swift_zip_r7 = glob.glob(os.path.join(config.SwiftInstall_path,'ODAESwiftDeployPlugin-*.zip'))
        if swift_zip_r6:
            swift_zip = swift_zip_r6[0]
            version = 'r6'
        elif swift_zip_r7:
            swift_zip = swift_zip_r7[0]
            version = 'r7'
        return swift_zip,version


    @property
    def get_host_ip(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('1.1.1.1', 80))
            ip = s.getsockname()[0]
        finally:
            s.close()
        return ip


    @property
    def get_hostlist(self):
        datamodel_path = os.path.join(config.SwiftInstall_path, 'data_model', 'FI_u2000.json')
        try:
            with open(datamodel_path,'r') as f:
                load_dict = json.load(f)
                hostlist = []
                for i in load_dict['hostlist']:
                    ip = i['nodemgrip']
                    hostlist.append(ip)
            return hostlist
        except Exception as e:
            raise e


    @property
    def get_encrypt_root_key(self):
        ret = -1
        cmd = 'python ' + os.path.join(config.SwiftInstall_path,'SwiftDeploy','bin','encrypt_root_key.pyc')
        text =  deploy_common.input_password_and_change(cmd)
        return text

