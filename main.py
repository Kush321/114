import pandas as pd
import plotly.express as px

df = pd.read_csv('d.csv')
fig = px.scatter(df, x="TOEFL Score", y="Chance of Admit ")
fig.show()