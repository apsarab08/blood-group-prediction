# Blood Group Prediction Using Fingerprint Patterns 🩸

---

## Project Description

This project is a deep learning-powered web application that predicts the blood group from fingerprint images. It uses a pretrained VGG16 Convolutional Neural Network model for classification, integrated with a Flask backend and MySQL database to provide automated predictions.

The platform supports secure user authentication, maintains prediction history, and provides an admin dashboard for system management.

---

## Problem It Solves

Blood group detection traditionally requires invasive blood tests and manual laboratory procedures. This system explores a non-invasive alternative using Artificial Intelligence and fingerprint pattern analysis.

The application helps achieve:

- faster prediction results  
- reduced human effort  
- automated classification  
- easy accessibility via a web browser  

---

## Features

- secure login and signup system  
- upload fingerprint images for prediction  
- image validation and preprocessing  
- display predicted blood group  
- confidence score generation  
- maintain user prediction history  
- admin panel for user management  
- donor data management  
- contact and privacy pages  

---

## Technologies Used

### Backend

- Python  
- Flask  
- TensorFlow  
- Keras  
- Werkzeug  
- MySQL Connector  
- OS Module  
- Datetime Module  

### Frontend

- HTML  
- CSS  
- JavaScript  

### Machine Learning and Libraries

- VGG16 Pretrained CNN Model  
- NumPy  
- OpenCV  
- Pillow  
- Scikit-Learn  
- Matplotlib  

---

## Workflow of the System

- user uploads a fingerprint image  
- system validates the image format  
- image preprocessing is applied  
- VGG16 model analyzes the image  
- probabilities for each class are generated  
- final blood group is selected  
- confidence score is displayed  
- result is stored in database  

---

## Project Structure

```
blood-group-prediction/
│
├── app.py
├── hashed_pass.py
├── model_blood_group_detection_vgg16.h5
│
├── static/
│   └── uploads/
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   ├── predict.html
│   ├── history.html
│   ├── account.html
│   ├── edit_account.html
│   ├── about.html
│   └── contact.html
│
└── blood_detector.sql
```

---

## Installation and Setup Guide

### 1. Clone the Repository

```
git clone https://github.com/apsarab08/blood-group-prediction.git
cd blood-group-prediction
```

### 2. Create a Virtual Environment

On Windows:

```
python -m venv .venv
.venv\Scripts\activate
```

On Linux or Mac:

```
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Setup Database

```
mysql -u root -p blood_detector < blood_detector.sql
```

### 5. Run Application

```
python app.py
```

### 6. Access the Web Interface

```
http://127.0.0.1:5000
```

---

## Limitations

- requires clear fingerprint images  
- accuracy depends on dataset size  
- not suitable for critical medical diagnosis  
- needs further training for real-world usage  

---

## Future Enhancements

- expand the dataset  
- improve model accuracy  
- integrate mobile fingerprint scanning  
- deploy on cloud platforms  
- enhance UI and UX  

---

## Conclusion

Blood group prediction using fingerprints is an innovative intersection of deep learning and biomedical image analysis. With further research and training, this system can evolve into a practical non-invasive screening tool.
