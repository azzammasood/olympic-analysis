import dash
from dash import dcc
from dash import html
import numpy as np
import plotly.express as px
import pandas as pd 

data = pd.read_csv('athlete_events.csv')

# Data Inspection
print('Shape of dataset:', data.shape, "\n")
print(data.isnull().sum())

# Data Cleaning
mean_age = data['Age'].mean()
std_age = data['Age'].std()
mean_height = data['Height'].mean()
std_height = data['Height'].mean()
mean_weight = data['Weight'].mean()
std_weight = data['Weight'].mean()

def fill_age_missing_from_Gaussian(column_val):
  if np.isnan(column_val) == True: 
        column_val = np.random.normal(mean_age, std_age, 1)
        if column_val < 0:
            column_val = -(column_val)
  else:
        column_val = column_val
  return column_val

def fill_height_missing_from_Gaussian(column_val):
  if np.isnan(column_val) == True: 
        column_val = np.random.normal(mean_height, std_height, 1)
        if column_val < 0:
            column_val = -(column_val)
  else:
        column_val = column_val
  return column_val

def fill_weight_missing_from_Gaussian(column_val):
  if np.isnan(column_val) == True: 
        column_val = float(np.random.normal(mean_weight, std_weight, 1))
        if column_val < 0:
            column_val = -(column_val)
  else:
        column_val = column_val
  return column_val

data['Age'] = data['Age'].apply(fill_age_missing_from_Gaussian) 
data['Height'] = data['Height'].apply(fill_height_missing_from_Gaussian) 
data['Weight'] = data['Weight'].apply(fill_weight_missing_from_Gaussian) 
data['Medal'] = data['Medal'].fillna('No medal')

print('\nCleaned dataset')
print(data.isnull().sum())

# Visualizations
app = dash.Dash()

# Scatter plot
scatter_fig = px.scatter(
    data,
    x="Age",
    y="Medal",
    hover_name="City",
    size="Weight",
    color="Team",
    log_x=True,
    size_max=60,
)

# pie_fig = px.pie(data, 
#              values='Medal', 
#              names='City', 
#              title='Medal Distribution')

# bar_fig = px.bar(data,
#                  x="Team",
#                  y="Age",
#                  title="Average Age by Team")

app.layout = html.Div([dcc.Graph(id="viz", figure=scatter_fig)])

if __name__ == "__main__":
    app.run_server(debug=False)


