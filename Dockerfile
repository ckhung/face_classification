FROM asashiho/ml-jupyter-python3

#Face classificarion dependencies & web application
RUN pip3 install flask statistics opencv-python==3.2.0.8

COPY . /ekholabs/face-classifier

WORKDIR /ekholabs/face-classifier

ENV FACE_CLASSIFICATION_PATH=/ekholabs/face-classifier
ENV PYTHONPATH=$PYTHONPATH:$FACE_CLASSIFICATION_PATH/src
ENV FACE_CLASSIFIER_PORT=8084
EXPOSE $FACE_CLASSIFIER_PORT

#ENTRYPOINT ["python3"]
#CMD ["src/web/faces.py"]
