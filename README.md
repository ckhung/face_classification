# Face classification and detection from the [B-IT-BOTS robotics team](https://mas-group.inf.h-brs.de/?page_id=622).
Real-time face detection and emotion/gender classification using fer2013/IMDB datasets with a keras CNN model and openCV.
* IMDB gender classification test accuracy: 96%.
* fer2013 emotion classification test accuracy: 66%.

For more information please consult the [publication](https://github.com/oarriaga/face_classification/blob/master/report.pdf)

# Emotion/gender examples:

![alt tag](images/demo_results.png)

Guided back-prop
![alt tag](images/gradcam_results.png)

Real-time demo:
<div align='center'>
  <img src='images/color_demo.gif' width='400px'>
</div>

[B-IT-BOTS](https://mas-group.inf.h-brs.de/?page_id=622) robotics team :)
![alt tag](images/robocup_team.png)

## Instructions

### Run real-time emotion demo: NOT UPDATED YET, ckhung
> python3 video_emotion_color_demo.py

### Run real-time guided back-prop demo: NOT UPDATED YET, ckhung
> python3 image_gradcam_demo.py

### Make inference on a single image:
> export FACE_CLASSIFICATION_PATH=<project_path> ; python3 image_emotion_gender_demo.py <image_path>

e.g.

> export FACE_CLASSIFICATION_PATH=/home/ckhung/face_classification ; python3 image_emotion_gender_demo.py ../images/test_image.jpg

### Running with Docker

With a few steps one can get its own face classification and detection running. Follow the commands below:

* ```docker pull ckhung/face_classification:18A```
* ```docker run -d --name fc -p 15984:8084 ckhung/face_classification:18A```
* ```curl -v -F image=@/some/image.jpg http://localhost:15984/emo/label```
* ```curl -v -F image=@/some/image.jpg http://localhost:15984/emo/mark > result.png```

### To train previous/new models for emotion classification: NOT UPDATED YET, ckhung

* Download the fer2013.tar.gz file from [here](https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data)

* Move the downloaded file to the datasets directory inside this repository.

* Untar the file:
> tar -xzf fer2013.tar

* Run the train_emotion_classification.py file
> python3 train_emotion_classifier.py

### To train previous/new models for gender classification:

* Download the imdb_crop.tar file from [here](https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/) (It's the 7GB button with the tittle Download faces only).

* Move the downloaded file to the datasets directory inside this repository.

* Untar the file:
> tar -xfv imdb_crop.tar

* Run the train_gender_classification.py file
> python3 train_gender_classifier.py

