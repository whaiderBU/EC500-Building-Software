# Phase 2
# Waqar Haider 
# Task: Design database to implement persistent user stories

import re
import tweepy
import wget
import urllib 
import os
import requests
import io
from google.cloud import vision
from google.cloud.vision import types
import tweepy  # https://github.com/tweepy/tweepy
import subprocess
import json
import re
import glob
import datetime
from pymongo import MongoClient
from os import listdir
from pickle import FALSE
from symbol import except_clause
from os import listdir
#app = Flask(__name__)


#Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""
##Define arguments
def parse_arguments():
  parser = argparse.ArgumentParser(description='Download pictures from a Twitter feed.')
  parser.add_argument('username', type=str, help='The twitter screen name from the account we want to retrieve all the pictures')
  parser.add_argument('--num', type=int, default=5, help='Maximum number of tweets to be returned.') # 4 images outputed
  parser.add_argument('--retweets', default=False, action='store_true', help='Include retweets')
  parser.add_argument('--output', default='', type=str, help='folder where the pictures will be stored') ## change to local path

  args = parser.parse_args()
  return args

##Define config.
def parse_config(config_file):
  config = configparser.ConfigParser()
  config.read(config_file)  
  return config 

##Define parser  
@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status

##Initialise tweepy
def init_tweepy():
  # Status() is the data model for a tweet
  tweepy.models.Status.first_parse = tweepy.models.Status.parse
  tweepy.models.Status.parse = parse
  # User() is the data model for a user profil
  tweepy.models.User.first_parse = tweepy.models.User.parse
  tweepy.models.User.parse = parse

##Authorise twitter API
def authorise_twitter_api(config):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    return auth

##Download images from twitter
def download_images(api, username, retweets,  num_tweets, output_folder):
  tweets = api.user_timeline(screen_name=username, count=200, include_rts=retweets)
  if not os.path.exists(output_folder):
      os.makedirs(output_folder)

  downloaded = 0
  while (len(tweets) != 0):    
    last_id = tweets[-1].id
    
    for status in tweets:
      media = status.entities.get('media', []) 
      if(len(media) > 0 and downloaded < num_tweets):
        wget.download(media[0]['media_url'], out=output_folder)
        downloaded += 1        

    tweets = api.user_timeline(screen_name=username, count=200, include_rts=retweets,  max_id=last_id-1)

##Rename photo by num for ffmpeg
def order():
    i=1
    path="" ## change to local path

    for filename in os.listdir(path):
        if filename.endswith(".jpg"):
            os.rename(path + "/" + filename, path + "/" + str(i) + ".jpg")
            i+=1

##Error checking for pictures in selected folder 
def checkError():
    os.chdir("") ## change to local path
    if (glob.glob("*.jpg")) == []:
        sys.exit('Error: Please carefully re-enter twitter credentials and rerun.')

  
##ffmpeg tool for video creation
def video():
    subprocess.call('ffmpeg -r .5 -f image2 -s 1920x1080 -i %d.jpg -vcodec libx264 -crf 20  -pix_fmt yuv420p test.mp4', shell=True)
    print('\n\nVideo created.')

def createLabels():
    client = vision.ImageAnnotatorClient()

    # create file 
    f1 = open('new.txt','w+') 
    f1.write('Labels:')

    # The name of the image file to annotate
    directory =  ""  ## change to local path
    #for i in range(1,n):
    for filename in os.listdir(directory): 
            if filename.endswith(".jpg"):
                file_name = filename 
                # Loads the image into memory 
                with io.open(file_name, 'rb') as image_file:
                    content = image_file.read()

                image = types.Image(content=content)

                # Performs label detection on the image file
                response = client.label_detection(image=image)
                labels = response.label_annotations

                
                for label in labels:
                    f1.write('\n')  
                    f1.write(label.description)
                    #labels created in new.txt
                
    f1.close()
    insertMongo("foodandwine", datetime.datetime.now(), labelData, len(pictures))
    
# function to connect to Mongodba nd update the database
def InitializeMongo():
    client = MongoClient('localhost:27017')
    db = client.TwitterFeed
    
def updateMongo(query, field, value):
    client = MongoClient('localhost:27017')
    db = client.TwitterFeed
    updateValue = {field:value}
    db.TwitterFeeds.update_one(query, updateValue)
       
def insertMongo(handler, date, data, imageCount):
    client = MongoClient('localhost:27017')
    db = client.TwitterFeed
    post = {"handler" : handler,
            "date" : date,
            "labels" : data,
            "imageCount" : imageCount        
    }
    db.TwitterFeed.insert_one(post)


def main():    
  arguments = parse_arguments() 
  username = arguments.username
  retweets = arguments.retweets
  num_tweets = arguments.num
  output_folder = arguments.output
  config = parse_config('../config.cfg')
  auth = authorise_twitter_api(config)   
  api = tweepy.API(auth)
  download_images(api, username, retweets, num_tweets, output_folder) 
  order()
  checkError()
  video()
  createLabels()
  InitializeMongo()
  updateMongo(query, field, value)
  insertMongo(handler, date, data, imageCount)

if __name__=='__main__':
    main()
