FROM python:3.8.3-slim-buster AS build

RUN pip install --upgrade pip

WORKDIR /usr/src/app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED 1

COPY . .

FROM build AS test
RUN pip3 install pytest pytest-cov && rm -rf /root/.cache
RUN pytest --doctest-modules \
  --junitxml=xunit-reports/xunit-result-all.xml \
  --cov \
  --cov-report=xml:coverage-reports/coverage.xml \
  --cov-report=html:coverage-reports/
