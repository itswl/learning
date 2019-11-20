
from contextlib import contextmanager
import paramiko
from host import *

ssh = paramiko.SSHClient()
@contextmanager
def connection():
    try:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, port, username, password)
        yield
    except Exception as e:
        raise e 
    finally:
        ssh.close()
