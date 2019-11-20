import getpass

hostname = ''
username = ''
password = ''
port = ''

while not hostname:
    hostname = input('please input hostname:')

while not username:
    username = input('(default root) please input username：')
    if not username:
        username = 'root'

while not password:
    password = getpass.getpass('please input password:')

while not port:
    port = input('(default 22) please input port：')
    if not port:
        port = 22

port = int(port)
