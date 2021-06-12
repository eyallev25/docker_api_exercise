FROM python:3

COPY . /tests
WORKDIR /tests


RUN apt-get update \
    && apt-get --no-install-recommends install -y curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./tests/support/docker_utils.py" ]