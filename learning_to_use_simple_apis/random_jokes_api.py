import requests
import json

import pandas as pd

r = requests.get("https://official-joke-api.appspot.com/jokes/ten")

results = json.loads(r.text)

for i, joke in enumerate(results):
    print(f"joke {i}: \n {joke['setup']} \n {joke['punchline']} \n")

""" Si quisiera convertir los resultados en una tabla: """

df = pd.DataFrame(results)

df.drop(columns=['type', 'id'], inplace=True)

print(df)