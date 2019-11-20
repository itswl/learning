import os
import time
import threading
import sys
import time 
import logging
import config

current_path = config.current_path

logging.basicConfig(level="INFO",
                    format="[%(asctime)s] [%(levelname)8s] [%(process)d-%(thread)d] %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    filename=os.path.join(current_path, "install.log"),
                    filemode='a')

class Deploy(threading.Thread):
    def run(self):
        os.system('python ' + os.path.join(current_path, 'deploy.py')+ ' start')
        return 0


if __name__ == '__main__':
    cmd = sys.argv[1]
    count = 0

    if cmd == 'stop':
        current_pid =str(os.getpid())
        pids = os.popen("ps -ef | grep auto_deploy.py| awk '{print $2}'")
        pids = pids.read().replace(current_pid,'')
        pids = pids.split()
        for pid in pids:
            os.system('kill -9 '+ pid )

    elif cmd =='start':
        while True:
            logging.info('_' * 30)
            logging.info("start to deploy ")
            fi_deploy = Deploy()
            fi_deploy.start()
            is_success = 0
            time.sleep(300)

            while True:
                log_file = open(os.path.join(current_path,'a/var/logs/app.log'))
                log_file.seek(-5000, 2)
                log_content = log_file.readlines()
                if *****' in str(log_content):
                    is_success = 0
                    logging.error("install failed")
                    break

                elif '*****' in str(log_content):  # sucess
                    is_success = 1
                    count += 1
                    logging.info("install sucess!  " + str(count))
                    break
                    
                time.sleep(120)
                logging.info('still Deploy')

            if not is_success:  # failed
                logging.info('Deploy Failed')
                break

            logging.info('start to uninstall  1 hour')
            time.sleep(3600)
            os.system('python ' + os.path.join(current_path, 'deploy.py') + ' uninstall')
            logging.info('uninstall  success')


