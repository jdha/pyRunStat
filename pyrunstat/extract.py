# extract.py

import numpy as np
import xarray as xr

def read_text(file_path, variable):
    # Mapping of variable strings to column indices
    variable_mapping = {
        'ssh_max': 4,
        'U_max': 6,
        'S_min': 8,
        'S_max': 10
    }

    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read all lines from the file
            lines = file.readlines()

            # Extract the specified column data
            column_index = variable_mapping.get(variable)
            if column_index is None:
                raise ValueError(f"Invalid variable: {variable}")

            data_array = [float(line.split()[column_index]) for line in lines]
            time_array = [float(line.split()[2]) for line in lines]

            # Convert the list to a NumPy array
            data_array = np.array(data_array)
            time_array = np.array(time_array)

            # Create an xarray DataArray
            data_xarray = xr.DataArray(data_array, dims=['time'], coords={'time': time_array})

            return data_xarray

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def read_nc(file_path, variable):

    raise ValueError(f"read_nc hasn't been written yet")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
