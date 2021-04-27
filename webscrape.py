import requests
# import json

url = f"https://www.footballdb.com/fantasy-football/index.html?pos=QB%2CRB%2CWR%2CTE&yr={yr}&wk={wk}&rules=1"

seasons = {}

for yr in range(2016, 2021):
    weeks = []
    for wk in range(1, 18):
        weeks.append(
            requests.get(
            f"https://www.footballdb.com/fantasy-football/index.html?pos=QB%2CRB%2CWR%2CTE&yr={yr}&wk={wk}&rules=1"
            ).text
        )
    seasons[str(yr)] = weeks

json_formatted_str = json.dumps(seasons, indent=4)
print(json_formatted_str)

from selenium import webdriver

requests.get(url=url)