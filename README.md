Создать образ:
docker build -t pos_rate:v0.0 flask_app/

Запустить контейнер:
docker run -it -p 8000:8000 --name pos_rate  pos_rate:v0.0
