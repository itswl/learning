import os
import getpass


current_path = os.path.split(os.path.realpath(__file__))[0]
password = '*******'
aaa_start = 'bash {}/a/bin/silentdeploy.sh '.format(current_path)
