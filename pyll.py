import json
import urllib.request
import time

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())    


 
con = True

while con:
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read()) 
    location = result["iss_position"]
    lat = location["latitude"]
    lon = location["longitude"]
    print(lat + " latitud")
    print(lon + " longitud")

