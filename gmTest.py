#!/usr/bin/env python3
import gmaps
import time
import requests
import matplotlib.pyplot as plt

apikey = ""
with open('gapi.txt') as f:
    apikey = f.readline().strip()
    f.close()

url = "https://maps.googleapis.com/maps/api/staticmap?"


center = "Columbus"
  
# zoom defines the zoom
# level of the map
zoom = 10
  
# get method of requests module
# return response object
r = requests.get(url + "&center=" + center + "&zoom=" +str(zoom) + "&size=400x400&key=" +apikey + "sensor=false")
  
# wb mode is stand for write binary mode
f = open('test.bmp', 'wb')
  
# r.content gives content,
# in this case gives image
f.write(r.content)
  
# close method of file object
# save and close the file
f.close()


gmaps.configure(api_key=apikey)

new_york_coordinates = (40.75, -74.00)
gmaps.figure(center=new_york_coordinates, zoom_level=12)



#time.sleep(5)