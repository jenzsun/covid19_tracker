""" Track cases of COVID19 in California and USA in total through a line graph.
    Source: https://covidtracking.com/data/api
"""
import requests
import json
from datetime import datetime

from plotly.graph_objs import Scatter
from plotly import offline

# Make an API call and store the response.
url = 'https://api.covidtracking.com/v1/states/ca/daily.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process results.
cali_dicts = r.json()
case_dicts = cali_dicts[:]
cali_dates, cali_positive = [], []
for cali_dict in cali_dicts:
    current_date = datetime.strptime(str(cali_dict['date']), '%Y%m%d')
    cali_date = current_date
    cali_pos = cali_dict['positiveIncrease']
    cali_dates.append(cali_date)
    cali_positive.append(cali_pos)

url = 'https://api.covidtracking.com/v1/us/daily.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

usa_dicts = r.json()
usa_case_dicts = usa_dicts[:]
usa_positive = []
for usa_dict in usa_dicts:
    usa_pos = usa_dict['positiveIncrease']
    usa_positive.append(usa_pos)

# Make visualization.
data = [{
    'type': 'scatter',
    'x': cali_dates,
    'y': cali_positive,
    'line': {'color': 'red'},
    'opacity': 0.6,
    'name': 'California',
    },
    {
    'type': 'scatter',
    'x': cali_dates,
    'y': usa_positive,
    'line': {'color': 'blue'},
    'opacity': 0.6,
    'name': 'USA',
    },
]

my_layout = {
    'title': 'California vs. USA COVID-19 Cases Rate of Change',
    'titlefont': {'size': 28},
    'template': 'simple_white',
    'xaxis': {
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Positive Cases Rate of Change',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='ca_covid19.html')
