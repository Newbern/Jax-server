CREATE DATABASE IF NOT EXISTS jax_server;

USE jax_server;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE devices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    api_key VARCHAR(255) NOT NULL UNIQUE,
    device_name VARCHAR(100) NOT NULL,
    device_type VARCHAR(50) NOT NULL,
    last_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE sessions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    device_id INT NOT NULL,
    session_token VARCHAR(255) NOT NULL UNIQUE,
    expires_at TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    FOREIGN KEY (device_id) REFERENCES devices(id) ON DELETE CASCADE
);

CREATE TABLE alarms (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    time TIME NOT NULL,
    day ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') NOT NULL,
    message VARCHAR(255) NOT NULL,
    is_repeat BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- CREATE TABLE smart_plug (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     device_id INT NOT NULL,
--     plug_name VARCHAR(100) NOT NULL,
--     status ENUM('ON', 'OFF') DEFAULT 'OFF',
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     FOREIGN KEY (device_id) REFERENCES devices(id) ON DELETE CASCADE
-- );

-- CREATE TABLE media (
-- 	id INT NULL,
-- 	user_id INT NULL,
-- 	movie VARCHAR(50) NULL DEFAULT NULL,
-- 	position INT NULL DEFAULT NULL
-- )

-- CREATE TABLE movies (
--     id INT AUTO_INCREMENT PRIMARY KEY,

--     title VARCHAR(255) NOT NULL,
--     year INT,

--     genre VARCHAR(100),

--     filename VARCHAR(255),
--     filepath TEXT,

--     poster_path TEXT,
--     backdrop_path TEXT,

--     runtime INT,
--     rating FLOAT,

--     overview TEXT,

--     added DATETIME DEFAULT CURRENT_TIMESTAMP,

--     scanned BOOLEAN DEFAULT FALSE
-- );