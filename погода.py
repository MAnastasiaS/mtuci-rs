import requests  # импортируем библиотеку requests

city = 'Moscow,RU'  # запоминаем в переменную город, который нас интересует
appid = '0f5ea9af177232617fb95989c0ce97a5'  # запоминаем в переменную appid
res = requests.get("http://api.openweathermap.org/data/2.5/weather",  # отправляем запрос на сервер и получаем данные
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("скорость ветра:", data['wind']['speed'])
print("видимость:", data['visibility'])
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
for i in data['list']:
    print("скорость ветра <", i['wind']['speed'], "> \r\nвидимость <", i['visibility'], ">")
    print("____________________________")
