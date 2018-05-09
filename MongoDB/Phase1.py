# Phase 1
# Waqar Haider 
# Task  : Write a python program to import the airport location data
# Demonstrate the following functions
# Read data
# Update data
# Search and find data


import json
import os
import numpy as np
from pymongo import MongoClient

def Initialize():
client = MongoClient('localhost', 27017)
db = client['airport-database']

 fname = open("airports.json", 'r')
    data = json.load(fname.read())
    client = MongoClient('localhost:27017')
    db = client.Airports
    db.Airports.insert_many(data)

# function to add new airports
def Insert(code, lat, lon, name, city, state, country, woeid, tz, phone, email, url, runwayLen, elev, icao, directFlights, carriers):
    try:
        
    client = MongoClient()
    db = client.Airports
    airport = {
    			"code": code,
             "lat": lat,
             "lon": lon,
             "name": name,
             "city": city,
             "state": state,
             "country": country,
             "woeid": woeid,
             "tz": tz,
             "phone": phone,
             "email": email,
             "url": url,
             "runway_length": runwayLen,
             "elev": elev,
             "icao": icao,
             "direct_flights": directFlights,
             "carriers": carriers
             }
    
    db.Airports.insert(airport)
    
    except Exception, e:
        print str(e)
    
# function to update   
 def Update(query, field, value):
        try:
        
        client = MongoClient()
        db = client.Airports
        updateValue = {field:value}
        db.Airports.update_one(query, updateValue)
        
        except Exception, e:
            print str(e)
    
# function to update   
 def Search(query, projection):
    try:
        
    client = MongoClient()
    db = client.airports
    result = db.Airports.find({query: projection})

    print("The results for your search are: \n")
    for item in result:
        print(result)
        
    except Exception, e:
        print str(e)

#MAIN 
def main():

with open('airports.json') as data_file:
    data = json.load(data_file)

    for index, value in enumerate(data):  # iterate through the json document
        posts = db.posts
        post_data = {

            "code": data[index]['code'],
            "lat": data[index]['lat'],
            "lon": data[index]['lon'],
            "name": data[index]['name'],
            "city": data[index]['city'],
            "state": data[index]['state'],
            "country": data[index]['country'],
            "woeid": data[index]['woeid'],
            "tz": data[index]['tz'],
            "phone": data[index]['phone'],
            "type": data[index]['type'],
            "email": data[index]['email'],
            "url": data[index]['url'],
            "runway_length": data[index]['runway_length'],
            "elev": data[index]['elev'],
            "direct_flights": data[index]['direct_flights'],
            "icao": data[index]['icao'],
            "carriers": data[index]['carriers']
        }
        
        result = posts.insert_one(post_data)
        print("successful " + str(index))





