# plot.py

import seaborn as sns
import matplotlib.pyplot as plt
import xarray as xr

def time_series( *data_xarray, label=None):
    sns.set(style="whitegrid")  # Set Seaborn style
    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed

    # Plot the xarray DataArray
    data_xarray.plot(marker='o', label=label)

    # Plot each data array
    for i, data_array in enumerate(data_arrays):
        label = labels[i] if labels else f'Data Array {i + 1}'
        data_xarray.plot(marker='o', label=label)

    plt.title('Time Series Plot')
    plt.xlabel('Time Step')
    plt.ylabel('Value')
    plt.legend()
    plt.show()
