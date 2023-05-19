#Jacob Barnes 
from urllib.request import urlopen
from http.client import responses
import json

apiKey = "oops"

def main():
    while True:
        # Ask the user for their location (zip code or city name)
        location = input("Enter zip code or city name: ")
        
        # Get weather data
        data = getWeatherData(location)

        if data is not None:
            # Display the weather information
            displayWeatherData(*data)
        
        # Run again?
        askAgain = input("Do you want to check another city/zip? (y/n): ")
        if askAgain.lower() != 'y':
            break
        
def getWeatherData(location):
    # From API docs:
    # Please note that API requests by city name, zip-codes and city id have been deprecated. 
    # Although they are still available for use, bug fixing and updates are no longer 
    # available for this functionality
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={apiKey}&units=imperial'
    try:
        response = urlopen(url)
        # Read the response and parse JSON
        data = json.loads(response.read())
        # print(data)

        # Check if the request was successful
        status_code = response.getcode()
        if status_code == 200:
            # Get weather information and return it
            name = data['name']
            description = data['weather'][0]['description']
            temperature = data['main']['temp']
            return name, description, temperature
        else:
            print(f"Failed to get weather data for {location}")
            return None        
    except Exception as e:
        print(e)

def displayWeatherData(name, description, temperature):
    # Display the weather information
    print(f"Current weather for {name}:")
    print(f"\tDescription: {description}")
    print(f"\tTemperature: {temperature}°F")

main()
