-- Creates a database and the user
-- if if already exist then don't do it
CREATE DATABASE IF NOT EXISTS hbtn_0c_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON * . * TO 'user_0d_2'@'localhost';
