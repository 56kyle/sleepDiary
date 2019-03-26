import json
from datetime import datetime

times = {}

file = open('/home/kyle/Desktop/Takeout/Chrome/BrowserHistory.json')
x = json.loads(file.read())

for i in x['Browser History']:
    if int(i['time_usec']) > 1551312000000000:
        time = datetime.utcfromtimestamp(i['time_usec']/1000000)
        times[i['url']] = time


for j in times:
    past = times[j].timestamp()
