import json
import requests

url = "http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&api_key=09d2e9996582ffb1cc444a438b09bdf9&format=json"
data = requests.get(url).text
data = json.loads(data)
print type(data)
print data['topartists']['artist'][0]['name']