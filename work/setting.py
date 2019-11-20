import os
import getpass

hostname = ''
port = None
password = ''
username = ''
remote_dir = ''
local_dir = os.path.join(os.getcwd(),'new')

while not hostname:
    hostname = input('please input hostname:')

while not username:
    username = input('( default root )please input username:')
    if not username:
        username = 'root'

while not password:
    password = getpass.getpass('please input password:')

while not port:
    port = input('( default 22 )please input port:')
    if not port:
        port = 22
    port = int(port)

while not remote_dir:
    remote_dir = input('( default /opt/TestInstall/ )please input remote:')
    if not remote_dir:
        remote_dir = '/opt/new/'
