
import os
import sys
import glob


class Third():

    def __init__(self):
        self.files = self.get_tar_gz

    @property
    def get_tar_gz(self):
        files = glob.glob(os.path.join(current_path, '*.tar.gz'))
        return files


    def install(self):
        for file_full_path in self.files:
            file = os.path.split(file_full_path)
            file_name = file[1]
            file_name_prefix = file_name.replace('.tar.gz','')
            os.system('tar zxvf  '+ file_full_path + ' --warning=no-timestamp  ' + ' -C {} >/dev/null'.format(current_path))
            os.chdir(os.path.join(current_path, '{}'.format(file_name_prefix)))
            os.system('python setup.py install --record install.txt &> /dev/null')


    def uninstall(self):
        for file in self.files:
            file = os.path.split(file)
            file_name = file[1]
            file_name_prefix = file_name.replace('.tar.gz','')
            os.chdir(os.path.join(current_path,  '{}'.format(file_name_prefix)))
            os.system('cat install.txt | xargs rm -rf')
            os.system('rm -rf ' + os.path.join(current_path, '{}').format(file_name_prefix))


def main():
    cmd = sys.argv[1]
    if cmd == 'install':
        third.install()
    elif cmd =='uninstall':
        third.uninstall()


if __name__ == '__main__':
    current_path = os.path.split(os.path.realpath(__file__))[0]
    third = Third()
    main()
