import pexpect
import os
current_path = os.getcwd()
def sshCmd(cmd):
    password ='123'
    ret = -1
    ssh = pexpect.spawn(cmd +' > pawword')
    try:
        i = ssh.expect(['password:'], timeout=5)
        if i == 0:
            h = ssh.sendline(cmd)
        ssh.sendline(password)
        r = ssh.read()
        print(r)

    except pexpect.EOF:
        print "EOF"
        ret = -1
    except pexpect.TIMEOUT:
        print "TIMEOUT"
        ret = -2
    finally:
        ssh.close()
    return ret

sshCmd('python os.path.join(current_path,'a.py')')
