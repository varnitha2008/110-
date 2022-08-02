import csv
import pandas as pd
import random
import plotly.figure_factory as ff
import statistics 
import plotly.graph_objects as go

df = pd.read_csv("medium_data.csv")
data=df["claps"].tolist()
fig=ff.create_distplot([data],["claps"],show_hist=False)
fig.show()
population_mean=statistics.mean(data)
standardDeviation =statistics.stdev(data)
print("population mean:- ", population_mean) 
print("std_deviation of population:- ",standardDeviation)

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
     df = mean_list 
     mean = statistics.mean(df) 
     fig = ff.create_distplot([df], ["temp"], show_hist=False) 
     fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN")) 
     fig.show()  

def setup():
    mean_list=[]
    for i in range(0,1000):
        setofmeans=random_set_of_mean(100)
        mean_list.append(setofmeans)
    show_fig(mean_list)
    mean=statistics.mean(mean_list)
    print("meanofsampling1000=",mean)  
setup()    

def setup_for_standardDeviation():
    mean_list=[]
    for i in range(0,1000):
        setofmeans=random_set_of_mean(100)
        mean_list.append(setofmeans)
    show_fig(mean_list)
    stdev=statistics.stdev(mean_list)
    print("meanofsampling1000=",stdev)  
setup_for_standardDeviation()