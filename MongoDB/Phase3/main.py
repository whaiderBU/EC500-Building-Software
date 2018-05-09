# Phase 3
# Waqar 
# Task: Develop scripts to run your new system (combined project 1 + Database project)
# with at least 20 twitter handles for at least 3 consecutive days 
# (I don’t want you to go over your free Google Vision API limits)

import tweet as tw
import mov as movie
import mongoDatabase as db
import googleVision as ggl
import wget
import os
import shutil
import datetime
import tweepy
import glob
import requests
from pymongo import MongoClient
from google.cloud import vision
from google.cloud.vision import type



def main():  

imgLabels = []

     Handles = ["katyperry", "justinbieber", "barackobama",
                  "rihanna", "narendramodi", "ladygaga",
                  "JLo", "wizkhalifa", "Youtube",
                  "jtimberlake", "twitter", "nytimes","KimKardashian",
                  "shakira", "ddlovato", "Oprah", "ddlovato",
                  "KevinHart4real", "MileyCyrus", "Drake", "foodandwine"]
    
    for handle in Handles:
        imgLabels[:] = []

        #make the output file
        output = "./output" 
        if os.path.exists(output):
            shutil.rmtree(output)
        if not os.path.exists(output):
            os.mkdir(output)

        try:
            imageCount = tw.get_all_tweets(handle, output) #from import tw 
            if (imageCount >= 1):
                imgLabels.append(ggl.lable_images())
                movie.mov()
                db.insertMongo(handle, datetime.datetime.now(), imgLabels, imageCount)
            else:
                print("Incorrect username")
        except Exception as e:
            print(str(e))
        else:
            print("Program successful")
            
if __name__ == '__main__':
    main()
