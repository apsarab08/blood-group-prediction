# Blood Group Prediction Using Fingerprint Patterns 🩸🧠

## Project Description
This project is a deep learning-powered web application that predicts the blood group of a person from a fingerprint image. The system uses a trained VGG16 Convolutional Neural Network model integrated with a Flask backend and MySQL database to provide quick and automated predictions.

The platform offers secure user authentication, prediction history tracking, and an admin dashboard for management purposes.

---

## Problem It Solves
Blood group identification usually requires invasive tests and manual lab procedures. This system proposes a non-invasive alternative by analyzing fingerprint images with AI, enabling:
- faster predictions  
- reduced human effort  
- automated classification  
- easy accessibility through a browser  

---

## Features
- secure login and signup system  
- upload fingerprint images for prediction  
- image validation and preprocessing  
- display predicted blood group  
- confidence score for each prediction  
- maintain user prediction history  
- admin panel to manage users and donor data  
- contact and privacy pages  

---

## Technologies Used

### Backend
- Python  
- Flask  
- TensorFlow & Keras  
- Werkzeug for security  
- MySQL Connector  
- OS and Datetime modules  

### Frontend
- HTML  
- CSS  
- JavaScript  

### Machine Learning
- VGG16 Pretrained CNN Model  
- NumPy  
- OpenCV  
- Pillow  
- Scikit-Learn  

---

## Workflow of the System
1. user uploads a fingerprint image  
2. system checks if the image format is valid  
3. preprocessing is applied  
4. VGG16 model predicts probabilities  
5. final blood group is selected  
6. confidence score displayed  
7. result stored for future reference  

---

## Project Structure

vgg16/
│
├── app.py
├── hashed_passs.py
├── model_blood_group_detection_vgg16.h5
│
├── static/
│ └── files/
│ └── Blood_Group_Prediction_Using_Fingerprint.pdf
│
├── templates/
│ ├── about.html
│ ├── account.html
│ ├── admin.html
│ ├── admin_donors.html
│ ├── admin_donors.html
│ ├── base.html
│ ├── contact.html
│ ├── edit_account.html
│ ├── history.html
│ ├── how_it_works.html
│ ├── index.html
│ ├── login.html
│ ├── signup.html
│ └── predict.html
│
└── blood_detector.sql


## Installation and Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/apsarab08/blood-group-prediction.git
cd blood-group-prediction
Step 2: Create Virtual Environment
bash
Copy code
python -m venv .venv
source .venv/bin/activate
Step 3: Install Dependencies
bash
Copy code
pip install -r requirements.txt
Step 4: Database Setup
Import the SQL file into MySQL database:

bash
Copy code
mysql -u root -p OnlineShopping < blood_detector.sql
Step 5: Run the Application
bash
Copy code
python app.py
Open http://127.0.0.1:5000 in your browser.

Requirements File
Create a file named requirements.txt with the following content:

Flask
tensorflow
numpy
opencv-python
mysql-connector-python
Werkzeug
Pillow
pandas
scikit-learn
matplotlib

Model Information
the project uses a VGG16-based CNN model trained on 8 blood group classes

predictions are generated using softmax probabilities

the highest probability class is chosen as the final result

performance depends on dataset quality and size

Limitations
requires clear fingerprint images

accuracy limited by dataset

not intended for critical medical diagnosis yet

needs further training for real-world deployment

Future Enhancements
expand dataset

improve accuracy

integrate mobile scanning

cloud-based deployment

enhanced UI/UX
