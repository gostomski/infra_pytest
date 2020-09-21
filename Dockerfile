FROM python:3.6-slim
MAINTAINER grzegorz@gostomski.pl
COPY . /python-test
WORKDIR /python-test
RUN pip install --no-cache-dir -r requirements.txt
RUN ["pytest", "--variables","variabes.yaml","test_cf_ota.py"]
CMD tail -f /dev/null