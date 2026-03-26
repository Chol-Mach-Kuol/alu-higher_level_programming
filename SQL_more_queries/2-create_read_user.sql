-- Create database user_2_db and user user_0d_2 with root privileges and SELECT, INSERT on user_2_db
CREATE DATABASE IF NOT EXISTS user_2_db;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';
GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
