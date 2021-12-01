import csv
import statistics
import pandas as pd
import plotly.figure_factory as ff

df = pd.read.csv("medium_data.csv")

def random set of mean(counter):
    data = []
    for i in range(0, counter):
        random index = random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def setup():
    mean list = []
    for i in range(0,100):
        set_of_means=  random_set_of_mean(30)
        mean_list.append(set_of_means)

def show fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df],["temp"], show_hist=False)
    fig.show()