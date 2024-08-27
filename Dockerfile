
ARG BASE_IMAGE=python:3.11-slim
FROM ${BASE_IMAGE}

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app 
COPY app/ .

#VOLUME /rates

EXPOSE 5001

ENV SECRET_KEY = '5f4fa7f2-5265-477c-8552-651b9683ef82'

ENTRYPOINT ["python3"]
CMD ["app.py"]
