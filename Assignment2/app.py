import requests


API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"


def get_weather_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("error in fetch.")
        return None


def get_temperature(weather_data, date_time):
    for item in weather_data['list']:
        if item['dt_txt'] == date_time:
            return item['main']['temp']
    return None


def get_wind_speed(weather_data, date_time):
    for item in weather_data['list']:
        if item['dt_txt'] == date_time:
            return item['wind']['speed']
    return None


def get_pressure(weather_data, date_time):
    for item in weather_data['list']:
        if item['dt_txt'] == date_time:
            return item['main']['pressure']
    return None


if __name__ == "__main__":
    weather_data = get_weather_data()
    
    if weather_data:
        while True:
            print("\nPress any 0Options:")
            
            print("1.Get The Temperature in k")
            print("2.Get Wind Speed")
            print("3.Get Pressure")
            print("0.Exit")
            
            option = input("enter an answer:")
            
            if option == "1":
                date_time = input("Enter date (YYYY-MM-DD HH:MM:SS):")
                temperature = get_temperature(weather_data, date_time)
                if temperature is not None:
                    print(f"\nTemperature = {temperature} k")
                else:
                    print("Data not found")
            elif option == "2":
                date_time = input("Enter date (YYYY-MM-DD HH:MM:SS):")
                wind_speed = get_wind_speed(weather_data, date_time)
                if wind_speed is not None:
                    print(f"\nWind Speed =  {wind_speed} m/s")
                else:
                    print("Data not found")
            elif option == "3":
                date_time = input("Enter date (YYYY-MM-DD HH:MM:SS):")
                pressure = get_pressure(weather_data, date_time)
                if pressure is not None:
                    print(f"\nPressure = {pressure} Pa")
                else:
                    print("Data not found")
            elif option == "0":
                break
            else:
                print("Invalid input")
