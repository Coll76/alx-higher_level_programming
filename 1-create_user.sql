-- Creates te first user
CREATE USER IF NOT EXISTS 'user_0d_1'@'%'
IDENTIFIED BY 'user_0d_1_pwd';
GRANT PRIVILEGES ON *.* TO 'user_0d_1'@'%';
