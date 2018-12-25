#!/usr/bin/python3

import matplotlib.pyplot as plt
import math
import statistics

def plot_data():
    """Plot acceleration, yaw rate change rate"""
    velocities = []
    lon_accels= []
    yawrates = []
    yaw_accels= []

    with open("obj_pose-laser-radar-synthetic-input.txt", "r") as f:
        previous_timestamp = None
        previous_speed = None
        previous_yawrate = None

        line = f.readline()
        while line:
            fields = line.split('\t')

            timestamp = None
            speed = None
            if fields[0] == 'L':
                timestamp = int(fields[3]) / 1e6
                vx = float(fields[6])
                vy = float(fields[7])
            else:
                timestamp = int(fields[4]) / 1e6
                vx = float(fields[7])
                vy = float(fields[8])

            speed = math.sqrt(vx * vx + vy * vy)
            yawrate = float(fields[-1])

            if previous_timestamp is None:
                previous_timestamp = timestamp
                previous_speed = speed
                previous_yawrate = yawrate
            else:
                # Calculate aceleration from speed
                delta_t = timestamp - previous_timestamp
                previous_timestamp = timestamp

                velocities.append(speed)
                lon_accels.append((speed - previous_speed) / delta_t)
                previous_speed = speed

                yawrates.append(yawrate)
                yaw_accels.append((yawrate - previous_yawrate) / delta_t)
                previous_yawrate = yawrate

            line = f.readline()

    t = [i for i in range(len(velocities))]
    fig, axs = plt.subplots(4, 1)
    fig.subplots_adjust(hspace=1)

    axs[0].plot(t, velocities)
    axs[0].set_title('Velocity')
    axs[0].set_xlabel('sample')
    axs[0].set_ylabel('m/s')

    axs[1].plot(t, lon_accels)
    axs[1].set_title('Acceleration')
    axs[1].set_xlabel('sample')
    axs[1].set_ylabel('m/s/s')

    axs[2].plot(t, yawrates)
    axs[2].set_title('Yawrate')
    axs[2].set_xlabel('sample')
    axs[2].set_ylabel('rad/s')

    axs[3].plot(t, yaw_accels)
    axs[3].set_title('Yaw Acceleration')
    axs[3].set_xlabel('sample')
    axs[3].set_ylabel('rad/s/s')

    plt.show()

    # Statistics of acceleration
    print("Standard viaration of acceleration is " + str(statistics.stdev(lon_accels)))
    print("Variance of acceleration is " + str(statistics.variance(lon_accels)))

    print("Standard viaration of yaw acceleration is " + str(statistics.stdev(yaw_accels)))
    print("Variance of yaw acceleration is " + str(statistics.variance(yaw_accels)))

if __name__ == "__main__":
    plot_data()
