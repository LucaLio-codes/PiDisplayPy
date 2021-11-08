import requests
import json
from datetime import datetime, timezone, timedelta
import pathlib

CITY = 'Darmstadt'
KEY = '381eac8a97bebb8bce2b2a392d7b8f2f'
PROJECT_PATH = str(pathlib.Path(__file__).parent)
CALL = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={KEY}'

def getdir():
    response = requests.get(CALL)
    json_string = response.text
    result = json.loads(json_string)
    icon = result['weather'][0]['icon']
    temp = result["main"]['temp']-273.15
    feel = result["main"]['feels_like']-273.15
    max_t = result["main"]['temp_max']-273.15
    min_t = result["main"]['temp_min']-273.15
    set_t = int(result['sys']['sunset'])
    rise_t = int(result['sys']['sunrise'])
    set_t = datetime.fromtimestamp(set_t).strftime('%H:%M')
    rise_t = datetime.fromtimestamp(rise_t).strftime('%H:%M')
    temp = round(temp, 1)
    feel = round(feel)
    max_t = round(max_t)
    min_t = round(min_t)
    descr = result['weather'][0]['description']
    url = f'http://openweathermap.org/img/wn/{icon}@2x.png'
    img_response = requests.get(url)
    with open(PROJECT_PATH + '/tmp.png', 'wb') as f:
        f.write(img_response.content)
    return PROJECT_PATH+'/tmp.png', temp, feel, max_t, min_t, set_t, rise_t, descr

if __name__ == '__main__':
    getdir()