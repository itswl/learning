# 配置文件

import os
import crypt
import re
import getpass
import json

script_path = os.path.split(os.path.realpath(__file__))[0]
SwiftInstall_path =os.path.abspath(os.path.join(script_path, os.path.pardir))

r6_start = 'bash {}/SwiftDeploy/bin/silentdeploy.sh admin Changeme_123'.format(SwiftInstall_path)

p = os.popen('cat /etc/shadow|grep root')
shadow_rootline = p.read()
_password = shadow_rootline.split(':')[1]


try:
    with open(os.path.join(script_path, 'password.json')) as f:
        load_dict = json.load(f)
        password = load_dict["password"]
except:
    password = 'Changeme_123'

salt = re.findall('\$[\s\S]*?\$[\s\S]*?\$',_password)[0]
crypt_password = crypt.crypt(password,salt)


while crypt_password != _password:
    password = getpass.getpass('password:')
    crypt_password = crypt.crypt(password,salt)
