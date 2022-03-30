import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('data.csv', sep=';')
#size of a column
r = df.Nota1.size
colors = [['rgb(255,0,0)'],
          ['rgb(255,0,0)' if pd.isnull(df.Nota1[v]) else 'rgb(10,10,10)' for v in range(r)],
          ['rgb(255,0,0)' if pd.isnull(df.Nota2[v]) else 'rgb(10,10,10)' for v in range(r)]]
fig = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df.Nombre, df.Nota1, df.Nota2],
               fill_color=colors,
               align='left')
)])
fig.show()