""" Track cases of COVID19 in California.
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
    cali_pos = cali_dict['positive']
    cali_dates.append(cali_date)
    cali_positive.append(cali_pos)

# Make visualization.
data = [{
    'type': 'scatter',
    'x': cali_dates,
    'y': cali_positive,
    'line': {'color': 'red'},
    'opacity': 0.6,
}]

my_layout = {
    'title': 'California COVID19 Cases',
    'titlefont': {'size': 28},
    'template': 'simple_white',
    'xaxis': {
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Positive Cases',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },

}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='ca_covid19.html')
