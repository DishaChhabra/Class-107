import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/whitehatjr/Data-Analysis-by-visualisation/master/data.csv')
import plotly.graph_objects as pg

groups = data.groupby('level')['attempt'].mean()
print(groups)

graph = pg.Figure(pg.Bar(x=groups, y=['level 1', 'level 2', 'level 3', 'level 4'], orientation='h'))
graph.show()