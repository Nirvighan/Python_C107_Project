# IMPORT NEEDED MODULES
import csv
import pandas as pd
import plotly.express as px


# READ THE CSV FILE
df = pd.read_csv('data.csv')

# FIND THE MEAN OF ATTEMPT ACCORDING TO STUDENT IN EACH LEVEL
data = df.groupby(["student_id","level"], as_index = False)["attempt"].mean()

# PRINT THE MEAN
print(data)

# PLOT THE GRAPH 
fig = px.scatter(data,x = "student_id",y = "level",color ="attempt",size = "attempt")
fig.show() 