from logger import LOG
import time
from contextlib import contextmanager
import pexpect
from config import password

logging = LOG('install.log')
@contextmanager
def cost_time():
    start_time = time.time()
    logging.info ('start time : ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    yield
    end_time = time.time()
    seconds = end_time - start_time
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    logging.info ('end time : ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    logging.info('time cost  %d:%02d:%02d ' % (h, m, s))


def input_password_and_change(cmd):
    ssh = pexpect.spawn(cmd)
    try:
        i = ssh.expect(['[Pp]assword:'], timeout=360)
        if i == 0:
            h = ssh.sendline(password)
        ssh.sendline(password)
        r = ssh.read()
        t = r.replace(password, '')
        text = t.replace('\r\n', '')
        return text
    except pexpect.EOF:
        logging.info("EOF")
        ret = -1
    except pexpect.TIMEOUT:
        logging.info("TIMEOUT")
        ret = -2
    finally:
        ssh.close()

def input_password(cmd):
    ssh = pexpect.spawn(cmd)
    try:
        i = ssh.expect(['[Pp]assword:', 'yes/no', pexpect.EOF], timeout=360)
        if i == 0:
            ssh.sendline(password)
            ssh.expect(pexpect.EOF)
        ssh.sendline('yes\n')
        ssh.expect(pexpect.EOF)
        ssh.sendline(password)
    except pexpect.EOF:
        logging.info("EOF")
        ret = -1
    except pexpect.TIMEOUT:
        logging.info("TIMEOUT")
        ret = -2
