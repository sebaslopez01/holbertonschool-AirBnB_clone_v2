-- Create database and user
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'user_0d_1pwd';
GRANT ALL PRIVELEGES ON hbnb_dev_db TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema TO 'hbnb_dev'@'localhost';