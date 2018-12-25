#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np

def plot_data():
    fig, axs = plt.subplots(2, 1)
    fig.subplots_adjust(hspace=1)

    y = np.loadtxt('../build/lidar.csv', delimiter=',', unpack=True)
    x = [5.991] * len(y)
    axs[0].plot(y, label="nis")
    axs[0].plot(x, label="5.991 - x2.050")
    axs[0].set_title('Lidar')
    axs[0].legend()

    y = np.loadtxt('../build/radar.csv', delimiter=',', unpack=True)
    x = [7.815] * len(y)
    axs[1].plot(y, label="nis")
    axs[1].plot(x, label="7.815 - x2.050")
    axs[1].set_title('Radar')
    axs[1].legend()

    plt.show()

if __name__ == "__main__":
    plot_data()
