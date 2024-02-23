from datetime import datetime as dt
import requests

base_url_weather_api = "https://api.openweathermap.org/data/3.0/onecall?"
base_url_geocoding_api = "http://api.openweathermap.org/geo/1.0/direct?"


api_key = open('api_key.txt', 'r').read()
city_name = 'Fairfax'
state_code = "VA"
country_code = 'US'

geocoding_api_url = base_url_geocoding_api + "q=" + city_name + ',' + state_code + ',' + country_code + '&appid=' + api_key

geocoding_api_response = requests.get(geocoding_api_url).json()
print(geocoding_api_response)
# [{'name': 'Fairfax', 'local_names': {'en': 'Fairfax'}, 'lat': 38.8462236, 'lon': -77.3063733, 'country': 'US', 'state': 'Virginia'}]
lat = str(geocoding_api_response[0]['lat'])
lon = str(geocoding_api_response[0]['lon'])
weather_api_url = base_url_weather_api + 'lat=' + lat + '&lon=' + lon + "&appid=" + api_key
weather_api_response = requests.get(weather_api_url).json()
print(weather_api_response)
temp_kelvin = weather_api_response['current']['temp']
feels_like_temp_kelvin = weather_api_response['current']['feels_like']
humidity = str(weather_api_response['current']['humidity']) + '%'
clock = dt.now()
current_time = clock.strftime('%H:%M:%S')
air_pressure = weather_api_response['current']['pressure']
uv_index = weather_api_response['current']['uvi']
wind_speed = weather_api_response['current']['wind_speed']
cloud_coverage = str(weather_api_response['current']['clouds']) + '%'
visibility = weather_api_response['current']['visibility']
wind_chill_kelvin = weather_api_response['current']['wind_deg']
weather_description = weather_api_response['current']['weather'][0]['description']
current_date = dt.today()

def kelvin_to_celsius_fahrenheit(kelvin):
    celcius = kelvin - 273.15
    fahrenheit = (kelvin - 273.15) * 1.8 + 32
    return round(celcius, 2), round(fahrenheit, 2)

temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_temp_celsius, feels_like_temp_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_temp_kelvin)
wind_chill_celsius, wind_chill_fahrenheit = kelvin_to_celsius_fahrenheit(wind_chill_kelvin)
print('\n\n\n\n')
print('Date:', current_date.strftime('%m/%d/%Y'))
print('Time:', current_time)
print('Location:', city_name)
print('Description of the current weather:', weather_description)
print('Temperature in celsius:', temp_celsius, 'but it feels like:', feels_like_temp_celsius)
print('Temperature in fahrenheit:', temp_fahrenheit, 'but it feels like:', feels_like_temp_fahrenheit)
print('Humidity level:', humidity)
print('Current air pressure is:', air_pressure)
print('The current UV index is:', uv_index)
print('The current cloud coverage is:', cloud_coverage)
print('The current visibility is:', visibility)

'''def chatgpt_prompt_generator(city, kelvin, celsius, fahrenheit, feels_like_kelvin, feels_like_celsius, feels_like_fahrenheit, wind_speed, humidity, sunrise_time, sunset_time):
    prompt = (f"Write a description of a city named {city}. It is {kelvin} degrees kelvin, but feels like {feels_like_kelvin}. It is {celsius} degrees celsius, but feels like {feels_like_celsius}. It is {fahrenheit} degrees Fahrenheit, but feels like {feels_like_fahrenheit}. The current wind speed is {wind_speed}. The humidity is {humidity}%. The sunrise is {sunrise_time} and the sunset time is {sunset_time}.")
    return prompt
chatgpt_prompt_generator(city, kelvin, celsius, fahrenheit, feels_like_kelvin, feels_like_celsius, feels_like_fahrenheit, wind_speed, humidity, sunrise_time, sunset_time)'''