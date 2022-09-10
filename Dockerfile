# syntax=docker/dockerfile:1
FROM python:3.9

RUN mkdir /notebooks
WORKDIR /notebooks
COPY ./h2o /notebooks/h2o
COPY ./datasets /notebooks/datasets

RUN apt-get update && apt-get install -y default-jre
RUN pip install requests tabulate future pandas notebook
RUN pip install -f https://h2o-release.s3.amazonaws.com/h2o/latest_stable_Py.html h2o

CMD ["jupyter","notebook","--ip=0.0.0.0","--port=8888","--no-browser","--allow-root", "--notebook-dir=/notebooks"]

EXPOSE 8888