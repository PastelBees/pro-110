
import plotly.figure_factory as ff
import statistics
import pandas as pd
import csv
import random
import plotly.graph_objects as go

df = pd.read_csv("data.csv")

data = df["reading_time"].tolist()

def random_set_of_mean(counter):
    data_set = []

    for i in range(0,counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        data_set.append(value)

    mean = statistics.mean(data_set)
    return mean


def plot_graph(mean_list):
    df = mean_list

    mean = statistics.mean(mean_list)

    fig = ff.create_distplot([df], ["reading_time"], show_hist = False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="Mean"))
    fig.show() 

    print("Sampling mean: ", mean)

    population_mean = statistics.mean(data)
    print("Population Mean",population_mean) 


def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)

    plot_graph(mean_list)

setup()