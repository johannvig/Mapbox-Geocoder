import requests.auth
import warnings
from colorama import Fore
from mapbox import Geocoder
warnings.filterwarnings('ignore')


token=input("Write here your mapbox API")
latitude=input("What is the latitude of your location?")
longitude=input("What is the longitude of your location?")

#send a requests to the mapbox API to get multiple addresses close to the starting location
w = requests.get("https://api.mapbox.com/v4/mapbox.mapbox-streets-v8/tilequery/"+longitude+","+latitude+".json?radius=1000&limit=50&geometry=polygon&access_token="+token)


a=0
try:
  while True:
    #cleaning the request response to have only coordinates
    response = w.json()['features'][a]['geometry']['coordinates']

    mot1 = str(response).replace('[', ' ')
    mot2 = str(mot1).replace(']', ' ')
    
    #separate longitude and latitude
    séparer = str(mot2).split(',')

    longitude_x=séparer[0]
    latitude_y=séparer[1]


    #convert coordinates into addresses
    geocoder = Geocoder(access_token=token)
    response = geocoder.reverse(lon=longitude_x, lat=latitude_y, types=['address'])

    #cleaning the request response to have only addresses
    data = response.json()['features'][0]['place_name']
    print(data)


    a+=1

except Exception as e:
        print(Fore.RED + "Ohoh! Something went wrong!")
        print(e)
