-- creates a table in a database
-- if it doesn't exist create it
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT '1' UNIQUE, name VARCHAR(256) NOT
NULL);
