import subprocess
from os import listdir

def  create():
        
        try:
            subprocess.call("cd ./output && ffmpeg -pattern_type glob -framerate 1/2 -i '*.jpg' -vf 'scale=w=1280:h=720:force_original_aspect_ratio=1,pad=1280:720:(ow-iw)/2:(oh-ih)/2' -vcodec libx264 video.mp4", shell=True)
        except (RuntimeError, TypeError,NameError):
            print ("Unable to create videp")
            pass
        else: 
            print("Video created")
