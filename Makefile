SHELL := /bin/bash

IMAGE_NAME := pos_rate
IMAGE_TAG := v1.0

CONTAINER_NAME := pos_rate
CONTAINER_PORT := 5001

VOLUME_NAME := rates

#
build:
	@make rmi
	@docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .

#
run:
	@mkdir -p rates
	@docker volume create $(VOLUME_NAME)
	@docker run --rm\
	--name $(CONTAINER_NAME) \
	-p $(CONTAINER_PORT):5001 \
	-v $(VOLUME_NAME):/rates \
	-e SECRET_KEY = '123qwe' \
	$(IMAGE_NAME):$(IMAGE_TAG)

#
stop:
	@docker stop $(CONTAINER_NAME)

#
volume-inspect:
	@docker volume inspect $(VOLUME_NAME)

#
volume-prune:
	@docker volume prune

#
rmi:
	@docker rmi $(IMAGE_NAME):$(IMAGE_TAG)

#
exec:
	@docker exec -it $(CONTAINER_NAME) bash

# копирование данных из контейнера на хост в рантайме
cp:
	@docker cp $(CONTAINER_NAME):/rates .


