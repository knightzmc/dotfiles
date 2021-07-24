#!/usr/bin/env python

import requests
import json
import datetime
import subprocess
import os
import asyncio

lat = '50.699478'
long = '-1.293190' # Isle of Wight, UK. Change to your location

day_img = '~/dotfiles/backgrounds/day.png'
night_img = '~/dotfiles/backgrounds/night.png'





def parse_date(s):
    return datetime.datetime.strptime(s, '%I:%M:%S %p')

async def get_suntimes():
    r = requests.get(f'https://api.sunrise-sunset.org/json?lat={lat}&lng={long}')

    parsed = json.loads(r.text)["results"]
    sunset = parse_date(parsed["sunset"])
    sunrise = parse_date(parsed["sunrise"])

    return sunset, sunrise

async def run():
    sunset, sunrise = await get_suntimes()

    while True:
        now = datetime.datetime.utcnow()

        path = night_img if now > sunset else day_img

        subprocess.run(['feh', '--bg-scale', os.path.expanduser(path)])
        print(f'Set background to {path}')
        await asyncio.sleep(10)


asyncio.run(run())
