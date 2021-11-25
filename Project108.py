import plotly.figure_factory as ff
import pandas as pd
df = pd.read_csv('C:/Users/Krithi/Desktop/Python/dataProject108.csv')
fig = ff.create_distplot([df["Avg Rating"].tolist()], ["average_rating"])
fig.show()