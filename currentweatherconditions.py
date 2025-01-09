import requests
from bs4 import BeautifulSoup

# Current Weather Conditions
# Created by Brad Voris
# Change the ZIP code to your location to display the current weather conditions from Weather.com
# This script displays weather information

zipcode = "77001"
url = f"https://weather.com/weather/today/l/{zipcode}"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract today's weather data
    weather_container = soup.find("div", {"data-testid": "CurrentConditionsContainer"})
    if weather_container:
        todays_weather = weather_container.get_text(strip=True)
        print("Today's Weather:\n")
        print("\n" + todays_weather + "\n")
    else:
        print("Unable to find today's weather information.\n")

    # Extract current forecast details
    details_container = soup.find("div", {"id": "todayDetails"})
    if details_container:
        current_forecast = details_container.get_text(strip=True)
        print("Current Forecast:\n")
        print("\n" + current_forecast + "\n")
    else:
        print("Unable to find current forecast details.\n")
else:
    print(f"Failed to retrieve data. HTTP Status Code: {response.status_code}\n")
