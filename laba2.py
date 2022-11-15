import requests

city = 'Moscow,RU'
appid = '8e6b778ff89badef894e189fd0a2a565'
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print('Дата:', i['dt_txt'],
          '\nТемпература:', i['main']['temp'], '°C'
          '\nПогодные условия:', i['weather'][0]['description'],
          '\nСкорость ветра:', i['wind']['speed'], 'м/с'
          '\nВидимость:', i['visibility'], 'метров')
    print('____________________________')
