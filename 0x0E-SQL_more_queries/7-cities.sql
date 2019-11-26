-- creates a table in a database
-- if it doesn't exist create it
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE AUTO_INCREMENT
PRIMARY KEY, state_id INT, FOREIGN KEY (state_id) REFERENCES
states(id), name VARCHAR(256) NOT NULL);
