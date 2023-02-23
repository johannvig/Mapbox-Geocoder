

<h1>Mapbox Reverse Geocoding</h1>


This Python script sends a request to the Mapbox API to get the addresses of locations near a given latitude and longitude. It does this by first sending a request to the Mapbox API to get the coordinates of locations near the given latitude and longitude, then sending requests to the Mapbox API to convert each set of coordinates into an address.

Installation
To run this script, you'll need Python 3.x and the following libraries:

requests
colorama
mapbox
You can install the required libraries using pip:

Copy code
pip install requests colorama mapbox
Usage
To use this script, you'll need a Mapbox API key. You can sign up for a free account at mapbox.com. Once you have an API key, run the script and enter your API key and the latitude and longitude of the location you want to find addresses for:

Copy code
python mapbox_reverse_geocoding.py
