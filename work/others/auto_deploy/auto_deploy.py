# 伪代码
# 一直安装卸载，直到安装失败，退出运行
# 成功就一直循环，不成功就跳出，还在运行中logging.info('still install')
import logging
import os
import time
import threading

current_path = os.getcwd()
class Deploy(threading.Thread):
    def run(self):
        os.system('python ' + os.path.join(current_path, 'deploy.py'))

if __name__ == '__main__':
    logging.basicConfig(level="INFO",
                        format="[%(asctime)s] [%(levelname)8s] [%(process)d-%(thread)d] %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S",
                        filename=os.path.join(os.path.dirname(__file__), "install.log"),
                        filemode='a')

    while True:
        logging.info('_' * 30)
        logging.info("start to install")
        fi_deploy = Deploy()
        fi_deploy.start()
        is_success = 0  # 默认失败
        time.sleep(60)

        while True:
            if "eds" in str('asle1eds'):  # 不成功
                is_success = 0
                logging.error("install failed")
                break
            elif "es" in str('leasasf'):  # 成功
                is_success = 1
                logging.info("install sucess!")
                break
            time.sleep(60)
            logging.info('still install')

        if not is_success:  # 不成功
            print(' Failed')
            break

        logging.info('start to uninstall 1 hour')
        time.sleep(3600)
