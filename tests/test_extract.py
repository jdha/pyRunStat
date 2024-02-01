# test_extract.py

import unittest
import os
import numpy as np
import xarray as xr
from pyrunstat.extract import read_text

class TestExtractData(unittest.TestCase):
    def setUp(self):
        # Create a temporary file with test data
        self.test_file_path = 'test_file.txt'
        with open(self.test_file_path, 'w') as test_file:
            test_file.write('1.0 2.0 3.0 4.0 5.0 6.0 7.0 8.0 9.0 10.0 11.0\n')
            test_file.write('2.0 3.0 4.0 5.0 6.0 7.0 8.0 9.0 10.0 11.0 12.0\n')

    def tearDown(self):
        # Remove the temporary test file
        os.remove(self.test_file_path)

    def test_read_text_ssh_max(self):
        # Test extracting 'ssh_max' column
        data_xarray = read_text(self.test_file_path, 'ssh_max')

        # Create expected xarray.DataArray
        expected_values = [4.0, 5.0]
        expected_xarray = xr.DataArray(expected_values, dims=['time'], coords={'time': np.arange(len(expected_values))})

        # Check the xarray.DataArray equality
        xr.testing.assert_equal(data_xarray, expected_xarray)

    def test_read_text_U_max(self):
        # Test extracting 'U_max' column
        data_xarray = read_text(self.test_file_path, 'U_max')

        # Create expected xarray.DataArray
        expected_values = [6.0, 7.0]
        expected_xarray = xr.DataArray(expected_values, dims=['time'], coords={'time': np.arange(len(expected_values))})

        # Check the xarray.DataArray equality
        xr.testing.assert_equal(data_xarray, expected_xarray)

    def test_read_text_S_min(self):
        # Test extracting 'S_min' column
        data_xarray = read_text(self.test_file_path, 'S_min')

        # Create expected xarray.DataArray
        expected_values = [8.0, 9.0]
        expected_xarray = xr.DataArray(expected_values, dims=['time'], coords={'time': np.arange(len(expected_values))})

        # Check the xarray.DataArray equality
        xr.testing.assert_equal(data_xarray, expected_xarray)

    def test_read_text_S_max(self):
        # Test extracting 'S_max' column
        data_xarray = read_text(self.test_file_path, 'S_max')

        # Create expected xarray.DataArray
        expected_values = [10.0, 11.0]
        expected_xarray = xr.DataArray(expected_values, dims=['time'], coords={'time': np.arange(len(expected_values))})

        # Check the xarray.DataArray equality
        xr.testing.assert_equal(data_xarray, expected_xarray)

    def test_read_text_invalid_variable(self):
        # Test that an error is thrown for an invalid variable
        with self.assertRaises(ValueError):
            read_text(self.test_file_path, 'invalid_variable')

if __name__ == '__main__':
    unittest.main()
