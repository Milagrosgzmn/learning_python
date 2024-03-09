import requests
import json

url = 'https://animechan.xyz/api/random'

data = requests.get(url)

result = json.loads(data.text)

print(f"Your quote for the day is: \n{result['character']} - '{result['quote']}'")