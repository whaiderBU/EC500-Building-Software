import os
import glob
import sys

##Error checking for pictures in selected folder 
os.chdir("/Users/waqarhaider/Desktop/EC500BuildingSoftware")#change to local directory
if (glob.glob("*.jpg")) == []:
    sys.exit('Error: Please carefully re-enter twitter credentials and rerun.')
