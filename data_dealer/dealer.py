
from random import shuffle
import numpy as np
import matplotlib as mpl

## agg backend is used to create plot as a .png file
mpl.use('agg')

import matplotlib.pyplot as plt

def shuffle_and_deal(data, test_data_ratio):
    shuffle(data)
    return data[:int(len(data) * (1 - test_data_ratio))], data[int(len(data) * (1 - test_data_ratio)):]


def remove_column(data, column_index):
    return_data = []

    for point in data:
        new_point = point[:column_index]
        new_point.extend(point[column_index+1:])
        return_data.append(new_point)
    return return_data


def transpose_data(data):
    return_data = []
    number_of_columns = len(data[0])

    for index in range(number_of_columns):
        return_data.append([])

    for row_index in range(len(data)):
        for col_index in range(number_of_columns):
            return_data[col_index].append(data[row_index][col_index])
    return return_data


def split_data_label(data, label_column):
    return_data = []
    label_data = []

    for point in data:
        new_point = point[:label_column]
        new_point.extend(point[label_column + 1:])
        return_data.append(new_point)
        label_data.append(point[label_column])
    return return_data, label_data


def merge_data_label(data,label):
    merged_data = []
    for index in range(len(data)):
        merged_data_point = data[index]
        merged_data_point.append(label[index])
        merged_data.append(merged_data_point)
    return merged_data


def plot_data(data):
    # Create a figure instance
    np_data = np.asarray(data)
    fig = plt.figure(1, figsize=(9, 6))

    # Create an axes instance
    ax = fig.add_subplot(111)

    # Create the boxplot
    bp = ax.boxplot(np_data.astype(np.float))

    # Save the figure
    fig.savefig('fig2.png', bbox_inches='tight')


def discreteize_data(data, clusters):
    cluster_ranges = []
    discreteized_data = []
    for index in range(len(clusters)):
        high = max(clusters[index])
        low = min(clusters[index])
        cluster_range = [low, high]
        cluster_ranges.append(cluster_range)
    for point in data:
        for index in range(len(cluster_ranges)):
            if cluster_ranges[index][0] <= point <= cluster_ranges[index][1]:
                discreteized_data.append(index)
    return discreteized_data

