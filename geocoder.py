import requests.auth
import warnings
from colorama import Fore
from mapbox import Geocoder

warnings.filterwarnings('ignore')


def get_coordinates(longitude, latitude, token):
    """
    This function sends a requests to the Mapbox API to get multiple addresses close to the starting location.
    It returns a list of coordinates as strings.
    """
    url = f"https://api.mapbox.com/v4/mapbox.mapbox-streets-v8/tilequery/{longitude},{latitude}.json?radius=1000&limit=50&geometry=polygon&access_token={token}"
    response = requests.get(url)
    response.raise_for_status()
    coordinates = []
    for feature in response.json()['features']:
        coordinates.append(str(feature['geometry']['coordinates']).replace('[', '').replace(']', ''))
    return coordinates


def get_address(longitude, latitude, token):
    """
    This function converts coordinates into addresses.
    It returns a list of addresses as strings.
    """
    geocoder = Geocoder(access_token=token)
    response = geocoder.reverse(lon=longitude, lat=latitude, types=['address'])
    response.raise_for_status()
    return response.json()['features'][0]['place_name']


if __name__ == "__main__":
    token = input("Write here your Mapbox API key: ")
    latitude = input("What is the latitude of your location? ")
    longitude = input("What is the longitude of your location? ")
    try:
        coordinates = get_coordinates(longitude, latitude, token)
        for coordinate in coordinates:
            longitude_x, latitude_y = coordinate.split(',')
            address = get_address(longitude_x, latitude_y, token)
            print(address)
    except Exception as e:
        print(Fore.RED + "Ohoh! Something went wrong!")
        print(e)
