from flask import Flask, render_template, request, redirect, url_for, session, flash
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.imagenet_utils import preprocess_input
import numpy as np
import os
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecretkey123"  # change for production

# Model
MODEL_PATH = 'model_blood_group_detection_vgg16.h5'
try:
    model = load_model(MODEL_PATH)
except Exception as e:
    print(f"Warning: could not load model at {MODEL_PATH}. Error: {e}")
    model = None

# labels mapping (int -> label)
labels = {'A+': 0, 'A-': 1, 'AB+': 2, 'AB-': 3, 'B+': 4, 'B-': 5, 'O+': 6, 'O-': 7}
labels = dict((v, k) for k, v in labels.items())

# Uploads
UPLOAD_FOLDER = os.path.join('static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXT = {'png', 'jpg', 'jpeg', 'bmp', 'gif'}

# MySQL connection — change creds if needed
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Appu@123',
    database='blood_detector'
)
cursor = db.cursor(dictionary=True)

# helpers
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXT

def save_prediction_db(user_id, filename, predicted_label, confidence):
    try:
        cursor.execute(
            "INSERT INTO predictions (user_id, image_name, predicted_label, confidence, timestamp) VALUES (%s,%s,%s,%s,%s)",
            (user_id, filename, predicted_label, confidence, datetime.now())
        )
        db.commit()
    except Exception as e:
        print('DB save prediction error:', e)

def save_contact_db(user_id, name, email, message):
    try:
        cursor.execute(
            "INSERT INTO contact_messages (user_id, name, email, message, timestamp) VALUES (%s,%s,%s,%s,%s)",
            (user_id, name, email, message, datetime.now())
        )
        db.commit()
    except Exception as e:
        print('DB save contact error:', e)

# Routes
@app.route('/', methods=['GET', 'POST'])
def index():
    # Optional: require login to use prediction
    # if 'user_id' not in session:
    #     return redirect(url_for('login'))

    prediction = None
    filename = None

    if request.method == 'POST':
        if 'image' not in request.files:
            flash('No file part', 'error')
            return redirect(request.url)

        file = request.files['image']
        if file.filename == '':
            flash('No selected file', 'error')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
            filename = f"{timestamp}_{filename}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            if model is None:
                prediction = 'Model not loaded on server.'
            else:
                try:
                    img = image.load_img(filepath, target_size=(256, 256))
                    x = image.img_to_array(img)
                    x = np.expand_dims(x, axis=0)
                    x = preprocess_input(x)

                    result = model.predict(x)
                    predicted_class = int(np.argmax(result))
                    predicted_label = labels.get(predicted_class, 'Unknown')
                    confidence = float(result[0][predicted_class] * 100)
                    prediction = f"{predicted_label} ({confidence:.2f}% confidence)"

                    user_id = session.get('user_id') if session.get('user_id') else None
                    save_prediction_db(user_id, filename, predicted_label, confidence)

                except Exception as e:
                    prediction = f"Error during prediction: {e}"
                    print('Prediction error:', e)
        else:
            flash('Invalid file type. Allowed: png,jpg,jpeg,bmp,gif', 'error')
            return redirect(request.url)

    return render_template('index.html', prediction=prediction, image_file=filename)

@app.route('/how-it-works')
def how_it_works():
    return render_template('how_it_works.html')

def save_contact_db(user_id, name, email, message):
    try:
        cursor.execute("""
            INSERT INTO contact_messages (user_id, name, email, message)
            VALUES (%s, %s, %s, %s)
        """, (user_id, name, email, message))

        db.commit()
    except Exception as e:
        print("DB Error (contact_messages):", e)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        user_id = session.get('user_id')  # None if not logged in

        save_contact_db(user_id, name, email, message)

        return redirect(url_for('success'))

    return render_template('contact/contact.html')


@app.route('/privacy')
def privacy():
    return render_template('contact/privacy.html')

@app.route('/success')
def success():
    return render_template('contact/success.html')




@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # use .get so missing fields don't raise KeyError
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip().lower()
        raw_pw = request.form.get('password', '')
        phone = request.form.get('phone', '').strip()
        gender = request.form.get('gender', '').strip()
        location = request.form.get('location', '').strip()
        blood_group = request.form.get('blood_group', '').strip()

        # basic validation (add more as needed)
        if not (name and email and raw_pw):
            flash("Name, email and password are required.", "error")
            return redirect(url_for('signup'))

        password = generate_password_hash(raw_pw)

        try:
            cursor.execute("""
                INSERT INTO users
                  (name, email, password, phone, gender, location, blood_group, created_at)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (name, email, password, phone, gender, location, blood_group, datetime.now()))

            db.commit()
            flash("Signup successful! Login now.", "success")
            return redirect(url_for("login"))

        except Exception as e:
            # log the real error for debug
            print("Signup Error:", repr(e))
            # If email unique constraint triggered, show friendly message
            flash("Email already exists or DB error.", "error")
            return redirect(url_for("signup"))

    # If GET (or any non-POST), render the signup page
    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cursor.execute('SELECT * FROM users WHERE email=%s', (email,))
        user = cursor.fetchone()
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['user_name'] = user['name']
            session['role'] = user.get('role', 'user')    # <-- add this
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid email or password', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out!', 'success')
    return redirect(url_for('login'))

@app.route('/history')
def history():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    cursor.execute("SELECT * FROM predictions WHERE user_id=%s ORDER BY timestamp DESC",
                   (session['user_id'],))
    history = cursor.fetchall()

    return render_template('history.html', history=history)

def admin_required():
    return session.get("role") == "admin"


@app.route('/admin')
def admin_dashboard():
    if not admin_required():
        return "❌ Access denied. Admins only."

    cursor.execute("SELECT * FROM users ORDER BY created_at DESC")
    users = cursor.fetchall()

    cursor.execute("""
        SELECT p.*, u.name 
        FROM predictions p 
        LEFT JOIN users u ON p.user_id = u.id
        ORDER BY p.timestamp DESC
    """)
    predictions = cursor.fetchall()

    return render_template("admin.html", users=users, predictions=predictions)

@app.route('/admin/donors')
def admin_donors():
    if not admin_required():
        return "❌ Access denied."

    blood = request.args.get("blood")
    city = request.args.get("city")

    query = "SELECT * FROM users WHERE 1=1"
    params = []

    if blood:
        query += " AND blood_group=%s"
        params.append(blood)

    if city:
        query += " AND location LIKE %s"
        params.append('%' + city + '%')

    cursor.execute(query, params)
    donors = cursor.fetchall()

    return render_template("admin_donors.html", donors=donors)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

@app.route('/account')
def account():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    cursor.execute("SELECT * FROM users WHERE id=%s", (session['user_id'],))
    user = cursor.fetchone()

    return render_template("account.html", user=user)

@app.route('/account/edit', methods=['GET', 'POST'])
def edit_account():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        name = request.form.get("name")
        phone = request.form.get("phone")
        gender = request.form.get("gender")
        location = request.form.get("location")
        blood_group = request.form.get("blood_group")

        cursor.execute("""
            UPDATE users SET 
                name=%s, phone=%s, gender=%s, 
                location=%s, blood_group=%s
            WHERE id=%s
        """, (name, phone, gender, location, blood_group, session['user_id']))

        db.commit()
        flash("Your details were updated!", "success")
        return redirect(url_for("account"))

    cursor.execute("SELECT * FROM users WHERE id=%s", (session['user_id'],))
    user = cursor.fetchone()

    return render_template("edit_account.html", user=user)


if __name__ == '__main__':
    app.run(debug=True)
