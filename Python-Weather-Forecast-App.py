import requests
import datetime


def get_forecast(city):
    api_key = "3e9033068741b561249db0c68bcf553f"
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    if data["cod"] != "200":
        print("Error:", data["message"])
        return
    forecast = data["list"]
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    for i in range(len(forecast)):
        date_time = forecast[i]['dt_txt']
        if today in date_time:
            date = datetime.datetime.fromtimestamp(forecast[i]['dt']).strftime('%a, %b %d')
            temp_min = int(round(forecast[i]['main']['temp_min'] - 273.15, 0))
            temp_max = int(round(forecast[i]['main']['temp_max'] - 273.15, 0))
            weather = forecast[i]['weather'][0]['main']
            print(f"{date} - {temp_min} / {temp_max}°C - {weather}")
            break


city = input("Enter a city: ")
get_forecast(city)
