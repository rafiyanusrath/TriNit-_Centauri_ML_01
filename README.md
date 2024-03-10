# Automated-Road-Damage-Detection-for-Infrastructure-Maintenance-Using-Yolov8

This project aims to automate the process of road damage detection for infrastructure maintenance using machine learning techniques.

Video Presentation: https://drive.google.com/file/d/11_2Is0I-EMBn9Ae1p5eSu23otedka92I/view?usp=sharing

## Table of Contents
- [Data Preprocessing](#data-preprocessing)
- [Training](#training)
- [Prediction](#prediction)
- [Coding and Making the UI in PyQt](#coding-and-making-the-ui-in-pyqt)
- [Deployment](#deployment)

## Data Preprocessing
We utilized three datasets provided to us for training: Japan, India, and Czech Republic. Annotations were provided in XML format, so we converted them using the tool provided in this repository. After conversion, we obtained annotations for 10 classes: 'D00', 'D40', 'D10', 'D20', 'D44', 'D01', 'D11', 'D50', 'D43', 'D0w0'.

To prepare the data for training, we split it into an 80-20 ratio for training and validation sets respectively.

## Training
For training, we employed the YOLOv8n model. The model was trained using the preprocessed data, incorporating the annotations and images from the training set.

## Prediction
To evaluate the performance of our model, we utilized testing images provided in the dataset. A few predicted images are available in this repository, generated using the custom weights obtained from training.

## Coding and Making the UI in PyQt
We developed the user interface (UI) using PyQt for three purposes: image detection, video input detection, and real-time detection. The UI interface includes the following features:
- **Frame Analysis:** The application can count the number of classes present in the frame.
- **Enhancement Techniques:** We implemented image enhancement techniques to improve prediction accuracy.
- **Maintenance Status:** The UI provides a maintenance status indicator (Low, Medium, High) based on the detection happening in the frame. This status can be adjusted according to specific needs.

## Deployment
Instructions for deploying the project in a real-world setting are provided in the repository. This includes steps for deploying the model and UI, managing dependencies, and considerations for scalability and maintenance.

