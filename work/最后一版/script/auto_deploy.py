import os
import time
import threading
import sys
from logger import LOG
import config



class Auto_Deploy(threading.Thread):

    def log(self):
        self.logging = LOG('auto_install.log')

    def run(self):

        print('python ' + os.path.join(config.SwiftInstall_path,'script', 'run.py')+ ' install')
        os.system('python ' + os.path.join(config.SwiftInstall_path,'script', 'run.py')+ ' install')
        return 0

    def stop(self):
        current_pid =str(os.getpid())
        pids = os.popen("ps -ef | grep auto_deploy.py| awk '{print $2}'")
        pids = pids.read().replace(current_pid,'')
        pids = pids.split()
        for pid in pids:
            os.system('kill -9 '+ pid + ' 2>> /dev/null')


if __name__ == '__main__':
    cmd = sys.argv[1]
    count = 0
    auto_deploy = Auto_Deploy()
    auto_deploy.log()

    if cmd == 'stop':
        auto_deploy.stop()

    elif cmd =='start':
        auto_deploy.stop()
        while True:
            auto_deploy.logging.info('_' * 30)
            auto_deploy.logging.info("start to deploy FI")
            auto_deploy.start()
            is_success = 0
            time.sleep(60)

            while True:
                log_file = open(os.path.join(config.SwiftInstall_path,'SwiftDeploy/var/logs/app.log'))
                log_file.seek(-5000, 2)
                log_content = log_file.readlines()
                if 'execute job shedule failed' in str(log_content):
                    is_success = 0
                    auto_deploy.logging.error("install failed")
                    break

                elif 'execute job shedule suceess.Install_FIConf' in str(log_content):  # sucess
                    is_success = 1
                    count += 1
                    auto_deploy.logging.info("install sucess!  " + str(count))
                    break

                time.sleep(60)
                auto_deploy.logging.info('still Deploy')

            if not is_success:  # failed
                auto_deploy.logging.error('FI Deploy Failed')
                break

            auto_deploy.logging.info('start to uninstall FI 1 hour')
            time.sleep(3600)
            os.system('python ' + os.path.join(config.SwiftInstall_path, 'script', 'run.py') + ' uninstall')
            auto_deploy.logging.info('uninstall FI success')

