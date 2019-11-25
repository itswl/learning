import subprocess
import os
with open('/home/weilai/Desktop/password.md','r') as f:
    s = f.read()
    password = s
    print(password)
p = subprocess.Popen('python /home/weilai/Desktop/a.py',shell =True, stdout=subprocess.PIPE,stdin=subprocess.PIPE)
p.stdin.write(password)
h = p.stdout.read()
print(h)
