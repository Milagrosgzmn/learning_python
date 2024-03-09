from pycoingecko import CoinGeckoAPI
import pandas as pd; 
cg = CoinGeckoAPI()

bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)

data = pd.DataFrame(bitcoin_data['prices'], columns=['TimeStamps', 'Price'])

data['Date'] = pd.to_datetime(data['TimeStamps'], unit='ms')

print(data)