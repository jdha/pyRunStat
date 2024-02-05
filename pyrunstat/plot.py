# plot.py

import matplotlib.pyplot as plt
import seaborn as sns


def time_series(*data_xarrays, labels=None):
    sns.set(style="whitegrid")  # Set Seaborn style
    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed

    # Plot each data array
    for i, data_xarray in enumerate(data_xarrays):
        label = labels[i] if labels else f"Data Array {i + 1}"
        data_xarray.plot(label=label)

    plt.title(data_xarray.attrs["description"])
    plt.xlabel("time step")
    # plt.ylabel("Value")
    plt.legend()
    plt.show()
