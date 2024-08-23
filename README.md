Создать образ:
docker build -t pos_rate:v0.0 POS_rate/

Запустить контейнер:
docker run -it -p 8000:8000 --name pos_rate  pos_rate:v0.0
