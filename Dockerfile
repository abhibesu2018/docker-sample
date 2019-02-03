FROM ubuntu:16.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    software-properties-common
RUN add-apt-repository universe
RUN apt-get update && apt-get install -y \
    vim \
    python2.7 \
    python-pip

RUN pip install -U pip

# Install dependencies
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt --ignore-installed

EXPOSE 5000
RUN chmod -R a+x /app/
CMD python ./src/index.py

