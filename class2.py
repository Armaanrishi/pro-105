import csv
with open('class2.csv',newline='')as f:
    reader = csv.reader(f)
    filedata = list(reader)
filedata.pop(0)
totalMarks = 0
totalEntries = len(filedata)
for marks in filedata:
    totalMarks = totalMarks + float(marks[1])
mean = totalMarks/totalEntries
print(mean)
import pandas as pd
import plotly.express as px
df = pd.read_csv('class2.csv')
figure = px.scatter(df,x="Student Number",y="Marks")
figure.update_layout(shapes = [dict(type='line',y0=mean,y1=mean,x0=0,x1=totalEntries)])
figure.update_yaxes(rangemode = "tozero")
figure.show()