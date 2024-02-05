# test_extract.py

import os
import unittest

import xarray as xr

from pyrunstat.extract import read_text


class TestExtractData(unittest.TestCase):
    def setUp(self):
        # Create a temporary file with test data
        self.test_file_path = "test_file.txt"
        with open(self.test_file_path, "w") as test_file:
            test_file.write(
                "it :      60    |ssh|_max:  0.23E-04 |U|_max: "
                + "0.16E-02 S_min:  0.34E+02 S_max: "
                + "0.36E+02\n"
            )
            test_file.write(
                "it :      61    |ssh|_max:  0.22E-04 |U|_max: "
                + "0.15E-02 S_min:  0.35E+02 S_max: "
                + "0.37E+02\n"
            )

    def tearDown(self):
        # Remove the temporary test file
        os.remove(self.test_file_path)

    def test_read_text_ssh_max(self):
        # Test extracting 'ssh_max' column
        data_xarray = read_text(self.test_file_path, "ssh_max")

        # Create expected xarray.DataArray
        expected_values = [0.23e-04, 0.22e-04]
        expected_xarray = xr.DataArray(
            expected_values,
            dims=["time"],
            coords={"time": [60, 61]},
        )

        # Check the xarray.DataArray equality
        xr.testing.assert_equal(data_xarray, expected_xarray)

    def test_read_text_U_max(self):
        # Test extracting 'U_max' column
        data_xarray = read_text(self.test_file_path, "U_max")

        # Create expected xarray.DataArray
        expected_values = [0.16e-02, 0.15e-02]
        expected_xarray = xr.DataArray(
            expected_values,
            dims=["time"],
            coords={"time": [60, 61]},
        )

        # Check the xarray.DataArray equality
        xr.testing.assert_equal(data_xarray, expected_xarray)

    def test_read_text_S_min(self):
        # Test extracting 'S_min' column
        data_xarray = read_text(self.test_file_path, "S_min")

        # Create expected xarray.DataArray
        expected_values = [0.34e02, 0.35e02]
        expected_xarray = xr.DataArray(
            expected_values,
            dims=["time"],
            coords={"time": [60, 61]},
        )

        # Check the xarray.DataArray equality
        xr.testing.assert_equal(data_xarray, expected_xarray)

    def test_read_text_S_max(self):
        # Test extracting 'S_max' column
        data_xarray = read_text(self.test_file_path, "S_max")

        # Create expected xarray.DataArray
        expected_values = [0.36e02, 0.37e02]
        expected_xarray = xr.DataArray(
            expected_values,
            dims=["time"],
            coords={"time": [60, 61]},
        )

        # Check the xarray.DataArray equality
        xr.testing.assert_equal(data_xarray, expected_xarray)

    def test_read_text_invalid_variable(self):
        # Test that an error is thrown for an invalid variable
        with self.assertRaises(ValueError):
            read_text(self.test_file_path, "invalid_variable")


if __name__ == "__main__":
    unittest.main()
