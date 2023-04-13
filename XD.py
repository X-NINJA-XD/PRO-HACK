#coding=utf-8
import os, sys, platform
 
os.system('rm -rf pro.so')
 
try:
    if sys.argv[1]=='update':
        os.system('rm -rf pro.so')
except:
    pass
 
 
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('pro.so'):
        os.system('curl -L https://github.com/Peaky-XD/X-SERVER/blob/main/pro.cpython-311.so?raw=true -o pro.so') 
        import pro
    else:
        import pro
 
elif bit == '32bit':sys.exit()
