# 4-2【基于py3.x】如何实现可迭代对象和迭代器对象2
# http://wthrcdn.etouch.cn/weather_mini?city=北京
from collections.abc import Iterator, Iterable
import requests


class WeatherIterator(Iterator):
    def __init__(self, caties):
        self.caties = caties
        self.index = 0

    def __next__(self):
        if self.index == len(self.caties):
            raise StopIteration

        city = self.caties[self.index]
        self.index += 1
        return self.get_weather(city)

    def get_weather(self, city):
        url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + city
        r = requests.get(url)
        data = r.json()['data']['forecast'][0]
        return city, data['high'], data['low']


class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


def show(w):
    for x in w:
        print(x)


w = WeatherIterable(['北京', '上海', '广州'] * 2)

show(w)
