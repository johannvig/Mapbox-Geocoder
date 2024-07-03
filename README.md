# Mapbox Geocoder Web Application

This project is a simple web application that uses the Mapbox API to get addresses from coordinates (latitude and longitude). Originally written in Python, this project has been transformed into a web-based application using HTML, CSS and JavaScript.

## Features

- Input your Mapbox API key, latitude, and longitude to retrieve a list of nearby addresses.
- Display the addresses in a scrollable list.
- Click on any address to open a map pointing to that location.
- Automatically remove duplicate addresses from the list.

## Installation

To set up and run this project locally, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/johannvig/mapbox-geocoder-web.git
    ```

2. **Navigate to the project directory**:
    ```sh
    cd mapbox-geocoder-web
    ```

3. **Open the `index.html` file in your web browser**:
    You can do this by simply double-clicking the `index.html` file or by running a local web server.

## Usage

1. **Enter your Mapbox API key**: You can get an API key by signing up on the [Mapbox website](https://www.mapbox.com/).
2. **Enter the latitude and longitude** of your desired location.
3. **Click the "Get Addresses" button** to retrieve the addresses.
4. **Scroll through the list** of addresses if it exceeds the screen height.
5. **Click on any address** to open a map in a new tab pointing to that location.

## Project Structure

- `index.html`: The main HTML file containing the structure of the web page.
- `styles.css`: The CSS file for styling the web page.
- `scripts.js`: The JavaScript file containing the logic for fetching data from the Mapbox API and handling user interactions.


![image](https://github.com/johannvig/geocoding-address-generator/assets/102874093/72af8f86-9367-484f-a7a8-fe977a9f2553)
![image](https://github.com/johannvig/geocoding-address-generator/assets/102874093/a7ea9255-c8b9-475a-9ba3-85496b95b3fc)
![image](https://github.com/johannvig/geocoding-address-generator/assets/102874093/1fa414cd-2ae2-4894-9dd5-ad7c993613a2)
