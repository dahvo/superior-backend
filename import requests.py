import requests
import pandas as pd
from pprint import pprint

url = "https://www.qnt.io/api/results?pID=gifgif&mID=54a309ae1c61be23aba0da62&key=54a309ac1c61be23aba0da3f"

response = requests.get(url)
results = response.json()["results"]

# pprint(results)

df = pd.DataFrame.from_dict(results)
pprint(df)