CREATE DATABASE IF NOT EXISTS blood_detector;
USE blood_detector;

-- =============================================
--  USERS TABLE (SIGNUP / LOGIN)
-- =============================================
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role ENUM('user', 'admin') DEFAULT 'user',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    phone VARCHAR(15),
    gender VARCHAR(20),
    location VARCHAR(100),
    blood_group VARCHAR(5);
);

-- =============================================
--  PREDICTIONS TABLE
-- =============================================
CREATE TABLE predictions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    image_name VARCHAR(255) NOT NULL,
    predicted_label VARCHAR(20) NOT NULL,
    confidence FLOAT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE SET NULL ON UPDATE CASCADE
);

-- =============================================
--  CONTACT MESSAGES TABLE
-- =============================================
CREATE TABLE contact_messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NULL,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    message TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE SET NULL ON UPDATE CASCADE
);
