🩸 Blood Group Prediction Using Fingerprint Patterns with Deep Learning
📌 Project Description

This project is a deep learning-powered web application that predicts the blood group of a person from a fingerprint image. The system uses a trained VGG16 Convolutional Neural Network model integrated with a Flask backend and MySQL database to provide quick and automated predictions.

The platform includes secure user authentication, prediction history tracking, and an admin dashboard for system management.

🧠 Problem It Solves

Traditional blood group identification requires invasive medical tests and manual laboratory procedures. This system proposes a non-invasive alternative by analyzing fingerprint images using Artificial Intelligence. It helps achieve:

faster prediction results

reduced human effort

automated classification

easy accessibility via a web browser

✨ Features

secure login and signup system

fingerprint image upload for prediction

image validation and preprocessing

display predicted blood group

confidence score for each prediction

user prediction history maintenance

admin panel for managing users and donor data

contact and privacy pages

🛠️ Technologies Used
Backend

Python

Flask

TensorFlow

Keras

Werkzeug

MySQL Connector

OS Module

Datetime Module

Frontend

HTML

CSS

JavaScript

Machine Learning and Libraries

VGG16 Pretrained CNN Model

NumPy

OpenCV

Pillow

Pillow Image Processing

Scikit-Learn

Matplotlib

⚙️ Workflow of the System

user uploads a fingerprint image

system checks for valid image format

preprocessing is applied

VGG16 model predicts probabilities

final blood group is selected

confidence score is displayed

result is stored for future reference

📂 Project Structure
blood-group-prediction/
│
├── app.py
├── hashed_pass.py
├── hashed_pass.py
├── model_blood_group_detection_vgg16.h5
│
├── static/
│   └── uploads/
│
├── templates/
│   ├── about.html
│   ├── account.html
│   ├── admin.html
│   ├── admin_donors.html
│   ├── base.html
│   ├── contact.html
│   ├── edit_account.html
│   ├── history.html
│   ├── how_it_works.html
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   ├── predict.html
│   ├── predict.html
│
└── blood_detector.sql

🚀 Installation and Setup Guide
1. Clone the Repository

Open terminal and run:

git clone https://github.com/apsarab08/blood-group-prediction.git
cd blood-group-prediction

2. Create a Virtual Environment

On Windows:

python -m venv .venv
.venv\Scripts\activate


On Linux or Mac:

python3 -m venv .venv
source .venv/bin/activate

3. Install Required Dependencies

Create a requirements.txt file in the project root and add:

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


Then run:

pip install -r requirements.txt

4. Database Setup

Ensure MySQL is installed and running.

Create a database named blood_detector.

Import the SQL file included in the repository:

mysql -u root -p blood_detector < blood_detector.sql

5. Configure Upload Folder

Make sure the upload directory exists:

mkdir static/uploads

6. Run the Application

Start the Flask server:

python app.py

7. Access the Web Interface

Open your browser and go to:

http://127.0.0.1:5000

⚠️ Limitations

requires clear fingerprint images

accuracy limited by dataset size

not intended for critical medical diagnosis

needs further training for real-world use

🔮 Future Enhancements

expand the dataset

improve model accuracy

integrate mobile scanning

deploy on cloud platforms

enhance UI and UX

💻 Conclusion

Blood group prediction using fingerprint patterns is an innovative application of deep learning in the biomedical domain. With further research and real-world data, this system can evolve into a useful non-invasive screening tool.
