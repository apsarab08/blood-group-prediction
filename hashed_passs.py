from werkzeug.security import generate_password_hash

password = "Admin@123"  # your desired password
print(generate_password_hash(password))
