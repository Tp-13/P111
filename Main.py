import plotly.figure_factory as ff
import pandas as pd
import csv
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv("StudentMarks.csv")
data = df["Math_score"].tolist()
""" fig = ff.create_distplot([data], ["Math Scores"], show_hist=False)
fig.show() """

P_mean = statistics.mean(data)
P_stdev = statistics.stdev(data)

print("Mean of the Population: ", P_mean)
print("Standard Deviation of the Population: ", P_stdev)

def randomSetOfMeans(counter):
    dataSet = []
    for i in range (0, counter):
        randomIndex = random.randint(0, len(data) - 1)
        value = data[randomIndex]
        dataSet.append(value)
    
    mean = statistics.mean(dataSet)
    return(mean)

meanList = []
for i in range (0,100):
    setOfMeans = randomSetOfMeans(30)
    meanList.append(setOfMeans)

S_mean = statistics.mean(meanList)
S_stdev = statistics.stdev(meanList)

print("Mean of the Sample: ", S_mean)
print("Standard Deviation of the Sample: ", S_stdev)

first_stdev_start, first_stdev_end = P_mean - P_stdev, P_mean + P_stdev
second_stdev_start, second_stdev_end = P_mean - (2*P_stdev), P_mean + (2*P_stdev)
third_stdev_start, third_stdev_end = P_mean - (3*P_stdev), P_mean + (3*P_stdev)

fig = ff.create_distplot([meanList], ["Math Scores"], show_hist=False)
fig.add_trace(go.Scatter(x=[P_mean, P_mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_stdev_start, first_stdev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_stdev_end, first_stdev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_stdev_start, second_stdev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_stdev_end, second_stdev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[third_stdev_start, third_stdev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))
fig.add_trace(go.Scatter(x=[third_stdev_end, third_stdev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3")) 

#First Intervention Data Analyzation

df_1 = pd.read_csv("Inter1.csv")
data_1 = df_1["Math_score"].tolist()
meanOfSample1 = statistics.mean(data_1)
print("Mean of Sample 1: ", meanOfSample1)
fig.add_trace(go.Scatter(x=[meanOfSample1, meanOfSample1], y=[0, 0.17], mode="lines", name="Mean of Sample 1"))

#Second Intervention Data Analyzation

df_2 = pd.read_csv("Inter2.csv")
data_2 = df_2["Math_score"].tolist()
meanOfSample2 = statistics.mean(data_2)
print("Mean of Sample 2: ", meanOfSample2)
fig.add_trace(go.Scatter(x=[meanOfSample2, meanOfSample2], y=[0, 0.17], mode="lines", name="Mean of Sample 2"))

#Third Intervention Data Analyzation

df_3 = pd.read_csv("Inter3.csv")
data_3 = df_3["Math_score"].tolist()
meanOfSample3 = statistics.mean(data_3)
print("Mean of Sample 3: ", meanOfSample3)
fig.add_trace(go.Scatter(x=[meanOfSample3, meanOfSample3], y=[0, 0.17], mode="lines", name="Mean of Sample 3"))

fig.show()

#Z-Score
ZScore = (meanOfSample1-P_mean)/P_stdev
print("Z-Score 1: ", ZScore)
ZScore2 = (meanOfSample2-P_mean)/P_stdev
print("Z-Score 2: ", ZScore2)
ZScore3 = (meanOfSample3-P_mean)/P_stdev
print("Z-Score 3: ", ZScore3)