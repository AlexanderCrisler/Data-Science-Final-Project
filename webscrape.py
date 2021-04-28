import requests
import json

url = "https://www.footballdb.com/fantasy-football/index.html?pos=QB%2CRB%2CWR%2CTE&yr=2020&wk=17&rules=1"
yr = "2010"
wk = "1"

seasons = {}

for yr in range(2010, 2021):
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