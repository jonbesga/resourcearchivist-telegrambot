FROM python:alpine

# Needed to install cryptography package
RUN apk --no-cache add gcc musl-dev python3-dev libffi-dev openssl-dev

WORKDIR /opt

RUN pip install pipenv

COPY Pipfile* /opt/

RUN pipenv install --system --deploy

COPY . /opt

RUN python setup.py install

CMD archivist