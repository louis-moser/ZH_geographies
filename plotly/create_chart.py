import pandas as pd
import plotly
import plotly.graph_objects as go

df = pd.read_csv("../data/Geographies.csv")
df['verlinkt'] = "<a href='" + df["Link"] + "' target='blank' style='color:black'>" + df["Geography"] + "</a>"
topics = [''] + ['Einheiten'] * 7 + df['Topic'].to_list()
geography = ['Einheiten'] + list(df['Topic'].unique()) + df['verlinkt'].to_list()

data = dict(
    character=geography,
    parent=topics,
    # value=list(range(len(topics)))
    )

fig = go.Figure(go.Sunburst(
    labels=geography,
    parents=topics,
    maxdepth=3))
# Update layout for tight margin
# See https://plotly.com/python/creating-and-updating-figures/
fig.update_layout(margin = dict(t=0, l=0, r=0, b=0), )


# html file
plotly.offline.plot(fig, filename='../index.html')