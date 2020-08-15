import pprint
import requests
class WeatherForecast:
    def get(self, city):
        url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=19635a07009bb029f8569e0bad9be9d3"
        data = requests.get(url).json()
        forecast_data = data["weather"]
        forecast = []
        for day_data in forecast_data:
            forecast.append(
                {
                    "main": day_data["main"],
                    "desc": day_data["description"]
                }
            )
        return forecast
class CityInfo:
    def __init__(self, city, weather_forecast = None):
        self.city = city
        self._weather_forecast = weather_forecast or WeatherForecast()
    def weather_forecast(self):
        return self._weather_forecast.get(self.city)
def _main():
    city_info = CityInfo("Odessa")
    forecast = city_info.weather_forecast()
    pprint.pprint(forecast)
if __name__ == "__main__":
    _main()