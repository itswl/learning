import os
current_path = os.getcwd()

with open(os.path.join(current_path,password.md),'r') as f:
    s = f.read()
    password = s
p = os.popen('python3' +os.path.join(current_path,a.py), 'w')
p.write(password)
