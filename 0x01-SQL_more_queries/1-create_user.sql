-- create user if not exist, and allow privelege
CREATE USER IF NOT EXIST 'user_0d_1' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVELEGES ON *.* TO 'user_0d_1'@'localhost';
