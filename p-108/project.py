import csv 
import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")

pc = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
fig = px.scatter(
pc,
x="student_id",
y="level", 
size="attempt",
color="attempt"
)
fig.show()