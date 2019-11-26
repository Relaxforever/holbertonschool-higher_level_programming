-- creates a table in a database
-- if it doesn't exist create it
SELECT cities.id, cities.name, states.name FROM states INNER JOIN
cities ON cities.state_id=states.id;
