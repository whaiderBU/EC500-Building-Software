import subprocess
import os
from code import consumer_key

#This script sees if the user is protect from stolen consumer secrets
f=open('/*', 'r')  

for line in f:
    if consumer_key == "":
        print('Safety Risk')
        break 
    else : 
        print('Script Pass')
        break
f.close()

