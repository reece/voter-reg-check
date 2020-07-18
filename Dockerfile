FROM ubuntu:20.04

RUN apt update && apt upgrade -y && apt install -y \
    curl \
    git \
    python3-pip \
    zip

RUN pip3 install -U setuptools pip

COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

COPY . /app/
WORKDIR /app
RUN python3 setup.py install

EXPOSE 5000

CMD ["voter-reg-check-service"]
