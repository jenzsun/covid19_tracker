""" Map of COVID19 cases by state in the USA.
    Source: https://covidtracking.com/data/api
"""
import requests
import csv

# Load the Pandas libraries with alias 'pd'
import pandas as pd
import plotly.express as px

# Read data from file
state_df = pd.read_csv("https://api.covidtracking.com/v1/states/current.csv")

fig = px.choropleth(state_df,  # Input Pandas DataFrame
                    locations="state",  # DataFrame column with locations
                    color="positive",  # DataFrame column with color values
                    hover_name="state", # DataFrame column hover info
                    locationmode = 'USA-states', # Set to plot US States
                    color_continuous_scale='amp', #white to maroon color scale
)
fig.update_layout(
    title_text = 'Positive COVID-19 Cases Per State',
    geo_scope='usa',  # Plot only the USA instead of globe
    coloraxis_colorbar=dict(title='Positive Cases'),
)

fig.show()  # Output the plot to the screen
