🩸 Blood Group Prediction Using Fingerprint Patterns
📌 Project Description

This project is a deep learning-powered web application that predicts the blood group of a person from a fingerprint image. The system uses a trained VGG16 Convolutional Neural Network model integrated with a Flask backend and MySQL database to generate automated predictions.

The platform provides user authentication, tracks prediction history, and includes an admin dashboard for managing system data.

🧠 Problem It Solves

Blood group identification in the real world normally requires invasive blood tests and manual lab analysis. This application explores a non-invasive AI-based alternative by using fingerprint image patterns for prediction.

It helps achieve:

faster prediction results

reduced human effort

automated classification

easy accessibility through a browser interface

✨ Features

secure login and signup system

fingerprint image upload for prediction

image format validation

preprocessing of fingerprint images

blood group prediction with deep learning

display of confidence score

user prediction history maintenance

admin panel for managing users

contact and privacy pages

🛠 Technologies Used
Backend

Python

Flask

TensorFlow

Keras

Werkzeug Security

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

Scikit-Learn

Matplotlib

⚙ Workflow of the System

user uploads a fingerprint image

system validates the image format

image preprocessing is applied

VGG16 model analyzes the image

probabilities for each class are generated

final blood group is selected

confidence score is displayed

result is stored in database

📂 Project Structure
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
│   ├── contact.html
│   └── how_it_works.html
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

Create a requirements.txt file in the project root and include the following packages:

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


Then execute:

pip install -r requirements.txt

4. Database Setup

Make sure MySQL is installed and running on your system.

Create a database named blood_detector.

Import the SQL schema file included in the repository:

mysql -u root -p blood_detector < blood_detector.sql

5. Configure Upload Folder

Ensure the uploads directory exists inside the static folder:

mkdir static/uploads

6. Run the Application

Start the Flask development server:

python app.py

7. Access the Web Interface

Open your browser and navigate to:

http://127.0.0.1:5000

⚠ Limitations

requires clear fingerprint images

prediction accuracy depends on dataset size

not suitable for critical medical diagnosis

needs further training for real-world use

🔮 Future Enhancements

expand and improve dataset

increase model accuracy

integrate mobile fingerprint scanning

deploy the system on cloud platforms

enhance UI and UX design

💻 Conclusion

Blood group prediction using fingerprint images is a creative intersection of deep learning and biomedical analysis. With further research and improvements, this system can evolve into a helpful non-invasive screening application.
