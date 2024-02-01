FROM continuumio/miniconda3

WORKDIR /src/pyRunStat

COPY environment.yml /src/pyRunStat/

RUN conda install -c conda-forge gcc python=3.11 \
    && conda env update -n base -f environment.yml

COPY . /src/pyRunStat

RUN pip install --no-deps -e .
