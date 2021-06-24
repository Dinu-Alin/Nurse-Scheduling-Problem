import operator
from matplotlib import pyplot as plt

from input import GENERATIONS
from utility_functions import get_schedule, get_fitness
from week import Week

import numpy as np
import math

colors = ['white']


def plot_answer(best_population, fitness):
    plt.rcParams.update(
        {
            'font.size': 20,
            'axes.titlesize': 35,
            'axes.facecolor': 'white'
        }
    )

    week = []
    for day in Week:
        week.append(day.__str__())

    values = get_schedule(best_population[0].chromosome)

    x = np.arange(len(week))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()

    ax.set_ylabel('Number of Nurses')
    ax.set_xlabel('Days')
    ax.set_title(f"Total sum: {get_fitness(best_population[0])[1]}")
    ax.set_xticks(x)
    ax.set_xticklabels(week)

    pps = ax.bar(x, values, width, label='population')
    for p in pps:
        height = p.get_height()
        ax.annotate('{}'.format(height),
                    xy=(p.get_x() + p.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

    plt.get_current_fig_manager().full_screen_toggle()
    plt.draw()
    plt.waitforbuttonpress(0)
    plt.close()


def plot_result(history):
    plots = []

    plt.rcParams.update(
        {
            'font.size': 7,
            'axes.titlesize': 12,
            'axes.facecolor': 'black'
         }
    )
    plt.get_current_fig_manager().full_screen_toggle()
    plt.subplots_adjust(hspace=1, wspace=0.3)

    division = math.ceil(GENERATIONS / 3)
    print(division)

    for i in range(len(history)):
        if i < division:
            index = i
            row = 0
        elif i < division * 2:
            index = (i - division)
            row = 1
        else:
            index = (i - (division * 2))
            row = 2
        plot = plt.subplot2grid((3, division), (row, index))
        plots.append(plot)

    for index, gen in enumerate(history):
        plot = plots[index]
        plot.set_title('Generation {0},\n Best individual: {1}'.format(index + 1, str(round((max(gen.values())), 5))))
        plot.tick_params(left=False)
        plot.set(yticklabels=[])
        gen = dict(sorted(gen.items(), key=operator.itemgetter(1)))
        plot.barh(list(gen.keys()), gen.values(), color=colors, align='center', height=0.6)
    plt.draw()
    plt.waitforbuttonpress(0)
    plt.close()