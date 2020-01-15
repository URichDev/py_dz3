import pprint
import argparse

import requests

key_api = '1336ad1901ec0d4b05a62ca5e67908ec'

parser = argparse.ArgumentParser()
parser.add_argument('-1', '--city', help='This will be option City')

city = parser.parse_args().city
how_days = 3

r = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?APPID={key_api}&q={city}&units=metric')
# print(f'https://api.openweathermap.org/data/2.5/forecast?APPID={key_api}&q={city}&units=metric')

r = r.json()

if r['cod'] == "200":
    new_day = 60*60*24 #24 hours
    days = 0
    date_r = []
    for item in r["list"]:
        if days == 0:
            days = item["dt"]
            next_day = days + new_day
            date_r.append(item)
        elif item["dt"] >= next_day:
            days = item["dt"]
            next_day = days + new_day
            date_r.append(item)

    i = 0
    for x in date_r:
        if i < how_days:
            if round(x["main"]["temp"]) <= 0:
                temp = round(x["main"]["temp"])
            else:
                temp = f'+{round(x["main"]["temp"])}'
            pprint.pprint(f'{x["dt_txt"]}  {temp}   {x["weather"][0]["description"]}')
        i += 1
else:
    print ('Results 0. Try Again!')