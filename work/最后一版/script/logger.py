#-*- coding: UTF-8 -*-  

# 日志，输出到屏幕和日志中
 
import logging.handlers
import os 
import config

class LOG(logging.Logger):
    def __init__(self, filename=None):
        super(LOG, self).__init__(self)

        if filename is None:
            filename = 'install.log'
        if not os.path.exists(os.path.join(config.SwiftInstall_path,'logs')):
            os.makedirs(os.path.join(config.SwiftInstall_path,'logs'), 0o700)
        self.filename = os.path.join(config.SwiftInstall_path,'logs',filename)


        fh = logging.handlers.TimedRotatingFileHandler(self.filename, 'D', 1, 30)
        fh.suffix = "%Y%m%d-%H%M.log"
        fh.setLevel(logging.DEBUG) 


        ch = logging.StreamHandler() 
        ch.setLevel(logging.DEBUG) 


        formatter = logging.Formatter("[%(asctime)s] [%(levelname)8s]  %(message)s")
        fh.setFormatter(formatter) 
        ch.setFormatter(formatter) 


        self.addHandler(fh) 
        self.addHandler(ch) 

if __name__ == '__main__':
    pass
