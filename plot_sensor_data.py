
import pandas as pd
import glob
import os
from plotly.subplots import make_subplots
import plotly.graph_objects as go

all_files = glob.glob(os.path.join('sense_data', "*.csv"))
df = pd.concat((pd.read_csv(f) for f in all_files))

# Create figure
fig = make_subplots(rows=1, cols=1, subplot_titles='Throttle')

col_list = list(df)

fig.add_trace(go.Scatter(x=df['datetime'], y=df['throttle'], mode='lines', name='speed'), row=1, col=1)

fig.show()
