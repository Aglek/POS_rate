
ARG BASE_IMAGE=python:3.11.9-slim
FROM ${BASE_IMAGE}

COPY requirements.txt .
COPY . /app
WORKDIR /app 

RUN pip install -r requirements.txt

VOLUME /rates

ENTRYPOINT ["python3"]
CMD ["app.py"]
