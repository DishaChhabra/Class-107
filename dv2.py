from this import d
import pandas as pd
import plotly.graph_objects as pg
data = pd.read_csv('https://raw.githubusercontent.com/whitehatjr/Data-Analysis-by-visualisation/master/data.csv')

#filtering a location
student = data.loc[data['student_id']=='TRL_xsl']
print(student)
groups = student.groupby('level')['attempt'].mean()
print(groups)
graph = pg.Figure(pg.Bar(x=groups, y=['Level 1', 'Level 2', 'Level 3', 'Level 4'], orientation='h'))
graph.show()