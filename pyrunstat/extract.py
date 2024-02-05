# extract.py

import numpy as np
import xarray as xr


def read_text(file_path, variable):
    # Mapping of variable strings to column indices

    variable_mapping = {"ssh_max": 4, "U_max": 6, "S_min": 8, "S_max": 10}
    units_mapping = {"ssh_max": "m", "U_max": "m/s", "S_min": "", "S_max": ""}
    short_name_mapping = {
        "ssh_max": "max ssh",
        "U_max": "max speed",
        "S_min": "min salt",
        "S_max": "max salt",
    }
    long_name_mapping = {
        "ssh_max": "sea surface height",
        "U_max": "ocean speed",
        "S_min": "salinity",
        "S_max": "salinity",
    }
    desc_mapping = {
        "ssh_max": "Sea Surface Height Maximum",
        "U_max": "Ocean Speed Maximum",
        "S_min": "Salinity Minimum",
        "S_max": "Salinity Maximum",
    }

    # Extract the specified column data
    column_index = variable_mapping.get(variable)
    if column_index is None:
        raise ValueError(f"Invalid variable: {variable}")

    try:
        # Open the file in read mode
        with open(file_path, "r") as file:
            # Read all lines from the file
            lines = file.readlines()

            data_array = [
                float(line.split()[column_index].replace("D", "e")) for line in lines
            ]
            time_array = [float(line.split()[2]) for line in lines]

            # Convert the list to a NumPy array
            data_array = np.array(data_array)
            time_array = np.array(time_array)

            # Create an xarray DataArray
            data_xarray = xr.DataArray(
                data_array, dims=["time"], coords={"time": time_array}
            )

            data_xarray.name = variable

            data_xarray.attrs = dict(
                units=units_mapping.get(variable),
                short_name=short_name_mapping.get(variable),
                long_name=long_name_mapping.get(variable),
                description=desc_mapping.get(variable),
            )

            return data_xarray

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def read_nc(file_path, variable):
    raise ValueError("read_nc hasn't been written yet")
