# syntax=docker/dockerfile:1
FROM python:3.9

RUN mkdir /notebooks
WORKDIR /notebooks
COPY ./pycaret /notebooks/pycaret
COPY ./datasets /notebooks/datasets

RUN pip install pycaret notebook

CMD ["jupyter","notebook","--ip=0.0.0.0","--port=8888","--no-browser","--allow-root", "--notebook-dir=/notebooks"]

EXPOSE 8888