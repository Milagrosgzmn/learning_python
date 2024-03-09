import requests
import json
import pandas as pd

data = requests.get("https://fruityvice.com/api/fruit/all")
result = json.loads(data.text)


df2= pd.json_normalize(result) # contiene subcolumnas asi que se tiene que aplanar



cherry = df2.loc[df2['name']=='Cherry']
print(cherry.iloc[0]['family'], cherry.iloc[0]['genus'])

"""#2- In this Exercise, find out how many calories are contained in a banana. """

banana = df2.loc[df2['name']=='Banana']
banana_calories = banana.iloc[0]['nutritions.calories']

print(banana_calories)