import os
import glob
import sys

#Haider
##Error checking for pictures in selected folder 

os.chdir("") #change to local folder directory
if (glob.glob("*.jpg")) == []:
    sys.exit('Error: Please carefully re-enter twitter credentials and rerun.')
