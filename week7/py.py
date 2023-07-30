import json
import sys
import requests

te = input()
response = requests.get(
"https://itunes.apple.com/search?entity=song&term=" +te)

o = response.json()
print(o)
for result in o["results"]:
    print(result["trackName"])

