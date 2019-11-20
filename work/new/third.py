
# 
import os
import sys


class Third():


    def install(self):
        os.system('tar zxvf {}/third/ptyprocess-0.6.0.tar.gz -C {}/third/ >/dev/null'.format(current_path,current_path))
        os.chdir('{}/third/ptyprocess-0.6.0/'.format(current_path))
        os.system('python setup.py install --record install.txt >/dev/null')
        os.system('tar zxvf {}/third/pexpect-4.6.0.tar.gz -C {}/third/ >/dev/null'.format(current_path, current_path))
        os.chdir('{}/third/pexpect-4.6.0/'.format(current_path))
        os.system('python setup.py install --record install.txt >/dev/null')
        print('you can ignore warning')


    def uninstall(self):
        os.chdir('{}/third/ptyprocess-0.6.0/'.format(current_path))
        os.system('cat install.txt | xargs rm -rf')
        os.system('rm -rf {}/third/ptyprocess-0.6.0/'.format(current_path))
        os.chdir('{}/third/pexpect-4.6.0/'.format(current_path))
        os.system('cat install.txt | xargs rm -rf')
        os.system('rm -rf {}/third/pexpect-4.6.0'.format(current_path))


if __name__ == '__main__':
    current_path = os.path.split(os.path.realpath(__file__))[0]
    cmd = sys.argv[1]
    third = Third()
    if cmd == 'install':
        third.install()
    elif cmd =='uninstall':
        third.uninstall()
