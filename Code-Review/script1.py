import subprocess
import os
import glob

#This script checks if memory infinetly gets created when running api app - error - Memory Usage failure 

os.system("python3 code.py")
os.system("python3 code.py")
os.chdir("/*") ## change to local path
if (glob.glob("(1).jpg")) == []:
    print('Memory Usage Failure')
