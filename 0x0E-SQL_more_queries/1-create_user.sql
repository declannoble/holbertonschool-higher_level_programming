-- script to create MYSQL server user

CREATE USER IF NOT EXISTS 'user_0d_1' IDENTIFIED BY 'user_0d_1';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
