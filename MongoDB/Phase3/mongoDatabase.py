from pymongo import MongoClient
from os import listdir
import subprocess

# function to connect to Mongodb initialize and update database
def InitializeMongo():
    client = MongoClient('localhost:27017')
    db = client.Tweet
    
def updateMongo(query, field, value):
    client = MongoClient('localhost:27017')
    db = client.Tweet
    updateValue = {field:value}
    db.Tweet.update_one(query, updateValue)
       
def insertMongo(handler, date, data, imageCount):
    client = MongoClient('localhost:27017')
    db = client.Tweet
    post = {"handler" : handler,
            "date" : date,
            "labels" : data,
            "imageCount" : imageCount        
    }
    db.tweet.insert_one(post)
