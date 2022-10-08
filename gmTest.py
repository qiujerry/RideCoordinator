#!/usr/bin/env python3
import gmaps

apikey = ""
with open('gapi.txt') as f:
    apikey = f.readline()
    f.close

gmaps.configure(api_key=apikey)

new_york_coordinates = (40.75, -74.00)
gmaps.figure(center=new_york_coordinates, zoom_level=12)