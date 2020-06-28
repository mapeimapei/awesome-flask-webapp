#4-2【基于py3.x】如何实现可迭代对象和迭代器对象2
#http://wthrcdn.etouch.cn/weather_mini?city=北京
from collections.abc import Iterator, Iterable
import requests

url ='http://wthrcdn.etouch.cn/weather_mini?city='+'北京'
r = requests.get(url)
print(r.text)
print(r.json()['data']['city'])