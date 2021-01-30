#FROM pytorch/pytorch:latest
FROM pytorch/pytorch
RUN mkdir -p /usr/src/detectApp
WORKDIR /usr/src/detectApp

COPY . /usr/src/detectApp

RUN pip install --no-cache-dir -r requirements.txt

#docker volume create model_volume
#VOLUME /model_volume
#docker container run --mount source=my_volume, target=/usr/src/model_volume my_image

CMD ["python3", "main.py"]

#docker run --rm -v model_volume:/usr/src/model_volume --name dtct  detection_docker


