

<h1>Mapbox Reverse Geocoding</h1>


This Python script sends a request to the Mapbox API to get the addresses of locations near a given latitude and longitude. It does this by first sending a request to the Mapbox API to get the coordinates of locations near the given latitude and longitude, then sending requests to the Mapbox API to convert each set of coordinates into an address.

Installation

To run this script, you'll need Python 3.x and the following libraries:

requests
colorama
mapbox


You can install the required libraries using pip:

pip install requests colorama mapbox

Usage


To use this script, you'll need a Mapbox API key. You can sign up for a free account at mapbox.com. Once you have an API key, run the script and enter your API key and the latitude and longitude of the location you want to find addresses for:

python mapbox_reverse_geocoding.py


![image](https://github.com/johannvig/geocoding-address-generator/assets/102874093/72af8f86-9367-484f-a7a8-fe977a9f2553)
![image](https://github.com/johannvig/geocoding-address-generator/assets/102874093/a7ea9255-c8b9-475a-9ba3-85496b95b3fc)
![image](https://github.com/johannvig/geocoding-address-generator/assets/102874093/1fa414cd-2ae2-4894-9dd5-ad7c993613a2)
