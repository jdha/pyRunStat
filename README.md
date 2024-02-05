# pyRunStat

.. image:: https://img.shields.io/github/workflow/status/jdha/pyRunStat/CI?logo=github
:target: https://github.com/jdha/pyRunStat/actions
:alt: GitHub Workflow CI Status

.. image:: https://codecov.io/gh/jdha/pyRunStat/branch/main/graph/badge.svg?token=
:target: https://codecov.io/gh/jdha/pyRunStat
:alt: Code Coverage

.. image:: https://readthedocs.org/projects/pyrunstat/badge/?version=latest
:target: https://pyrunstat.readthedocs.io/en/latest/?badge=latest
:alt: Documentation Status

![pre-commit.ci status](https://results.pre-commit.ci/badge/github/jdha/pyRunStat/main.svg )(https://results.pre-commit.ci/latest/github/jdha/pyRunStat/main)

Read in and plot run.stat data from a NEMO simulation.

## Quick Start

- Clone pyRunStat repository:

  ```
  export PYRS_DIR=$PWD/pyRunStat
  git clone https://github.com/jdha/pyRunStat.git
  ```

- Creating a specific conda virtual environment is highly recommended ([click here for more about virtual
  enviroments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)).
  Use the latest version of anaconda (to be added in your .bashrc or load the module in the command line, e.g ` module load anaconda`).

  ```
  cd $PYRS_DIR
  conda env create -n pyrunstat -f environment.yml python=3.11
  ```

- Activate the new virtual environment:

  ```
  conda activate pyrunstat
  ```

- To deactivate (not now!):

  ```
  conda deactivate
  ```

- Install pyRunStat:

  ```
  pip install -e .
  ```

This should result in pyRunStat being installed in the virtual environment,
and can be checked by entering:

```
pyrunstat -v
```

Usage:

```
import pyrunstat as rs

file_path = './run.stat'

# Extract the 'ssh_max'
da_ssh_max = rs.extract.read_text(file_path, 'ssh_max')

# Plot ssh_max timeseries
rs.plot.time_series(da_ssh_max, labels=['SSH maximum'])
```

`pyrunstat.plot.time_series` can accept a list of DataArrays to allow the plotting of multiple timeseries
from different simulations.

## Example: plotting up the output from a run.stat or run.stat.nc file

see: notebook
